from backend.tools.executor import ToolExecutor


def test_valid_tool():

    executor = ToolExecutor()

    result = executor.execute(
        "calculator",
        "10 + 5"
    )

    assert result["success"] is True
    assert result["tool"] == "calculator"
    assert result["input"] == "10 + 5"
    assert result["output"] == "15"

    print("PASS: valid tool execution")


def test_unknown_tool():

    executor = ToolExecutor()

    result = executor.execute(
        "unknown_tool",
        "test"
    )

    assert result["success"] is False
    assert result["tool"] == "unknown_tool"

    print("PASS: unknown tool handling")


def test_missing_input():

    executor = ToolExecutor()

    result = executor.execute(
        "calculator",
        ""
    )

    assert result["success"] is False
    assert result["input"] == ""

    print("PASS: missing input handling")


def test_invalid_input():

    executor = ToolExecutor()

    result = executor.execute(
        "calculator",
        "hello"
    )

    assert result["success"] is False

    print("PASS: invalid input handling")


def run_tests():

    test_valid_tool()
    test_unknown_tool()
    test_missing_input()
    test_invalid_input()

    print("\nAll ToolExecutor tests passed.")


if __name__ == "__main__":
    run_tests()