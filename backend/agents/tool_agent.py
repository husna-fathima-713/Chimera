from backend.tools.registry import ToolRegistry


class ToolAgent:

    def __init__(self):
        self.registry = ToolRegistry()

    def process(self, prompt):

        tool_name = None
        tool_input = None

        lines = prompt.strip().splitlines()

        for line in lines:

            if line.upper().startswith("TOOL:"):
                tool_name = line.split(":", 1)[1].strip()

            elif line.upper().startswith("INPUT:"):
                tool_input = line.split(":", 1)[1].strip()

        if not tool_name or tool_input is None:
            return None

        tool = self.registry.get(tool_name)

        if tool is None:

            return {
                "success": False,
                "tool": tool_name,
                "input": tool_input,
                "output": f"Tool '{tool_name}' not found."
            }

        try:

            output = tool.run(tool_input)

            return {
                "success": True,
                "tool": tool_name,
                "input": tool_input,
                "output": output
            }

        except Exception as e:

            return {
                "success": False,
                "tool": tool_name,
                "input": tool_input,
                "output": str(e)
            }