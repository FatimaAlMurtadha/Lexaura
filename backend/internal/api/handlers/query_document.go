package handlers

import (
	"encoding/json"
	"net/http"
	"github.com/FatimaAlMurtadha/Lexaura/backend/internal/shared/clients"
)

type QueryRequest struct {
	Question string `json:"question"`
}

func QueryDocument(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}

	var req QueryRequest
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		http.Error(w, "invalid JSON", http.StatusBadRequest)
		return
	}

	if req.Question == "" {
		http.Error(w, "question is required", http.StatusBadRequest)
		return
	}

	result, err := clients.SendQueryToAIService(req.Question)
	if err != nil {
		http.Error(w, "AI-Service error: "+err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.Write([]byte(result))
}