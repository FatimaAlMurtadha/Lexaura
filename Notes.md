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

----------------------------------------------------------
# ai-service
cd ai-service
uv run uvicorn src.main:app --reload

//
- src/infrastructure/storage/pdf.py : pdf extraction + file handling + any file or storage logic (io infrastructure) - NOT a business logic.

- src/infrastructure/vectorstore/ chromaDB client to create collections + add embeddings + search (similarity search) LIKE client.py + collection.py + store.py // (VECTOR DATABASE).

- src/infrastructure/llm/ here is to deal with llm -> create ollama or openAI + Prompts LIKE ollama_client.py || openai.py + prompt_templates.py. 

- src/infrastructure/embeddings/ here is to deal with (sentenceTransformers model + HuggingFace embeddings). It is responsible to convert the text to vector. LIKE model.py + embedder.py

//

- src/features/ingestion/ LIKE service.py (orchestrates pdf -> text -> chunks -> embeddings -> chroma) + schemas.py (request/ response models) + logic.py ( business logic) + errors.py (custom exceptions)

//
- src/api/ endpoints LIKe ingest.py + rag.py + chat.py

// 

- src/core/ LIKE chunking.py + utils.py
----------------------------------------------------
# plan 1
1. Implement /ingest in AI-Service  // pipeline //  pdf -> text -> chunks -> embeddings -> chromaDB -> query -> retrieve -> LLM -> answer

2. Implement /upload in Backend  
3. Build frontend upload UI  
4. Integrate all components  
5. Add RAG search  
6. Add chat endpoint  


// MY STOR:

- (ingest) The Secretary "system: FASTAPI" -> receive files -> check -> if pdf -> well(async) wait(await) -> open the file and convert it to a flexible book inside the computer using (io.BytesIO) -> hand it to the expert.
- (func extract_text_from_pdf) The Expert: read the book -> handed the book as a text to the secretary again
- The secretary print 500 char out of the received text -> handed a receipt to the customer (status, message, text_preview)
- (Chunk) The scissors -> ever pace size: 800 char -> overlap: 100