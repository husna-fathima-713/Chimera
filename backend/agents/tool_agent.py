from backend.tools.registry import ToolRegistry


class ToolAgent:

    def __init__(self):

        self.registry = ToolRegistry()

    def process(self, prompt):

        for tool in self.registry.get_all():

            if tool.can_handle(prompt):

                input_data = tool.prepare_input(
                    prompt
                )

                output = tool.execute(
                    input_data
                )

                return {

                    "tool": tool.name,

                    "input": input_data,

                    "output": output

                }

        return None