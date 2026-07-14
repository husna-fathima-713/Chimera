from ollama import chat

from backend.config import MODEL_NAME


class ModelManager:

    SYSTEM_PROMPT = (
        "You are Chimera, an open-source AI assistant that runs locally. "
        "You help with programming, cybersecurity, blockchain, IoT, "
        "research, and technical tasks. "
        "Always introduce yourself as Chimera."
    )

    def __init__(self):
        self.model_name = MODEL_NAME

    def current_model(self):
        return self.model_name

    def generate(self, messages):
        response = chat(
            model=self.model_name,
            messages=[
                {
                    "role": "system",
                    "content": self.SYSTEM_PROMPT,
                }
            ] + messages,
            stream=False,
        )

        return response.message.content