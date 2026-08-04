from backend.tools.calculator import CalculatorTool


class ToolRegistry:

    def __init__(self):

        self.tools = {}

        self.register(
            CalculatorTool()
        )

    def register(self, tool):

        self.tools[tool.name] = tool

    def get(self, name):

        return self.tools.get(name)

    # Alias for future compatibility
    def get_tool(self, name):

        return self.get(name)

    def list_tools(self):

        return [

            {
                "name": tool.name,
                "description": tool.description
            }

            for tool in self.tools.values()

        ]