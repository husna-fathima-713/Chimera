class BaseTool:

    name = ""
    description = ""

    def can_handle(self, prompt):
        return False

    def prepare_input(self, prompt):
        return prompt

    def execute(self, tool_input):
        raise NotImplementedError(
            "Tool must implement execute()."
        )

    def run(self, prompt):
        tool_input = self.prepare_input(prompt)

        try:

            output = self.execute(tool_input)

            return {
                "success": True,
                "tool": self.name,
                "input": tool_input,
                "output": output
            }

        except Exception as e:

            return {
                "success": False,
                "tool": self.name,
                "input": tool_input,
                "output": str(e)
            }