import pickle
from pathlib import Path

import faiss
import numpy as np


class MemoryVectorStore:

    STORAGE_PATH = Path("backend/storage/memory_db")

    INDEX_FILE = STORAGE_PATH / "memory.faiss"

    MEMORY_FILE = STORAGE_PATH / "memories.pkl"

    def __init__(self, dimension=384):

        self.STORAGE_PATH.mkdir(
            parents=True,
            exist_ok=True
        )

        self.dimension = dimension

        self.memories = []

        if self.INDEX_FILE.exists():

            self.index = faiss.read_index(
                str(self.INDEX_FILE)
            )

            with open(
                self.MEMORY_FILE,
                "rb"
            ) as file:

                self.memories = pickle.load(file)

        else:

            self.index = faiss.IndexFlatL2(
                dimension
            )

    def add(self, embedding, memory):

        vector = np.array(
            [embedding]
        ).astype("float32")

        self.index.add(vector)

        self.memories.append(memory)

        self.save()

    def search(self, embedding, k=5):

        if self.index.ntotal == 0:

            return []

        vector = np.array(
            [embedding]
        ).astype("float32")

        distances, indices = self.index.search(
            vector,
            min(k, self.index.ntotal)
        )

        results = []

        for idx in indices[0]:

            results.append(
                self.memories[idx]
            )

        return results

    def save(self):

        faiss.write_index(
            self.index,
            str(self.INDEX_FILE)
        )

        with open(
            self.MEMORY_FILE,
            "wb"
        ) as file:

            pickle.dump(
                self.memories,
                file
            )