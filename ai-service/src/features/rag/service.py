from typing import List
from src.infrastructure.vectorstore.store import VectorStore
from src.infrastructure.llm.ollama_client import generate_answer

def build_prompt(question: str, context_chunks: List[str]) -> str:
    context = "\n\n".join(context_chunks)
    return
f"""You are an AI assistant.

Use ONLY the following context to answer the question.

context:
{context}

Question:
{question}
Answer in clear, concise English (or the user's language if obvious)
"""

def rag_query(question:str, top_k:int = 5) -> (str, List[str]):
    # convert question into embedding
    question_embedding = EmbeddingModel.embed([question]) [0]

    # search on ChromaDB
    store = VectorStore(collection_name="documents")
    result = store.query(query_embedding=question_embedding, top_k=top_k)

    # extract the best chunks
    context_chunks : List[str] = result.get("documents", [[]] [0])

    # build prompt and send llm
    prompt = build_prompt(question, context_chunks)
    answer = generate_answer(prompt)

    return answer, context_chunks