from uuid import uuid4


class ChatSession:

    def __init__(self, title="New Chat"):
        self.id = str(uuid4())
        self.title = title

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
        }