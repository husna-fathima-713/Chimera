from backend.agents.tool_selector import ToolSelector


class ToolPlanner:

    def __init__(self):

        self.selector = ToolSelector()

    def plan(self, prompt):

        if not prompt:
            return None

        prompt_lower = prompt.lower()

        tools = self.selector.available_tools()

        # Explicit calculator request
        if "calculator" in prompt_lower:

            calculator = self.selector.select(
                "calculator"
            )

            if calculator:

                calculation = self._extract_calculation(
                    prompt
                )

                if calculation:

                    return {
                        "tool": "calculator",
                        "input": calculation,
                        "reason": "Calculator tool explicitly requested.",
                        "confidence": 1.0
                    }

        # Natural calculation
        if self._looks_like_calculation(prompt):

            calculator = self.selector.select(
                "calculator"
            )

            if calculator:

                return {
                    "tool": "calculator",
                    "input": self._extract_calculation(prompt),
                    "reason": "Mathematical expression detected.",
                    "confidence": 0.9
                }

        return None

    def _looks_like_calculation(self, prompt):

        operators = (
            "+",
            "-",
            "*",
            "/",
            "%"
        )

        return (
            any(
                operator in prompt
                for operator in operators
            )
            and any(
                char.isdigit()
                for char in prompt
            )
        )

    def _extract_calculation(self, prompt):

        expression = ""

        for char in prompt:

            if (
                char.isdigit()
                or char in "+-*/().%"
                or char.isspace()
            ):

                expression += char

        return expression.strip()

    def available_tools(self):

        return self.selector.available_tools()