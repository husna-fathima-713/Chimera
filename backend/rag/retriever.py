from backend.rag.loader import DocumentLoader
from backend.rag.chunker import TextChunker
from backend.rag.embeddings import EmbeddingModel
from backend.rag.vector_store import VectorStore


class Retriever:

    def __init__(self):
        self.loader = DocumentLoader()
        self.chunker = TextChunker()
        self.embedder = EmbeddingModel()
        self.store = VectorStore()

    def index_document(self, filepath):
        text = self.loader.load(filepath)

        chunks = self.chunker.split(text)

        embeddings = self.embedder.encode(chunks)

        self.store.add(embeddings, chunks)

    def search(self, query, k=3):
        query_embedding = self.embedder.encode([query])[0]

        return self.store.search(query_embedding, k)