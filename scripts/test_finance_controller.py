from backend.finance.controller import run_finance_controller


def test_finance_controller():

    result = run_finance_controller()

    assert "metrics" in result
    assert "exceptions" in result

    assert result["metrics"]["records_processed"] == 101
    assert result["metrics"]["matched"] == 89
    assert result["metrics"]["exceptions"] == 12

    assert len(result["exceptions"]) == 12

    print("Finance controller test passed.")
    print()
    print("Records processed :", result["metrics"]["records_processed"])
    print("Matched           :", result["metrics"]["matched"])
    print("Exceptions        :", result["metrics"]["exceptions"])
    print("Match rate        :", result["metrics"]["match_rate"])


if __name__ == "__main__":
    test_finance_controller()