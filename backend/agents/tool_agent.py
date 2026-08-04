import re

from backend.tools.registry import ToolRegistry


class ToolAgent:

    def __init__(self):
        self.registry = ToolRegistry()

    def process(self, prompt: str):

        prompt = prompt.strip()

        if re.fullmatch(r"[0-9+\-*/().\s]+", prompt):

            calculator = self.registry.get_tool("calculator")

            if calculator:

                try:

                    result = calculator.execute(prompt)

                    return {
                        "tool": "calculator",
                        "input": prompt,
                        "output": str(result)
                    }

                except Exception as e:

                    return {
                        "tool": "calculator",
                        "input": prompt,
                        "output": f"Error: {e}"
                    }

        return None