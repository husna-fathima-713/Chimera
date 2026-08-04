from backend.models.manager import ModelManager
from backend.services.chat_manager import ChatManager
from backend.services.memory_manager import MemoryManager
from backend.rag.retriever import Retriever
from backend.tools.registry import ToolRegistry
from backend.agents.tool_agent import ToolAgent


class ChatService:

    def __init__(self):
        self.model = ModelManager()
        self.chat_manager = ChatManager()
        self.memory_manager = MemoryManager()
        self.retriever = Retriever()
        self.tool_registry = ToolRegistry()
        self.tool_agent = ToolAgent()

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

        self.memory_manager.remember(prompt)

        messages = self.chat_manager.get_messages(chat_id)

        # ----------------------------
        # Tool Agent
        # ----------------------------

        tool_result = self.tool_agent.process(prompt)

        if tool_result:

            print("\n==========================")
            print("TOOL RESULT")
            print("==========================")
            print(tool_result)

        # ----------------------------
        # Memory
        # ----------------------------

        memories = self.memory_manager.retrieve(
            prompt,
            k=5
        )

        # ----------------------------
        # RAG
        # ----------------------------

        context = self.retriever.search(prompt)

        print("\n==========================")
        print("RELEVANT MEMORIES")
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

        # ----------------------------
        # Memories
        # ----------------------------

        if memories:

            system_prompt += "Known facts about the user:\n\n"
            system_prompt += "\n".join(memories)
            system_prompt += "\n\n"

        # ----------------------------
        # Retrieved Documents
        # ----------------------------

        if context:

            context_text = "\n\n".join(
                chunk["text"]
                for chunk in context
            )

            system_prompt += (
                "Use the following document context when answering.\n\n"
                + context_text
                + "\n\n"
            )

        # ----------------------------
        # Available Tools
        # ----------------------------

        tools = self.tool_registry.list_tools()

        if tools:

            system_prompt += (
                "You have access to the following tools.\n"
                "If one is useful, reply ONLY in this format:\n\n"
                "TOOL: tool_name\n"
                "INPUT: input\n\n"
                "Available tools:\n"
            )

            for tool in tools:

                system_prompt += (
                    f"- {tool['name']}: {tool['description']}\n"
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