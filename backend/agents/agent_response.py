from dataclasses import dataclass


@dataclass
class AgentResponse:

    tool_called: bool
    tool_name: str | None = None
    tool_input: str | None = None
    tool_output: str | None = None