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

        return tool.run(prompt)

    def _select_tool(self, prompt, tools):

        prompt_lower = prompt.lower()

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

        return tools[0]