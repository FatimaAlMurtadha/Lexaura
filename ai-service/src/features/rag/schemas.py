from pydantic import BaseModel
from typing import List

# request / response

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str
    context_chunks: List[str]    