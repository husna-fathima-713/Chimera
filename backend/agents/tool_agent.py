import re
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

        # --------------------------------
        # Explicit TOOL / INPUT request
        # --------------------------------

        tool_request = self.parse_request(prompt)

        if tool_request:

            return self._execute(
                tool_request["tool"],
                tool_request["input"]
            )

        # --------------------------------
        # Natural-language tool planning
        # --------------------------------

        plan = self.planner.plan(prompt)

        if plan is None:
            return None

        tool_name = plan["tool"]

        tool_input = self._extract_input(
            prompt,
            tool_name
        )

        if not tool_input:
            return None

        return self._execute(
            tool_name,
            tool_input
        )

    def parse_request(self, prompt):

        tool_match = re.search(
            r"TOOL:\s*([a-zA-Z0-9_]+)",
            prompt,
            re.IGNORECASE
        )

        if not tool_match:
            return None

        input_match = re.search(
            r"INPUT:\s*(.*)",
            prompt,
            re.IGNORECASE | re.DOTALL
        )

        tool_name = tool_match.group(1).strip()

        tool_input = ""

        if input_match:
            tool_input = input_match.group(1).strip()

        return {
            "tool": tool_name,
            "input": tool_input
        }

    def _extract_input(self, prompt, tool_name):

        if tool_name == "calculator":

            expression = re.search(
                r"[\d\s+\-*/().%]+",
                prompt
            )

            if expression:
                return expression.group(0).strip()

        return prompt.strip()

    def _execute(self, tool_name, tool_input):

        result = self.executor.execute(
            tool_name,
            tool_input
        )

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
            f"output={result['output']!r}"
        )