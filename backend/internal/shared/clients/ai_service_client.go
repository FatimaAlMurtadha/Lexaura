package clients

import (
	"bytes"
	"fmt"
	"io"
	"mime/multipart"
	"net/http"
	"os"
	"strings"
)

func aiServiceBaseURL() string {
	base := strings.TrimSpace(os.Getenv("AI_SERVICE_URL"))
	if base == "" {
		return "http://localhost:8001"
	}
	return strings.TrimRight(base, "/")
}

func SendToAIService(file io.Reader, filename string) (string, error) {
	body := &bytes.Buffer{}
	writer := multipart.NewWriter(body)

	part, err := writer.CreateFormFile("file", filename)
	if err != nil {
		return "", err
	}

	io.Copy(part, file)
	writer.Close()

	req, err := http.NewRequest("POST", fmt.Sprintf("%s/api/ingest", aiServiceBaseURL()), body)
	if err != nil {
		return "", err
	}

	req.Header.Set("Content-Type", writer.FormDataContentType())

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	respBody, _ := io.ReadAll(resp.Body)
	return string(respBody), nil
}

func SendQueryToAIService(question string) (string, error) {
	payload := strings.NewReader(fmt.Sprintf(`{"question":"%s"}`, question))

	req, err := http.NewRequest("POST", fmt.Sprintf("%s/api/query", aiServiceBaseURL()), payload)

	if err != nil {
		return "", err
	}

	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	respBody, _ := io.ReadAll(resp.Body)
	return string(respBody), nil

}
