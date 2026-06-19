

# text -> chunks
# business logic for chunking text into smaller pieces for embedding and storage in chromaDB
# chunking is important for handling large documents and ensuring that the LLM can process the information effectively
# the chunking strategy can be based on sentence boundaries, paragraph boundaries, or a fixed number of tokens/characters 

def chunk_text(text: str, chunk_size: int = 800, overlap: int = 100):
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]

        chunks.append(chunk.strip())
        start = end - overlap

    return chunks