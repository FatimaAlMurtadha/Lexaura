from fastapi import APIRouter

router = APIRouter()

@router.post("/ingest")
async def ingest_pdf():
    return {"status": "ok", "message": "ingest endpoint is working! heeeej"}