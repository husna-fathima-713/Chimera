from backend.tools.base import BaseTool


class CalculatorTool(BaseTool):

    name = "calculator"

    description = (
        "Evaluate simple mathematical expressions."
    )

    def execute(self, expression):

        allowed = (
            "0123456789"
            "+-*/(). %"
        )

        if any(
            char not in allowed
            for char in expression
        ):
            raise ValueError(
                "Invalid expression."
            )

        return str(
            eval(
                expression,
                {
                    "__builtins__": {}
                },
                {}
            )
        )