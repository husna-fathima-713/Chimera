"""
Integration test for Chimera Finance Controller tools.

Verifies that finance tools are automatically discovered by the
ToolRegistry and execute correctly through ToolExecutor.
"""

from backend.tools.executor import ToolExecutor
from backend.tools.registry import ToolRegistry


EXPECTED_TOOLS = {
    "load_financial_batch",
    "reconcile_batch",
    "get_exceptions",
    "calculate_metrics",
}


def test_finance_tool_discovery():
    registry = ToolRegistry()

    discovered_tools = {
        tool["name"]
        for tool in registry.list_tools()
    }

    assert EXPECTED_TOOLS.issubset(discovered_tools)

    print("Finance tool discovery test passed.")


def test_finance_tool_execution():
    executor = ToolExecutor()

    load_result = executor.execute(
        "load_financial_batch",
        "load",
    )

    assert load_result["success"] is True

    reconcile_result = executor.execute(
        "reconcile_batch",
        "reconcile",
    )

    assert reconcile_result["success"] is True
    assert reconcile_result["output"]["records_processed"] == 101

    exceptions_result = executor.execute(
        "get_exceptions",
        "exceptions",
    )

    assert exceptions_result["success"] is True
    assert exceptions_result["output"]["count"] == 12

    metrics_result = executor.execute(
        "calculate_metrics",
        "metrics",
    )

    assert metrics_result["success"] is True
    assert metrics_result["output"]["matched"] == 89
    assert metrics_result["output"]["exceptions"] == 12
    assert metrics_result["output"]["match_rate"] == 88.12

    print("Finance tool execution test passed.")


if __name__ == "__main__":
    test_finance_tool_discovery()
    test_finance_tool_execution()
    print("All finance tool tests passed.")