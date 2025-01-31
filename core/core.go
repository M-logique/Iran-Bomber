package core

import (
	"encoding/json"
	"fmt"
	"net/http"
)

const (
	APIURL = "https://m-logique.github.io/files/API.json"
)

func fetchAPI() (error, map[string]interface{}) {
	resp, err := http.Get(APIURL)
	if err != nil {
		return err, nil
	}

	defer resp.Body.Close()

	var result map[string]interface{}
	if err = json.NewDecoder(resp.Body).Decode(&result); err != nil {
		return err, nil
	}

	return nil, result
}

func sendSMS() {
	fmt.Println("Sending SMS")

	err, result := fetchAPI()

	if err != nil {
		panic(err)
	}

	for _, v := range result {
	
		fmt.Println(v)
	}

}

// func main() {
// 	sendSMS()
// }