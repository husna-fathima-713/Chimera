from backend.agents.agent_planner import AgentPlanner
from backend.agents.agent_result import AgentResult
from backend.tools.executor import ToolExecutor


class AgentLoop:

    MAX_ITERATIONS = 4

    def __init__(self):

        self.planner = AgentPlanner()
        self.executor = ToolExecutor()

    def run(self, prompt):

        if not prompt:
            return []

        results = []
        history = []

        for _ in range(self.MAX_ITERATIONS):

            plan = self.planner.plan(
                prompt,
                self.executor.list_tools(),
                history
            )

            if plan is None:
                break

            if plan["tool"] is None:
                break

            result = self.executor.execute(
                plan["tool"],
                plan["input"]
            )

            agent_result = AgentResult(
                success=result["success"],
                tool=result["tool"],
                input=result["input"],
                output=result["output"],
                reason="LLM-selected tool execution.",
                confidence=1.0
            )

            results.append(agent_result)

            history.append(
                {
                    "role": "assistant",
                    "content": (
                        f"Tool: {agent_result.tool}\n"
                        f"Input: {agent_result.input}\n"
                        f"Output: {agent_result.output}"
                    )
                }
            )

            if not agent_result.success:
                break

        return results