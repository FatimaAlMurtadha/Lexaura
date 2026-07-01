from fastapi import APIRouter
from src.features.rag.schemas import QueryRequest, QueryResponse
from src.features.rag.service import rag_query

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
async def query_rag(request: QueryRequest):
    answer, context_chunks = rag_query(request.question)
    return QueryResponse(
        answer=answer,
        context_chunks=context_chunks
    )