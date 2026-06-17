# backend
cd Lexaura

git clone https://github.com/evrone/go-clean-template backend

cd backend
go mod edit -module github.com/FatimaAlMurtadha/Lexaura/backend
go mod tidy
rm -rf .git
cd ..

--------------------------------
# frontend
cd frontend

npx create-next-app@latest . --typescript

-----------------------------
# backend
mkdir backend

mkdir backend/cmd backend/internal backend/internal/handlers backend/internal/services backend/internal/repositories backend/internal/models backend/internal/middleware backend/internal/sessions backend/internal/acl backend/internal/ai backend/pkg

go mod init github.com/FatimaAlMurtadha/Lexaura/backend

----------------------------------------------------
# plan 1
1. Implement /ingest in AI-Service  // pipeline
2. Implement /upload in Backend  
3. Build frontend upload UI  
4. Integrate all components  
5. Add RAG search  
6. Add chat endpoint  