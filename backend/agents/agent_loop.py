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

        for iteration in range(
            self.MAX_ITERATIONS
        ):

            result = self.tool_agent.process(
                current_prompt
            )

            if result is None:
                break

            results.append(result)

            if not result.success:
                break

            current_prompt = self._build_next_prompt(
                prompt,
                results
            )

        return results

    def _build_next_prompt(
        self,
        original_prompt,
        results
    ):

        latest = results[-1]

        return (
            f"{original_prompt}\n\n"
            f"Previous tool result:\n"
            f"Tool: {latest.tool}\n"
            f"Input: {latest.input}\n"
            f"Output: {latest.output}\n\n"
            "Determine whether another tool "
            "execution is required."
        )