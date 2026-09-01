import json

from backend.models.manager import ModelManager


class AgentPlanner:

    def __init__(self):

        self.model = ModelManager()

    def plan(self, prompt, tools, history=None):

        history = history or []

        tool_descriptions = []

        for tool in tools:

            tool_descriptions.append(
                {
                    "name": tool["name"],
                    "description": tool["description"]
                }
            )

        system_prompt = (
            "You are Chimera's tool planning component.\n\n"
            "Decide whether a tool is required to answer "
            "the user's request.\n\n"
            "If a tool is required, return ONLY valid JSON "
            "using this format:\n"
            '{"tool": "tool_name", "input": "tool_input"}\n\n'
            "If no tool is required, return ONLY:\n"
            '{"tool": null, "input": null}\n\n'
            "Available tools:\n"
            f"{json.dumps(tool_descriptions)}"
        )

        messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

        messages.extend(history)

        messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        response = ""

        for chunk in self.model.stream(
            messages
        ):

            response += chunk

        return self._parse_response(
            response
        )

    def _parse_response(self, response):

        try:

            data = json.loads(
                response.strip()
            )

        except json.JSONDecodeError:

            return None

        if not isinstance(data, dict):

            return None

        if "tool" not in data:

            return None

        if data["tool"] is None:

            return {
                "tool": None,
                "input": None
            }

        return {
            "tool": data["tool"],
            "input": data.get(
                "input",
                ""
            )
        }