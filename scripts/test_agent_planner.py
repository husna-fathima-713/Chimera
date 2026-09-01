from backend.agents.agent_planner import AgentPlanner
from backend.tools.registry import ToolRegistry


def test_calculator_planning():

    planner = AgentPlanner()
    registry = ToolRegistry()

    result = planner.plan(
        "Calculate 25 + 15",
        registry.list_tools()
    )

    assert result is not None
    assert result["tool"] == "calculator"
    assert result["input"] is not None

    print("PASS: calculator planning")
    print(f"Result: {result}")


def test_no_tool_planning():

    planner = AgentPlanner()
    registry = ToolRegistry()

    result = planner.plan(
        "Explain what blockchain is.",
        registry.list_tools()
    )

    assert result is not None
    assert result["tool"] is None
    assert result["input"] is None

    print("PASS: no-tool planning")


def run_tests():

    test_calculator_planning()
    test_no_tool_planning()

    print("\nAll AgentPlanner tests passed.")


if __name__ == "__main__":
    run_tests()