from backend.finance.data_generator import generate_financial_data
from backend.finance.metrics import calculate_metrics
from backend.finance.reconciliation_engine import reconcile_financial_data


def test_finance_engine():

    data = generate_financial_data()

    results = reconcile_financial_data(data)

    metrics = calculate_metrics(
        data,
        results,
    )

    assert metrics["records_received"] == 101
    assert metrics["records_processed"] == 101
    assert metrics["matched"] == 88
    assert metrics["exceptions"] == 13
    assert metrics["match_rate"] == 87.13

    duplicate_results = [
        result
        for result in results
        if "DUPLICATE_TRANSACTION" in result["issues"]
    ]

    assert len(duplicate_results) == 2

    unknown_results = [
        result
        for result in results
        if "UNKNOWN_TRANSACTION" in result["issues"]
    ]

    assert len(unknown_results) == 1

    print("Finance reconciliation engine test passed.")
    print()
    print("Records received  :", metrics["records_received"])
    print("Records processed :", metrics["records_processed"])
    print("Matched           :", metrics["matched"])
    print("Exceptions        :", metrics["exceptions"])
    print("Match rate        :", metrics["match_rate"])
    print()
    print("Duplicate records :", len(duplicate_results))
    print("Unknown records   :", len(unknown_results))


if __name__ == "__main__":
    test_finance_engine()