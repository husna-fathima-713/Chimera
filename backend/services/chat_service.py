from backend.models.manager import ModelManager
from backend.services.chat_manager import ChatManager


class ChatService:

    def __init__(self):
        self.model_manager = ModelManager()
        self.chat_manager = ChatManager()

    def chat(self, chat_id, prompt):

        self.chat_manager.add_message(
            chat_id,
            "user",
            prompt
        )

        messages = self.chat_manager.get_messages(chat_id)

        response = self.model_manager.generate(messages)

        self.chat_manager.add_message(
            chat_id,
            "assistant",
            response
        )

        return response