from ollama import chat


class ModelManager:

    def __init__(self, model_name="qwen3:4b"):
        self.model_name = model_name

    def generate(self, messages):

        response = chat(
            model=self.model_name,
            messages=messages,
        )

        return response["message"]["content"]

    def stream(self, messages):

        stream = chat(
            model=self.model_name,
            messages=messages,
            stream=True,
        )

        for chunk in stream:

            if "message" in chunk:

                yield chunk["message"]["content"]