from datetime import datetime, timezone

from backend.agents.tool_planner import ToolPlanner
from backend.tools.executor import ToolExecutor


class ToolAgent:

    def __init__(self):

        self.planner = ToolPlanner()
        self.executor = ToolExecutor()

    def process(self, prompt):

        if not prompt:
            return None

        plan = self.planner.plan(prompt)

        if plan is None:
            return None

        result = self.executor.execute(
            plan["tool"],
            plan["input"]
        )

        result["reason"] = plan["reason"]
        result["confidence"] = plan["confidence"]

        self._log_result(result)

        return result

    def available_tools(self):

        return self.executor.list_tools()

    def _log_result(self, result):

        timestamp = datetime.now(
            timezone.utc
        ).isoformat()

        status = (
            "SUCCESS"
            if result["success"]
            else "FAILED"
        )

        print(
            f"[TOOL {status}] "
            f"{timestamp} | "
            f"{result['tool']} | "
            f"input={result['input']!r} | "
            f"output={result['output']!r} | "
            f"confidence={result.get('confidence')}"
        )