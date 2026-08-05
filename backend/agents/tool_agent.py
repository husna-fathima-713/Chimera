from backend.tools.registry import ToolRegistry


class ToolAgent:

    def __init__(self):

        self.registry = ToolRegistry()

    def execute(self, tool_name, tool_input):

        tool = self.registry.get_tool(tool_name)

        if tool is None:

            return None

        return tool.run(tool_input)