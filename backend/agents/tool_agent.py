import re

from backend.tools.registry import ToolRegistry


class ToolAgent:

    def __init__(self):

        self.registry = ToolRegistry()

    def process(self, prompt):

        expression = re.search(
            r"(\d+[\+\-\*/]\d+)",
            prompt.replace(" ", "")
        )

        if not expression:
            return None

        tool = self.registry.get("calculator")

        if tool is None:
            return None

        output = tool.run(expression.group(1))

        return {
            "tool": tool.name,
            "input": expression.group(1),
            "output": output
        }