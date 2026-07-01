from fastapi import FastAPI
from src.api.ingest import router as ingest_router
from src.api.rag import router as rag_router

app = FastAPI(title="Lexaura AI-Service")

app.include_router(ingest_router, prefix="/api")
app.include_router(rag_router, prefix="/api")

@app.get("/")
def health():
    return {"message": "AI Service is running!"}