from backend.models.manager import ModelManager
from backend.services.chat_manager import ChatManager
from backend.rag.retriever import Retriever


class ChatService:

    def __init__(self):
        self.model = ModelManager()
        self.chat_manager = ChatManager()
        self.retriever = Retriever()

    def create_chat(self, title="New Chat"):
        return self.chat_manager.create_chat(title)

    def delete_chat(self, chat_id):
        self.chat_manager.delete_chat(chat_id)

    def index_document(self, filepath):
        self.retriever.index_document(filepath)

    def chat(self, chat_id, prompt):

        self.chat_manager.add_message(
            chat_id,
            "user",
            prompt
        )

        messages = self.chat_manager.get_messages(chat_id)

        context = self.retriever.search(prompt)

        if context:

            context_text = "\n\n".join(
                chunk["text"] for chunk in context
            )

            messages.insert(
                0,
                {
                    "role": "system",
                    "content":
                        "Answer ONLY using the following context.\n\n"
                        + context_text
                }
            )

        response = self.model.generate(messages)

        self.chat_manager.add_message(
            chat_id,
            "assistant",
            response
        )

        return response