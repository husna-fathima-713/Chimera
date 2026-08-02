import json
from pathlib import Path

from backend.models.manager import ModelManager
from backend.rag.embeddings import EmbeddingModel
from backend.services.memory_vector_store import MemoryVectorStore


class MemoryManager:

    STORAGE_PATH = Path("backend/storage")
    MEMORY_FILE = STORAGE_PATH / "user_memory.json"

    def __init__(self):

        self.model = ModelManager()
        self.embedder = EmbeddingModel()
        self.vector_store = MemoryVectorStore()

        self.STORAGE_PATH.mkdir(
            parents=True,
            exist_ok=True
        )

        if not self.MEMORY_FILE.exists():

            with open(
                self.MEMORY_FILE,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump([], file, indent=4)

    def load(self):

        with open(
            self.MEMORY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    def save(self, memories):

        with open(
            self.MEMORY_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                memories,
                file,
                indent=4
            )

    def remember(self, prompt):

        extraction_prompt = [

            {
                "role": "system",
                "content":
                (
                    "Extract ONE long-term user fact.\n"
                    "Return ONLY the fact.\n"
                    "If nothing should be remembered return NONE."
                )
            },

            {
                "role": "user",
                "content": prompt
            }

        ]

        fact = self.model.generate(
            extraction_prompt
        ).strip()

        if fact.upper() == "NONE":
            return

        memories = self.load()

        if fact not in memories:

            memories.append(fact)

            self.save(memories)

            embedding = self.embedder.encode(fact)

            self.vector_store.add(
                embedding,
                fact
            )

    def retrieve(self, query, k=5):

        embedding = self.embedder.encode(query)

        return self.vector_store.search(
            embedding,
            k
        )