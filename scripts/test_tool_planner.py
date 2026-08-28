from backend.agents.tool_planner import ToolPlanner


def test_calculator_detection():

    planner = ToolPlanner()

    result = planner.plan(
        "Calculate 25 * 4"
    )

    assert result is not None
    assert result["tool"] == "calculator"
    assert result["input"] == "25 * 4"
    assert result["confidence"] == 0.9

    print("PASS: calculator detection")


def test_explicit_tool():

    planner = ToolPlanner()

    result = planner.plan(
        "Use calculator to calculate 10 + 5"
    )

    assert result is not None
    assert result["tool"] == "calculator"
    assert result["confidence"] == 1.0

    print("PASS: explicit tool detection")


def test_no_tool():

    planner = ToolPlanner()

    result = planner.plan(
        "Explain blockchain."
    )

    assert result is None

    print("PASS: no-tool detection")


def test_available_tools():

    planner = ToolPlanner()

    tools = planner.available_tools()

    assert isinstance(tools, list)
    assert len(tools) > 0

    print("PASS: available tools")


def run_tests():

    test_calculator_detection()
    test_explicit_tool()
    test_no_tool()
    test_available_tools()

    print("\nAll ToolPlanner tests passed.")


if __name__ == "__main__":
    run_tests()