from backend.rag.loader import DocumentLoader
from backend.rag.chunker import TextChunker
from backend.rag.embeddings import EmbeddingModel

loader = DocumentLoader()
chunker = TextChunker()
embedder = EmbeddingModel()

text = loader.load("README.md")

chunks = chunker.split(text)

embeddings = embedder.encode(chunks)

print(f"Chunks: {len(chunks)}")
print(f"Embeddings: {len(embeddings)}")
print(f"Embedding Dimension: {len(embeddings[0])}")