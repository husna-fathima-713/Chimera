from backend.agents.tool_agent import ToolAgent


class AgentLoop:

    MAX_ITERATIONS = 3

    def __init__(self):

        self.tool_agent = ToolAgent()

    def run(self, prompt):

        if not prompt:
            return []

        results = []

        current_prompt = prompt

        for _ in range(self.MAX_ITERATIONS):

            result = self.tool_agent.process(
                current_prompt
            )

            if result is None:
                break

            results.append(result)

            if not result.success:
                break

            # The current tool architecture is
            # single-step. Stop after a successful
            # execution until multi-step planning
            # is implemented.
            break

        return results