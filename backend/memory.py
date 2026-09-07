import json
from pathlib import Path


class Memory:

    FILE_PATH = Path("backend/storage/memory.json")

    def __init__(self):
        self.memory = {}
        self.load()

    def load(self):

        if not self.FILE_PATH.exists():
            self.memory = {}
            return

        try:

            with open(
                self.FILE_PATH,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

            if isinstance(data, dict):
                self.memory = data

            elif isinstance(data, list):
                self.memory = {
                    "default": data
                }

            else:
                self.memory = {}

        except (
            json.JSONDecodeError,
            OSError
        ):

            self.memory = {}

    def save(self):

        self.FILE_PATH.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            self.FILE_PATH,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.memory,
                file,
                indent=4,
                ensure_ascii=False
            )

    def add_message(
        self,
        chat_id,
        role,
        content
    ):

        if chat_id not in self.memory:
            self.memory[chat_id] = []

        self.memory[chat_id].append(
            {
                "role": role,
                "content": content
            }
        )

        self.save()

    def get_history(self, chat_id):

        return self.memory.get(
            chat_id,
            []
        )

    def clear(self, chat_id):

        self.memory[chat_id] = []

        self.save()

    def clear_all(self):

        self.memory = {}

        self.save()