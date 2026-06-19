from fastapi import APIRouter, UploadFile, HTTPException
from src.infrastructure.storage.pdf import extract_text_from_pdf
from src.core.chunking import chunk_text
from src.infrastructure.embeddings.embedder import EmbeddingModel
from src.infrastructure.vectorstore.store import VectorStore

import io

router = APIRouter()

@router.post("/ingest")
async def ingest_pdf(file: UploadFile):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail= "Invalid file type")
    content = await file.read()
    pdf_bytes = io.BytesIO(content)

    text = extract_text_from_pdf(pdf_bytes)

    print("============ Extracted Text ==================")
    print(text[:500]) # show first 500 letters on the text

    chunks = chunk_text(text)
    print("===== Number of chunks: ", len(chunks))
    print("===== First chunk preview ===")
    print(chunks[0][:300])

    embeddings = EmbeddingModel.embed(chunks) # translate the chunks into vectors (embeddings)
    print("===== Number of shape: ")
    print(len(embeddings), "vectors")
    print("Vector size: ", len(embeddings[0]))

    store = VectorStore(collection_name="documents")
    ids = [f"chunk_{i}" for i in range(len(chunks))]
    store.add(ids=ids, embeddings=embeddings, chunks=chunks)
    print("===== Stored in ChromaDB ===")
    print("Total chunks:", len(chunks))

    return {"status":"ok",
            "message": "PDF processed( text extracted + chunked -> embeddings generated -> stored)",
            "chunks_count": len(chunks),
            "first_chunk_preview": chunks[0][:200],
            "embedding_dim": len(embeddings[0])
            }

