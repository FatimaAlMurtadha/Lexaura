from typing import List
from .client import get_chroma_client

class VectorStore:
    def __init__(self, collection_name: str):
        self.collection_name = collection_name
        client = get_chroma_client()

        self.collection = client.get_or_create_collection(
            name=self.collection_name,
            metadata={"hnsw:space": "cosine"}
        )

    def add(self, ids: List[str], embeddings: List[List[float]], chunks: List[str]):
        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=chunks
        )

    def query(self, query_embedding: List[float], top_k: int = 5):
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
