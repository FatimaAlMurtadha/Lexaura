from sentence_transformers import SentenceTransformer
from typing import List

# chunks -> embeddings

class EmbeddingModel:
    _model = None

    @classmethod
    def load_model(cls):
        if cls._model is None:
            cls._model = SentenceTransformer("all-MiniLM-l6-v2") # a library that has a dictionary 
        return cls._model
    
    @classmethod
    def embed(cls, texts: List[str]) -> List[List[float]]:
        model = cls.load_model()
        return model.encode(texts, convert_to_numpy=True).tolist()