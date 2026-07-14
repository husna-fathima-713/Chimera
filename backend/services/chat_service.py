from backend.models.manager import ModelManager
from backend.memory import Memory


class ChatService:

    def __init__(self):
        self.model_manager = ModelManager()
        self.memory = Memory()

    def chat(self, prompt):

        self.memory.add_message("user", prompt)

        messages = self.memory.get_history()

        response = self.model_manager.generate(messages)

        self.memory.add_message("assistant", response)

        return response