from backend.rag.loader import DocumentLoader
from backend.rag.chunker import TextChunker
from backend.rag.embeddings import EmbeddingModel
from backend.rag.vector_store import VectorStore

loader = DocumentLoader()
chunker = TextChunker()
embedder = EmbeddingModel()
store = VectorStore()

text = loader.load("README.md")

chunks = chunker.split(text)

embeddings = embedder.encode(chunks)

store.add(embeddings, chunks)

query = "What is Chimera?"

query_embedding = embedder.encode([query])[0]

results = store.search(query_embedding)

print(results[0])