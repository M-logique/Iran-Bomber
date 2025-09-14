package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"io"
	"math/rand"
	"net/http"
	"net/url"
	"os"
	"strconv"
	"strings"
	"text/template"
	"time"
)

// ===== UI: ANSI Color Constants =====
const (
	ColorGreen  = "\033[92m"
	ColorYellow = "\033[93m"
	ColorRed    = "\033[91m"
	ColorBlue   = "\033[94m"
	ColorCyan   = "\033[36m"
	ColorGray   = "\033[90m"
	ColorReset  = "\033[0m"
)

var Version string

// ===== UI: Console and Logo Functions =====

func PrintLogoString() {
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
    {{.G}}╚═════╝  ╚════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
	
	{{.G}}! {{.Gr}}Version: {{.C}}{{.Version}}{{.Reset}}
	`
	tmpl := template.Must(template.New("logo").Parse(logoTemplate))
	data := map[string]string{"Y": ColorYellow, "C": ColorCyan, "Gr": ColorGray, "G": ColorGreen, "Reset": ColorReset, "Version": Version}
	tmpl.Execute(os.Stdout, data)
	fmt.Println()
}

func GetInput(prompt string, checker func(string) bool) string {
	reader := bufio.NewReader(os.Stdin)
	for {
		fmt.Print(prompt)
		txt, _ := reader.ReadString('\n')
		txt = strings.TrimSpace(txt)
		if checker(txt) {
			return txt
		}
		fmt.Printf("%sInvalid input — please try again.%s\n", ColorRed, ColorReset)
	}
}

func PrintSummary(total, success, failed int32) {
	fmt.Printf("\n%s--- Attack Summary ---%s\n", ColorBlue, ColorReset)
	fmt.Printf("Total Requests Sent:   %d\n", total)
	fmt.Printf("%sSuccessful Requests:     %d%s\n", ColorGreen, success, ColorReset)
	fmt.Printf("%sFailed Requests:         %d%s\n", ColorRed, failed, ColorReset)
	fmt.Printf("%s--------------------%s\n", ColorBlue, ColorReset)
}

// ===== DATA LOADING UTILS =====

func isHTTPURL(s string) bool {
	u, err := url.Parse(s)
	return err == nil && (u.Scheme == "http" || u.Scheme == "https") && u.Host != ""
}

func LoadAndFilterAPIs(filePathOrURL, filterURL, phoneNumber string) ([]API, error) {
	var fileBytes []byte
	fmt.Printf("%s[INFO]%s Loading API List from: %s'%s%s%s'%s\n", ColorGreen, ColorYellow, ColorRed, ColorReset, filePathOrURL, ColorRed, ColorReset)

	if isHTTPURL(filePathOrURL) {
		resp, err := http.Get(filePathOrURL)
		if err != nil {
			return nil, fmt.Errorf("failed to load API file from URL '%s': %w", filePathOrURL, err)
		}
		defer resp.Body.Close()
		fileBytes, _ = io.ReadAll(resp.Body)
	} else {
		fpBytes, err := os.ReadFile(filePathOrURL)
		if err != nil {
			return nil, fmt.Errorf("failed to read API file '%s': %w", filePathOrURL, err)
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

func LoadProxies(filePath, url string) ([]string, error) {
	if filePath == "" && url == "" {
		return nil, nil // No proxy source provided
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