import json
from pathlib import Path

from backend.models.chat import ChatSession


class ChatManager:

    STORAGE_PATH = Path("backend/storage/chats")

    def __init__(self):
        self.STORAGE_PATH.mkdir(parents=True, exist_ok=True)

    def create_chat(self, title="New Chat"):
        chat = ChatSession(title)

        file_path = self.STORAGE_PATH / f"{chat.id}.json"

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(
                {
                    "chat": chat.to_dict(),
                    "messages": []
                },
                file,
                indent=4,
            )

        return chat

    def list_chats(self):
        chats = []

        for file in self.STORAGE_PATH.glob("*.json"):
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)
                chats.append(data["chat"])

        return chats

    def load_chat(self, chat_id):
        file_path = self.STORAGE_PATH / f"{chat_id}.json"

        if not file_path.exists():
            return None

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)