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

    def index_document(self, filepath):
        self.retriever.index_document(filepath)

    def chat(self, chat_id, prompt):

        # Store user message
        self.chat_manager.add_message(
            chat_id,
            "user",
            prompt
        )

        # Get conversation history
        messages = self.chat_manager.get_messages(chat_id)

        # Retrieve relevant context
        context = self.retriever.search(prompt)

        # If context exists, inject it before the latest user message
        if context:

            messages.insert(
                -1,
                {
                    "role": "system",
                    "content": f"Relevant Context:\n\n{context}"
                }
            )

        # Generate response
        response = self.model.generate(messages)

        # Store assistant reply
        self.chat_manager.add_message(
            chat_id,
            "assistant",
            response
        )

        return response