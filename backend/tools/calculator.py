import re

from backend.tools.base import BaseTool


class CalculatorTool(BaseTool):

    name = "calculator"

    description = "Evaluate simple mathematical expressions."

    def can_handle(self, prompt):

        return bool(

            re.fullmatch(
                r"[0-9+\-*/().%\s]+",
                prompt.strip()
            )

        )

    def execute(self, expression):

        allowed = (
            "0123456789"
            "+-*/(). %"
        )

        if any(
            c not in allowed
            for c in expression
        ):
            raise ValueError(
                "Invalid expression."
            )

        return str(

            eval(
                expression,
                {"__builtins__": {}},
                {}
            )

        )