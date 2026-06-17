# Lexaura Lite — Project Overview (MVP)

Lexaura Lite is an AI-powered study assistant that helps students understand their study materials by uploading PDFs and asking questions.  
This document summarizes the MVP scope, architecture, technical decisions, and the first feature to implement.

---

 1. MVP Scope

The MVP focuses on the core value of the product:

> Upload a PDF → Extract text → Generate embeddings → Store in ChromaDB → Ask questions using RAG.

Included in MVP:
- PDF upload
- Text extraction
- Chunking
- Embeddings generation
- ChromaDB storage
- RAG search
- Chat answer

Not included in MVP:
- Authentication
- Sessions
- ACL
- Flashcards
- Summaries
- Study Plan
- Dashboard
- Courses management

---

 2. First User Story (MVP)

As a student, I want to upload a PDF file so that the system can understand my study material.

This is the foundation for all future features.

---

 3. System Architecture (MVP)

`
Frontend → Backend → AI-Service → ChromaDB
`

Responsibilities:

Frontend
- Provide a simple upload UI
- Send PDF to backend
- Display success/error messages

Backend (Go)
- Receive PDF
- Validate file
- Generate document_id (UUID)
- Forward file to AI service
- Return success response

AI-Service (Python + FastAPI)
- Extract text from PDF
- Chunk text
- Generate embeddings
- Store vectors in ChromaDB
- Return success

ChromaDB
- Store embeddings
- Support vector search for RAG

---

 4. Technical Specification — PDF Upload

4.1 Backend API

POST /upload
- Content-Type: multipart/form-data
- Body:
  - file: PDF file

Success Response
`json
{
  "status": "success",
  "message": "PDF uploaded and processed"
}
`

Error Response
`json
{
  "status": "error",
  "message": "Invalid file type"
}
`

---

4.2 Backend → AI-Service API

POST /ingest
- Content-Type: multipart/form-data
- Body:
  - file: PDF file
  - document_id: UUID

Success Response
`json
{
  "status": "ok",
  "document_id": "uuid"
}
`

---

 5. AI-Service Processing Pipeline

5.1 PDF Extraction
- Library: pypdf
- Clean text:
  - remove empty lines
  - remove repeated whitespace

5.2 Chunking
- Chunk size: 300–500 tokens
- Overlap: 50 tokens

5.3 Embeddings
- Model: sentence-transformers/all-MiniLM-L6-v2
- Vector size: 384 dimensions

5.4 Vector Store (ChromaDB)
- Collection: documents
- Fields:
  - id: chunk_id
  - document_id: UUID
  - text: chunk text
  - embedding: vector

---

 6. Folder Structure (Monorepo)

`
Lexaura/
│
├── frontend/
│
├── backend/
│   ├── cmd/
│   ├── internal/
│   │   ├── auth/
│   │   ├── learning/
│   │   ├── ai/
│   │   ├── middleware/
│   │   └── shared/
│   └── go.mod
│
├── ai-service/
│   ├── src/
│   │   ├── api/
│   │   ├── features/
│   │   │   ├── ingestion/
│   │   │   ├── rag/
│   │   │   ├── chat/
│   │   │   ├── summaries/
│   │   │   ├── flashcards/
│   │   │   └── studyplan/
│   │   ├── infrastructure/
│   │   │   ├── llm/
│   │   │   ├── embeddings/
│   │   │   ├── vectorstore/
│   │   │   └── storage/
│   │   └── core/
│   └── pyproject.toml
│
├── docker/
│   ├── postgres/
│   ├── redis/
│   └── chroma/
│
├── docker-compose.yml
│
└── docs/
`

---

 7. Acceptance Criteria

- Student can upload a PDF  
- Backend validates and forwards file  
- AI-service extracts text  
- Embeddings stored in ChromaDB  
- Backend returns success  
- Frontend shows success message  
- No errors in logs  
- CI pipeline passes