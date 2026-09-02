"""
Integration test for the Chimera Finance Controller engine.

Tests the complete deterministic pipeline:

data generation
    ↓
reconciliation
    ↓
metrics
"""

from backend.finance.data_generator import generate_financial_data
from backend.finance.reconciliation_engine import reconcile_financial_data
from backend.finance.metrics import calculate_metrics


def test_finance_engine():
    data = generate_financial_data()

    results = reconcile_financial_data(data)

    metrics = calculate_metrics(
        data,
        results,
    )

    # Basic dataset validation
    assert len(data["transactions"]) == 101
    assert len(data["settlements"]) == 100
    assert len(data["invoices"]) == 100
    assert len(data["payouts"]) == 100

    # Reconciliation validation
    assert len(results) == 101

    assert metrics["records_received"] == 101
    assert metrics["records_processed"] == 101

    assert metrics["matched"] == 89
    assert metrics["exceptions"] == 12

    assert metrics["matched"] + metrics["exceptions"] == 101

    # Match rate validation
    expected_match_rate = round(
        (89 / 101) * 100,
        2,
    )

    assert metrics["match_rate"] == expected_match_rate

    # Financial value validation
    assert metrics["total_transaction_value"] == 206500.0
    assert metrics["reconciled_value"] == 177250.0
    assert metrics["exception_value"] == 29250.0

    # Failure handling validation
    malformed_transaction = next(
        result
        for result in results
        if result["transaction_id"] == "TXN-0091"
    )

    assert malformed_transaction["status"] == "EXCEPTION"

    assert (
        "MALFORMED_TRANSACTION_AMOUNT"
        in malformed_transaction["issues"]
    )

    print("Finance engine integration test passed.")


if __name__ == "__main__":
    test_finance_engine()