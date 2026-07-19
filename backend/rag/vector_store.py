import faiss
import numpy as np


class VectorStore:

    def __init__(self, dimension=384):
        self.index = faiss.IndexFlatL2(dimension)
        self.documents = []

    def add(self, embeddings, chunks):
        vectors = np.array(embeddings).astype("float32")

        self.index.add(vectors)

        self.documents.extend(chunks)

    def search(self, embedding, k=3):
        vector = np.array([embedding]).astype("float32")

        distances, indices = self.index.search(vector, k)

        results = []

        for idx in indices[0]:
            if idx < len(self.documents):
                results.append(self.documents[idx])

        return results