from backend.models.manager import ModelManager
from backend.services.chat_manager import ChatManager
from backend.services.memory_service import MemoryService
from backend.services.memory_extractor import MemoryExtractor
from backend.rag.retriever import Retriever


class ChatService:

    def __init__(self):
        self.model = ModelManager()
        self.chat_manager = ChatManager()
        self.memory_service = MemoryService()
        self.memory_extractor = MemoryExtractor()
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

        extracted = self.memory_extractor.extract(prompt)

        for memory in extracted:
            self.memory_service.add_memory(memory)

        messages = self.chat_manager.get_messages(chat_id)

        context = self.retriever.search(prompt)

        memories = self.memory_service.get_memories()

        print("\n==========================")
        print("USER MEMORIES")
        print("==========================")

        for memory in memories:
            print(memory)

        print("\n==========================")
        print("RETRIEVED CHUNKS")
        print("==========================")

        for i, chunk in enumerate(context, start=1):

            print(f"\nChunk {i}")
            print(f"Source : {chunk['source']}")
            print(f"Chunk ID : {chunk['chunk_id']}\n")

            print(chunk["text"][:700])

            print("\n--------------------------")

        system_prompt = ""

        if memories:

            system_prompt += (
                "Known facts about the user:\n\n"
            )

            system_prompt += "\n".join(memories)

            system_prompt += "\n\n"

        if context:

            context_text = "\n\n".join(
                chunk["text"]
                for chunk in context
            )

            system_prompt += (
                "Answer using the following document context.\n\n"
                + context_text
            )

        if system_prompt:

            messages.insert(
                0,
                {
                    "role": "system",
                    "content": system_prompt
                }
            )

        def response_generator():

            full_response = ""

            for chunk in self.model.stream(messages):

                full_response += chunk

                yield chunk

            self.chat_manager.add_message(
                chat_id,
                "assistant",
                full_response
            )

        return response_generator()