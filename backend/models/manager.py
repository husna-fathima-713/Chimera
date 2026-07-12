from ollama import chat

from backend.config import MODEL_NAME


class ModelManager:
    def __init__(self):
        self.model_name = MODEL_NAME

    def current_model(self):
        return self.model_name

    def generate(self, prompt: str) -> str:
        response = chat(
            model=self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.message.content