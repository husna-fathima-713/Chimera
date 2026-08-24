from backend.tools.registry import ToolRegistry


class ToolExecutor:

    def __init__(self):

        self.registry = ToolRegistry()

    def execute(self, tool_name, tool_input):

        tool = self.registry.get(tool_name)

        if tool is None:

            return {
                "success": False,
                "tool": tool_name,
                "input": tool_input,
                "output": f"Unknown tool: {tool_name}"
            }

        if not tool_input:

            return {
                "success": False,
                "tool": tool_name,
                "input": "",
                "output": "Tool input is required."
            }

        try:

            result = tool.run(tool_input)

            return result

        except Exception as error:

            return {
                "success": False,
                "tool": tool_name,
                "input": tool_input,
                "output": f"Tool execution failed: {error}"
            }