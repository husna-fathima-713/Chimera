from backend.models.manager import ModelManager
from backend.services.chat_manager import ChatManager
from backend.services.memory_manager import MemoryManager
from backend.rag.retriever import Retriever
from backend.tools.registry import ToolRegistry
from backend.agents.tool_agent import ToolAgent
from backend.agents.parser import ToolParser


class ChatService:

    def __init__(self):

        self.model = ModelManager()
        self.chat_manager = ChatManager()
        self.memory_manager = MemoryManager()
        self.retriever = Retriever()

        self.tool_registry = ToolRegistry()
        self.tool_agent = ToolAgent()
        self.tool_parser = ToolParser()

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

        memories = self.memory_manager.retrieve(
            prompt,
            k=5
        )

        context = self.retriever.search(prompt)

        system_prompt = ""

        if memories:

            system_prompt += "Known facts about the user:\n\n"

            system_prompt += "\n".join(memories)

            system_prompt += "\n\n"

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

        tools = self.tool_registry.list_tools()

        if tools:

            system_prompt += (
                "You may use tools when necessary.\n\n"
                "If a tool is required, respond ONLY in this format:\n\n"
                "TOOL: tool_name\n"
                "INPUT: tool_input\n\n"
                "Do not include any explanation.\n\n"
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