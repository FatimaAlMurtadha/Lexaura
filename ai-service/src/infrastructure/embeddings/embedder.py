import hashlib
import re
from typing import List

try:
    from sentence_transformers import SentenceTransformer
except Exception:  # pragma: no cover - defensive fallback for local/dev environments
    SentenceTransformer = None


class EmbeddingModel:
    _model = None

    @classmethod
    def load_model(cls):
        if cls._model is None:
            try:
                if SentenceTransformer is None:
                    raise ImportError("sentence_transformers is not available")
                cls._model = SentenceTransformer("all-MiniLM-l6-v2")
            except Exception:
                cls._model = None
        return cls._model

    @staticmethod
    def _fallback_embedding(text: str, dimensions: int = 32) -> List[float]:
        tokens = re.findall(r"\w+", text.lower())
        if not tokens:
            return [0.0] * dimensions

        vector = [0.0] * dimensions
        for token in tokens:
            index = int(hashlib.sha256(token.encode("utf-8")).hexdigest(), 16) % dimensions
            vector[index] += 1.0 / len(tokens)
        return [round(value, 6) for value in vector]

    @classmethod
    def embed(cls, texts: List[str]) -> List[List[float]]:
        model = cls.load_model()
        if model is None:
            return [cls._fallback_embedding(text) for text in texts]

        return model.encode(texts, convert_to_numpy=True).tolist()