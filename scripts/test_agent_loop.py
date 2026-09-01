from backend.agents.agent_loop import AgentLoop


def test_no_tool():

    agent = AgentLoop()

    results = agent.run(
        "Explain blockchain."
    )

    assert results == []

    print("PASS: no-tool request")


def test_calculator():

    agent = AgentLoop()

    results = agent.run(
        "Calculate 10 + 5"
    )

    assert len(results) >= 1

    result = results[0]

    assert result.success is True
    assert result.tool == "calculator"
    assert result.input == "10 + 5"
    assert result.output == "15"

    print("PASS: calculator execution")


def test_explicit_calculator():

    agent = AgentLoop()

    results = agent.run(
        "Use calculator to calculate 20 + 5"
    )

    assert len(results) >= 1

    result = results[0]

    assert result.success is True
    assert result.tool == "calculator"
    assert result.input == "20 + 5"
    assert result.output == "25"

    print("PASS: explicit calculator")


def test_iteration_limit():

    agent = AgentLoop()

    assert agent.MAX_ITERATIONS == 3

    print("PASS: iteration limit")


def run_tests():

    test_no_tool()
    test_calculator()
    test_explicit_calculator()
    test_iteration_limit()

    print("\nAll AgentLoop tests passed.")


if __name__ == "__main__":
    run_tests()