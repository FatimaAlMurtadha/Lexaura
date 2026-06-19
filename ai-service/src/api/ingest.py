from fastapi import APIRouter, UploadFile, HTTPException
from src.infrastructure.storage.pdf import extract_text_from_pdf
from src.core.chunking import chunk_text

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

    return {"status":"ok",
            "message": "PDF processed( text extracted + chunked)",
            "chunks_count": len(chunks),
            "first_chunk_preview": chunks[0][:200]
            }

