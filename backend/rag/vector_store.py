import pickle
from pathlib import Path

import faiss
import numpy as np


class VectorStore:

    STORAGE_PATH = Path("backend/storage/vector_db")
    INDEX_FILE = STORAGE_PATH / "index.faiss"
    DOCUMENTS_FILE = STORAGE_PATH / "documents.pkl"

    def __init__(self, dimension=384):

        self.dimension = dimension

        self.STORAGE_PATH.mkdir(parents=True, exist_ok=True)

        self.documents = []

        if (
            self.INDEX_FILE.exists()
            and self.DOCUMENTS_FILE.exists()
        ):

            self.index = faiss.read_index(str(self.INDEX_FILE))

            with open(self.DOCUMENTS_FILE, "rb") as file:
                self.documents = pickle.load(file)

        else:

            self.index = faiss.IndexFlatL2(self.dimension)

    def add(self, embeddings, chunks):

        vectors = np.array(embeddings, dtype=np.float32)

        self.index.add(vectors)

        self.documents.extend(chunks)

        self.save()

    def search(self, embedding, k=3):

        if self.index.ntotal == 0:
            return []

        k = min(k, self.index.ntotal)

        vector = np.array([embedding], dtype=np.float32)

        distances, indices = self.index.search(vector, k)

        results = []

        for idx in indices[0]:

            if idx == -1:
                continue

            if idx < len(self.documents):
                results.append(self.documents[idx])

        return results

    def save(self):

        faiss.write_index(
            self.index,
            str(self.INDEX_FILE),
        )

        with open(self.DOCUMENTS_FILE, "wb") as file:
            pickle.dump(
                self.documents,
                file,
            )