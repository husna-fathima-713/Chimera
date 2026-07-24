from ollama import chat

from backend.config import MODEL_NAME


class ModelManager:

    SYSTEM_PROMPT = (
        "You are Chimera, an open-source AI assistant that runs locally. "
        "You help with programming, cybersecurity, blockchain, IoT, "
        "research, and technical tasks. "
        "Always introduce yourself as Chimera.\n\n"
        "When DOCUMENT CONTEXT is provided, answer ONLY from that context. "
        "If the answer is not present in the document, clearly say "
        "'I could not find that information in the uploaded document.' "
        "Do not make up information."
    )

    def __init__(self):
        self.model_name = MODEL_NAME

    def current_model(self):
        return self.model_name

    def generate(self, messages, context=None):

        prompt = self.SYSTEM_PROMPT

        if context:
            prompt += (
                "\n\nDOCUMENT CONTEXT:\n"
                f"{context}"
            )

        response = chat(
            model=self.model_name,
            messages=[
                {
                    "role": "system",
                    "content": prompt,
                }
            ] + messages,
            stream=False,
        )

        return response.message.content