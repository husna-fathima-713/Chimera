from backend.models.manager import ModelManager


class ChatService:

    def __init__(self):
        self.model_manager = ModelManager()

    def chat(self, prompt: str):
        return self.model_manager.generate(prompt)