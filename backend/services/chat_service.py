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

        self.chat_manager.add_message(
            chat_id,
            "user",
            prompt
        )

        messages = self.chat_manager.get_messages(chat_id)

        context = self.retriever.search(prompt)

        print("\n==========================")
        print("RETRIEVED CHUNKS")
        print("==========================")

        for i, chunk in enumerate(context, start=1):

            print(f"\nChunk {i}")
            print(f"Source : {chunk['source']}")
            print(f"Chunk ID : {chunk['chunk_id']}")
            print()

            print(chunk["text"][:700])

            print("\n--------------------------")

        if context:

            context_text = ""

            for chunk in context:

                context_text += (
                    f"Source: {chunk['source']}\n"
                    f"Chunk: {chunk['chunk_id']}\n"
                    f"{chunk['text']}\n\n"
                )

            messages.insert(
                0,
                {
                    "role": "system",
                    "content":
                        "Answer ONLY using the document context below.\n\n"
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