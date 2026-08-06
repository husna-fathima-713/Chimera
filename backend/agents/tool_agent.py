import re

from backend.tools.registry import ToolRegistry


class ToolAgent:

    def __init__(self):

        self.registry = ToolRegistry()

    def process(self, prompt):

        prompt = prompt.strip()

        # ----------------------------
        # Calculator
        # ----------------------------

        expression = re.fullmatch(
            r"[0-9+\-*/().%\s]+",
            prompt
        )

        if expression:

            tool = self.registry.get("calculator")

            if tool:

                output = tool.execute(prompt)

                return {
                    "tool": "calculator",
                    "input": prompt,
                    "output": output
                }

        # ----------------------------
        # File Reader
        # ----------------------------

        file_match = re.search(
            r"(?:read|open|show)\s+(.+)",
            prompt,
            re.IGNORECASE
        )

        if file_match:

            filepath = file_match.group(1).strip()

            tool = self.registry.get("file_reader")

            if tool:

                output = tool.execute(filepath)

                return {
                    "tool": "file_reader",
                    "input": filepath,
                    "output": output
                }

        return None