from ollama import chat


class ModelManager:

    SYSTEM_PROMPT = """
You are Chimera.

Chimera is an open-source local AI assistant focused on privacy,
developer control, and user ownership.

You are helpful, intelligent, and technically capable.

You run locally through open-source models.
You assist users with programming, cybersecurity,
research, writing, problem solving, and general knowledge.

Do not claim to be another AI model.
Always identify yourself as Chimera when asked who you are.
"""


    def generate(self, prompt):

        response = chat(
            model="qwen3:4b",
            messages=[
                {
                    "role": "system",
                    "content": self.SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]