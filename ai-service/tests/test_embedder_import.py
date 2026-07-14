import importlib


def test_embedder_module_imports():
    module = importlib.import_module("src.infrastructure.embeddings.embedder")

    assert hasattr(module, "EmbeddingModel")


def test_embedder_falls_back_when_sentence_transformer_is_unavailable(monkeypatch):
    module = importlib.import_module("src.infrastructure.embeddings.embedder")
    monkeypatch.setattr(module, "SentenceTransformer", None)
    monkeypatch.setattr(module.EmbeddingModel, "_model", None)

    embeddings = module.EmbeddingModel.embed(["hello world"])

    assert len(embeddings) == 1
    assert len(embeddings[0]) == 32
    assert all(isinstance(value, float) for value in embeddings[0])
