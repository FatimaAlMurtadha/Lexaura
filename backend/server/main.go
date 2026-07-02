package main

import (
	"log"
	"net/http"
	"os"

	"github.com/FatimaAlMurtadha/Lexaura/backend/internal/api"
)

func main() {
	port := os.Getenv("PORT")
	if port == "" {
		port = "8000"
	}

	mux := http.NewServeMux()

	// Health check
	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		w.Write([]byte(`{"message":"Backend is running!"}`))
	})

	// Register all API routes
	api.RegisterRoutes(mux)

	addr := ":" + port
	log.Printf("Backend server listening on %s", addr)

	if err := http.ListenAndServe(addr, mux); err != nil {
		log.Fatal(err)
	}
}
