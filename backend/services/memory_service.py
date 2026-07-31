import json
from pathlib import Path


class MemoryService:

    STORAGE_PATH = Path("backend/storage")
    MEMORY_FILE = STORAGE_PATH / "user_memory.json"

    def __init__(self):

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

    def add_memory(self, fact):

        memories = self.load()

        if fact not in memories:

            memories.append(fact)

            self.save(memories)

    def get_memories(self):

        return self.load()