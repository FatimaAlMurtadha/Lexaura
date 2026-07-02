package clients

import (
    "bytes"
    "io"
    "mime/multipart"
    "net/http"
)

func SendToAIService(file io.Reader, filename string) (string, error) {
    body := &bytes.Buffer{}
    writer := multipart.NewWriter(body)

    part, err := writer.CreateFormFile("file", filename)
    if err != nil {
        return "", err
    }

    io.Copy(part, file)
    writer.Close()

    req, err := http.NewRequest("POST", "http://localhost:8000/api/ingest", body)
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