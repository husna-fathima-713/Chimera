from backend.agents.tool_agent import ToolAgent


def test_no_tool_request():

    agent = ToolAgent()

    result = agent.process(
        "Hello Chimera"
    )

    assert result is None

    print("PASS: no tool request")


def test_calculator():

    agent = ToolAgent()

    result = agent.process(
        "TOOL: calculator\n"
        "INPUT: 10 + 5"
    )

    assert result is not None
    assert result["success"] is True
    assert result["tool"] == "calculator"
    assert result["input"] == "10 + 5"
    assert result["output"] == "15"

    print("PASS: calculator execution")


def test_unknown_tool():

    agent = ToolAgent()

    result = agent.process(
        "TOOL: does_not_exist\n"
        "INPUT: test"
    )

    assert result is not None
    assert result["success"] is False
    assert result["tool"] == "does_not_exist"

    print("PASS: unknown tool")


def test_missing_input():

    agent = ToolAgent()

    result = agent.process(
        "TOOL: calculator"
    )

    assert result is not None
    assert result["success"] is False
    assert result["tool"] == "calculator"
    assert result["input"] == ""

    print("PASS: missing input")


def test_invalid_calculation():

    agent = ToolAgent()

    result = agent.process(
        "TOOL: calculator\n"
        "INPUT: hello"
    )

    assert result is not None
    assert result["success"] is False

    print("PASS: invalid calculation")


def run_tests():

    test_no_tool_request()
    test_calculator()
    test_unknown_tool()
    test_missing_input()
    test_invalid_calculation()

    print("\nAll ToolAgent tests passed.")


if __name__ == "__main__":
    run_tests()