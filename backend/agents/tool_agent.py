import re

from backend.tools.registry import ToolRegistry


class ToolAgent:

    def __init__(self):

        self.registry = ToolRegistry()

    def process(self, prompt):

        tools = self.registry.tools.values()

        for tool in tools:

            if not tool.can_handle(prompt):

                continue

            tool_input = tool.prepare_input(prompt)

            try:

                output = tool.execute(tool_input)

            except Exception as e:

                output = f"Tool execution failed: {e}"

            return {
                "tool": tool.name,
                "input": tool_input,
                "output": output
            }

        return None