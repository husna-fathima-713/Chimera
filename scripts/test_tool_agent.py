from backend.agents.tool_agent import ToolAgent


def test_no_tool_request():

    agent = ToolAgent()

    result = agent.process(
        "Explain blockchain."
    )

    assert result is None

    print("PASS: no tool request")


def test_calculator_execution():

    agent = ToolAgent()

    result = agent.process(
        "Calculate 10 + 5"
    )

    assert result is not None
    assert result["success"] is True
    assert result["tool"] == "calculator"
    assert result["input"] == "10 + 5"
    assert result["output"] == "15"
    assert result["confidence"] == 0.9

    print("PASS: calculator execution")


def test_explicit_tool():

    agent = ToolAgent()

    result = agent.process(
        "calculator"
    )

    assert result is not None
    assert result["tool"] == "calculator"

    print("PASS: explicit tool detection")


def test_unknown_tool():

    agent = ToolAgent()

    result = agent.process(
        "Use does_not_exist tool"
    )

    assert result is not None
    assert result["success"] is False
    assert result["tool"] == "does_not_exist"

    print("PASS: unknown tool")


def run_tests():

    test_no_tool_request()
    test_calculator_execution()
    test_explicit_tool()
    test_unknown_tool()

    print("\nAll ToolAgent tests passed.")


if __name__ == "__main__":
    run_tests()