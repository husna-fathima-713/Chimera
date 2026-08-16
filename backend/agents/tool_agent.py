import re
from datetime import datetime, timezone

from backend.tools.registry import ToolRegistry


class ToolAgent:

    def __init__(self):

        self.registry = ToolRegistry()

    def process(self, prompt):

        if not prompt:
            return None

        tool_match = re.search(
            r"TOOL:\s*([a-zA-Z0-9_]+)",
            prompt,
            re.IGNORECASE
        )

        input_match = re.search(
            r"INPUT:\s*(.*)",
            prompt,
            re.IGNORECASE | re.DOTALL
        )

        if not tool_match:
            return None

        tool_name = tool_match.group(1).strip()

        if not self.registry.has(tool_name):

            result = {
                "success": False,
                "tool": tool_name,
                "input": None,
                "output": f"Unknown tool: {tool_name}"
            }

            self._log_result(result)

            return result

        tool = self.registry.get(tool_name)

        tool_input = ""

        if input_match:
            tool_input = input_match.group(1).strip()

        if not tool_input:

            result = {
                "success": False,
                "tool": tool_name,
                "input": "",
                "output": "Tool input is required."
            }

            self._log_result(result)

            return result

        result = tool.run(tool_input)

        self._log_result(result)

        return result

    def _log_result(self, result):

        timestamp = datetime.now(
            timezone.utc
        ).isoformat()

        status = "SUCCESS" if result["success"] else "FAILED"

        print(
            f"[TOOL {status}] "
            f"{timestamp} | "
            f"{result['tool']} | "
            f"input={result['input']!r} | "
            f"output={result['output']!r}"
        )