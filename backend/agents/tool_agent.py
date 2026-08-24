import re
from datetime import datetime, timezone

from backend.tools.executor import ToolExecutor


class ToolAgent:

    def __init__(self):

        self.executor = ToolExecutor()

    def process(self, prompt):

        if not prompt:
            return None

        tool_request = self.parse_request(prompt)

        if tool_request is None:
            return None

        tool_name = tool_request["tool"]
        tool_input = tool_request["input"]

        result = self.executor.execute(
            tool_name,
            tool_input
        )

        self._log_result(result)

        return result

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