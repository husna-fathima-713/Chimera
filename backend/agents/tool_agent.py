import re

from backend.tools.registry import ToolRegistry


class ToolAgent:

    def __init__(self):
        self.registry = ToolRegistry()

    def process(self, prompt):

        match = re.search(
            r"TOOL:\s*(\w+)\s*INPUT:\s*(.+)",
            prompt,
            re.IGNORECASE | re.DOTALL
        )

        if not match:
            return None

        tool_name = match.group(1).strip()
        tool_input = match.group(2).strip()

        tool = self.registry.get(tool_name)

        if tool is None:
            return {
                "tool": tool_name,
                "input": tool_input,
                "output": f"Tool '{tool_name}' not found."
            }

        try:

            output = tool.run(tool_input)

            return {
                "tool": tool_name,
                "input": tool_input,
                "output": output
            }

        except Exception as e:

            return {
                "tool": tool_name,
                "input": tool_input,
                "output": f"Tool execution failed: {str(e)}"
            }