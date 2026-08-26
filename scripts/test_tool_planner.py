from backend.agents.tool_planner import ToolPlanner


def test_calculator_detection():

    planner = ToolPlanner()

    result = planner.plan(
        "Calculate 25 * 4"
    )

    assert result is not None
    assert result["tool"] == "calculator"

    print("PASS: calculator detection")


def test_explicit_tool():

    planner = ToolPlanner()

    result = planner.plan(
        "Use calculator to calculate 10 + 5"
    )

    assert result is not None
    assert result["tool"] == "calculator"

    print("PASS: explicit tool detection")


def test_no_tool():

    planner = ToolPlanner()

    result = planner.plan(
        "Explain blockchain."
    )

    assert result is None

    print("PASS: no-tool detection")


def run_tests():

    test_calculator_detection()
    test_explicit_tool()
    test_no_tool()

    print("\nAll ToolPlanner tests passed.")


if __name__ == "__main__":
    run_tests()