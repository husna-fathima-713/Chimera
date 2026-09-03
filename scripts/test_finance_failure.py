"""
Failure-recovery test for the Chimera Finance Controller.

Verifies that malformed financial records become controlled
exceptions instead of crashing the reconciliation pipeline.
"""

from backend.finance.data_generator import generate_financial_data
from backend.finance.reconciliation_engine import reconcile_financial_data


def test_malformed_transaction():

    data = generate_financial_data()

    # Inject malformed financial data.
    data["transactions"][90]["amount"] = "N/A"

    results = reconcile_financial_data(data)

    result = next(
        item
        for item in results
        if item["transaction_id"] == "TXN-0091"
    )

    assert result["status"] == "EXCEPTION"

    assert (
        "MALFORMED_TRANSACTION_AMOUNT"
        in result["issues"]
    )

    assert result["transaction_amount"] is None

    print("Malformed transaction handled safely.")


def test_malformed_settlement():

    data = generate_financial_data()

    # Inject malformed settlement data.
    data["settlements"][94]["settlement_amount"] = "INVALID"

    results = reconcile_financial_data(data)

    result = next(
        item
        for item in results
        if item["transaction_id"] == "TXN-0095"
    )

    assert result["status"] == "EXCEPTION"

    assert (
        "MALFORMED_SETTLEMENT_AMOUNT"
        in result["issues"]
    )

    print("Malformed settlement handled safely.")


if __name__ == "__main__":

    test_malformed_transaction()
    test_malformed_settlement()

    print("All finance failure-recovery tests passed.")