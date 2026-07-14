import json
from pathlib import Path


class Memory:

    FILE_PATH = Path("backend/storage/memory.json")

    def __init__(self):
        self.history = []
        self.load()

    def load(self):
        if self.FILE_PATH.exists():
            with open(self.FILE_PATH, "r", encoding="utf-8") as file:
                self.history = json.load(file)

    def save(self):
        with open(self.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(
                self.history,
                file,
                indent=4,
                ensure_ascii=False
            )

    def add_message(self, role, content):
        self.history.append(
            {
                "role": role,
                "content": content
            }
        )
        self.save()

    def get_history(self):
        return self.history

    def clear(self):
        self.history = []
        self.save()