"""
End-to-end test for the Chimera Finance Controller backend.
"""

from backend.finance.audit_logger import get_audit_records
from backend.finance.data_generator import generate_financial_data
from backend.finance.exception_analyzer import ExceptionAnalyzer
from backend.finance.metrics import calculate_metrics
from backend.finance.reconciliation_engine import reconcile_financial_data


def test_finance_e2e():

    # 1. Generate financial batch
    data = generate_financial_data()

    # 2. Reconcile deterministically
    results = reconcile_financial_data(data)

    # 3. Calculate deterministic metrics
    metrics = calculate_metrics(
        data,
        results,
    )

    assert metrics["records_processed"] == 101
    assert metrics["matched"] == 89
    assert metrics["exceptions"] == 12

    # 4. Select one detected exception
    exception = next(
        result
        for result in results
        if result["transaction_id"] == "TXN-0020"
    )

    assert exception["status"] == "EXCEPTION"

    # 5. LLM analyzes the already-detected exception
    analysis = ExceptionAnalyzer().analyze(
        exception
    )

    assert analysis["severity"] in {
        "LOW",
        "MEDIUM",
        "HIGH",
    }

    assert analysis["explanation"]
    assert analysis["recommended_action"]

    # 6. Verify audit infrastructure
    audit_records = get_audit_records()

    assert isinstance(audit_records, list)

    print("Finance E2E test passed.")
    print()
    print("Records processed :", metrics["records_processed"])
    print("Matched           :", metrics["matched"])
    print("Exceptions        :", metrics["exceptions"])
    print("Match rate        :", metrics["match_rate"])
    print()
    print("Sample exception  :", exception["transaction_id"])
    print("Severity          :", analysis["severity"])
    print("Explanation       :", analysis["explanation"])
    print("Action            :", analysis["recommended_action"])


if __name__ == "__main__":
    test_finance_e2e()