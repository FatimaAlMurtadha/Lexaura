package handlers

import (
	"net/http"

	"github.com/FatimaAlMurtadha/Lexaura/backend/internal/shared/clients"
)

func UploadPDF(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}

	file, header, err := r.FormFile("file")
	if err != nil {
		http.Error(w, "file is required", http.StatusBadRequest)
		return
	}
	defer file.Close()

	result, err := clients.SendToAIService(file, header.Filename)
	if err != nil {
		http.Error(w, "AI-Service error: "+err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.Write([]byte(result))
}
