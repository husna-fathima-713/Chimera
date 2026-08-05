import re

from backend.tools.registry import ToolRegistry


class ToolAgent:

    def __init__(self):
        self.registry = ToolRegistry()

    def process(self, prompt):

        expression = re.fullmatch(
            r"\s*([0-9+\-*/().%\s]+)\s*",
            prompt
        )

        if expression is None:
            return None

        tool = self.registry.get("calculator")

        if tool is None:
            return None

        output = tool.execute(
            expression.group(1)
        )

        return {
            "tool": "calculator",
            "input": expression.group(1),
            "output": output
        }