from backend.tools.registry import ToolRegistry


class ToolSelector:

    def __init__(self):

        self.registry = ToolRegistry()

    def select(self, tool_name):

        if not tool_name:
            return None

        tool_name = tool_name.strip()

        if not self.registry.has(tool_name):
            return None

        return self.registry.get(tool_name)

    def available_tools(self):

        return self.registry.list_tools()