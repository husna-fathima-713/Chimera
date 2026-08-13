import re

from backend.tools.registry import ToolRegistry


class ToolAgent:

    def __init__(self):

        self.registry = ToolRegistry()

    def process(self, prompt):

        if not prompt:
            return None

        tool_match = re.search(
            r"TOOL:\s*([a-zA-Z0-9_]+)",
            prompt,
            re.IGNORECASE
        )

        input_match = re.search(
            r"INPUT:\s*(.*)",
            prompt,
            re.IGNORECASE | re.DOTALL
        )

        if not tool_match:
            return None

        tool_name = tool_match.group(1).strip()

        tool = self.registry.get(tool_name)

        if tool is None:

            return {
                "success": False,
                "tool": tool_name,
                "input": None,
                "output": f"Unknown tool: {tool_name}"
            }

        tool_input = ""

        if input_match:

            tool_input = input_match.group(1).strip()

        if not tool_input:

            return {
                "success": False,
                "tool": tool_name,
                "input": "",
                "output": "Tool input is required."
            }

        try:

            output = tool.run(tool_input)

            return {
                "success": True,
                "tool": tool_name,
                "input": tool_input,
                "output": output
            }

        except Exception as exc:

            return {
                "success": False,
                "tool": tool_name,
                "input": tool_input,
                "output": str(exc)
            }