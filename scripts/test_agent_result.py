from backend.agents.agent_result import AgentResult


def test_agent_result():

    result = AgentResult(
        success=True,
        tool="calculator",
        input="10 + 5",
        output="15",
        reason="Mathematical expression detected.",
        confidence=0.9
    )

    data = result.to_dict()

    assert data["success"] is True
    assert data["tool"] == "calculator"
    assert data["input"] == "10 + 5"
    assert data["output"] == "15"
    assert data["reason"] == "Mathematical expression detected."
    assert data["confidence"] == 0.9

    print("PASS: agent result serialization")


if __name__ == "__main__":

    test_agent_result()

    print("\nAll AgentResult tests passed.")