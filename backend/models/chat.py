from uuid import uuid4


class ChatSession:

    def __init__(self):
        self.id = str(uuid4())
        self.title = "New Chat"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title
        }