package api

import (
	"net/http"

	"github.com/FatimaAlMurtadha/Lexaura/backend/internal/api/handlers"
)

func RegisterRoutes(mux *http.ServeMux) {
	mux.HandleFunc("/upload", handlers.UploadPDF)

}
