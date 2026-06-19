from fastapi import APIRouter, UploadFile, HTTPException
from src.infrastructure.storage.pdf import extract_text_from_pdf

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

    return {"status":"ok",
            "message": "PDF processed( text extracted)",
            "text_preview": text[:200]
            }