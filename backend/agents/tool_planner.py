from backend.agents.tool_selector import ToolSelector


class ToolPlanner:

    def __init__(self):

        self.selector = ToolSelector()

    def plan(self, prompt):

        if not prompt:
            return None

        prompt_lower = prompt.lower()

        tools = self.selector.available_tools()

        for tool in tools:

            name = tool["name"].lower()
            description = tool["description"].lower()

            if name in prompt_lower:
                return {
                    "tool": tool["name"],
                    "reason": "Tool name mentioned in request."
                }

            if (
                name == "calculator"
                and any(
                    operator in prompt
                    for operator in ["+", "-", "*", "/", "%"]
                )
            ):
                return {
                    "tool": tool["name"],
                    "reason": "Mathematical expression detected."
                }

        return None