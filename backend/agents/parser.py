import re

from backend.agents.agent_response import AgentResponse


class ToolParser:

    def parse(self, text):

        pattern = (
            r"TOOL:\s*(.*?)\n"
            r"INPUT:\s*(.*)"
        )

        match = re.search(
            pattern,
            text,
            re.DOTALL
        )

        if not match:

            return AgentResponse(
                tool_called=False
            )

        return AgentResponse(
            tool_called=True,
            tool_name=match.group(1).strip(),
            tool_input=match.group(2).strip()
        )