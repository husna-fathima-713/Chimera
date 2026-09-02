"""
Synthetic financial data generator for Chimera Finance Controller.

This module generates deterministic transaction, settlement, invoice,
and payout records with controlled anomalies for reconciliation testing.
"""

from __future__ import annotations

import random
from datetime import date, timedelta
from typing import Any


DEFAULT_SEED = 42
DEFAULT_RECORD_COUNT = 100


def generate_financial_data(
    record_count: int = DEFAULT_RECORD_COUNT,
    seed: int = DEFAULT_SEED,
) -> dict[str, list[dict[str, Any]]]:
    """
    Generate deterministic synthetic financial records.

    Args:
        record_count: Number of transaction records to generate.
        seed: Random seed for reproducible output.

    Returns:
        Dictionary containing transactions, settlements, invoices,
        and payouts.
    """

    if record_count < 1:
        raise ValueError("record_count must be at least 1")

    rng = random.Random(seed)

    transactions: list[dict[str, Any]] = []
    settlements: list[dict[str, Any]] = []
    invoices: list[dict[str, Any]] = []
    payouts: list[dict[str, Any]] = []

    start_date = date(2026, 8, 1)

    for index in range(1, record_count + 1):
        transaction_id = f"TXN-{index:04d}"

        amount = rng.choice(
            [
                500,
                750,
                1000,
                1250,
                1500,
                2000,
                2500,
                3000,
                3500,
                5000,
            ]
        )

        transaction_date = start_date + timedelta(
            days=rng.randint(0, 30)
        )

        customer_id = f"CUST-{rng.randint(1, 30):03d}"

        fee = round(amount * 0.02, 2)
        settlement_amount = round(amount - fee, 2)

        transactions.append(
            {
                "transaction_id": transaction_id,
                "customer_id": customer_id,
                "amount": amount,
                "currency": "INR",
                "transaction_date": transaction_date.isoformat(),
                "status": "SUCCESS",
            }
        )

        settlements.append(
            {
                "settlement_id": f"SET-{index:04d}",
                "transaction_id": transaction_id,
                "settlement_amount": settlement_amount,
                "fee": fee,
                "currency": "INR",
                "settlement_date": (
                    transaction_date + timedelta(days=1)
                ).isoformat(),
                "status": "SETTLED",
            }
        )

        invoices.append(
            {
                "invoice_id": f"INV-{index:04d}",
                "transaction_id": transaction_id,
                "invoice_amount": amount,
                "currency": "INR",
                "invoice_date": transaction_date.isoformat(),
                "status": "PAID",
            }
        )

        payouts.append(
            {
                "payout_id": f"PAY-{index:04d}",
                "transaction_id": transaction_id,
                "payout_amount": settlement_amount,
                "currency": "INR",
                "payout_date": (
                    transaction_date + timedelta(days=2)
                ).isoformat(),
                "status": "PROCESSED",
            }
        )

    _inject_anomalies(
        transactions=transactions,
        settlements=settlements,
        invoices=invoices,
        payouts=payouts,
    )

    return {
        "transactions": transactions,
        "settlements": settlements,
        "invoices": invoices,
        "payouts": payouts,
    }


def _inject_anomalies(
    transactions: list[dict[str, Any]],
    settlements: list[dict[str, Any]],
    invoices: list[dict[str, Any]],
    payouts: list[dict[str, Any]],
) -> None:
    """
    Inject controlled anomalies into the generated dataset.

    The anomaly positions are deterministic because the source dataset
    itself is generated deterministically.
    """

    # 1. Amount mismatch
    settlements[9]["settlement_amount"] += 400

    # 2. Missing settlement
    settlements[19]["status"] = "MISSING"

    # 3. Duplicate transaction
    duplicate_transaction = transactions[29].copy()
    duplicate_transaction["transaction_id"] = "TXN-DUP-0030"
    transactions.append(duplicate_transaction)

    # 4. Delayed settlement
    settlements[39]["settlement_date"] = "2026-09-15"

    # 5. Incorrect fee
    settlements[49]["fee"] += 50
    settlements[49]["settlement_amount"] -= 50

    # 6. Invoice mismatch
    invoices[59]["invoice_amount"] += 250

    # 7. Unknown transaction
    settlements[69]["transaction_id"] = "TXN-UNKNOWN-0070"

    # 8. Partial settlement
    payouts[79]["payout_amount"] = round(
        payouts[79]["payout_amount"] * 0.5,
        2,
    )

    # 9. Another amount mismatch
    settlements[84]["settlement_amount"] += 125

    # 10. Malformed transaction record
    transactions[90]["amount"] = "N/A"

    # 11. Malformed settlement record
    settlements[94]["settlement_amount"] = "INVALID"

    # 12. Missing payout
    payouts[99]["status"] = "MISSING"


if __name__ == "__main__":
    data = generate_financial_data()

    print("CHIMERA FINANCE DATA GENERATOR")
    print("=" * 40)

    for category, records in data.items():
        print(f"{category.capitalize():15}: {len(records)} records")

    print()
    print("Sample transaction:")
    print(data["transactions"][0])

    print()
    print("Sample settlement:")
    print(data["settlements"][0])