from backend.tools.registry import ToolRegistry


class ToolAgent:

    def __init__(self):

        self.registry = ToolRegistry()

    def process(self, prompt):

        prompt = prompt.strip()

        tools = list(
            self.registry.tools.values()
        )

        matched_tools = []

        for tool in tools:

            try:

                if tool.can_handle(prompt):

                    matched_tools.append(tool)

            except Exception:

                continue

        if not matched_tools:

            return None

        tool = self._select_tool(
            prompt,
            matched_tools
        )

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

    def _select_tool(self, prompt, tools):

        prompt_lower = prompt.lower()

        # Prefer code search when the user
        # explicitly asks to search inside code.
        if any(
            phrase in prompt_lower
            for phrase in (
                "search code",
                "search inside",
                "inside the code",
                "find function",
                "find class",
                "find def"
            )
        ):

            for tool in tools:

                if tool.name == "code_search":

                    return tool

        # Prefer file search when the user
        # is looking for a filename.
        if any(
            phrase in prompt_lower
            for phrase in (
                "find file",
                "find filename",
                "locate file",
                "locate filename"
            )
        ):

            for tool in tools:

                if tool.name == "search":

                    return tool

        # Otherwise preserve registry order.
        return tools[0]