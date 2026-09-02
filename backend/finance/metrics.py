"""
Financial reconciliation metrics for Chimera Finance Controller.

This module calculates deterministic reconciliation statistics from
the output produced by reconciliation_engine.py.
"""

from __future__ import annotations

from typing import Any


def calculate_metrics(
    data: dict[str, list[dict[str, Any]]],
    results: list[dict[str, Any]],
) -> dict[str, Any]:
    """
    Calculate reconciliation metrics.

    Args:
        data: Original financial datasets.
        results: Reconciliation results.

    Returns:
        Dictionary containing reconciliation metrics.
    """

    transactions = data.get("transactions", [])

    records_received = len(transactions)
    records_processed = len(results)

    matched = sum(
        result.get("status") == "MATCHED"
        for result in results
    )

    exceptions = sum(
        result.get("status") == "EXCEPTION"
        for result in results
    )

    match_rate = (
        (matched / records_processed) * 100
        if records_processed
        else 0.0
    )

    automatically_resolved = sum(
        _is_automatically_resolvable(result)
        for result in results
    )

    unresolved = exceptions - automatically_resolved

    total_transaction_value = sum(
        _safe_float(transaction.get("amount"))
        for transaction in transactions
        if _safe_float(transaction.get("amount")) is not None
    )

    reconciled_value = sum(
        result.get("transaction_amount", 0)
        for result in results
        if result.get("status") == "MATCHED"
        and result.get("transaction_amount") is not None
    )

    exception_value = sum(
        result.get("transaction_amount", 0)
        for result in results
        if result.get("status") == "EXCEPTION"
        and result.get("transaction_amount") is not None
    )

    return {
        "records_received": records_received,
        "records_processed": records_processed,
        "matched": matched,
        "exceptions": exceptions,
        "match_rate": round(match_rate, 2),
        "automatically_resolved": automatically_resolved,
        "unresolved": max(unresolved, 0),
        "total_transaction_value": round(
            total_transaction_value,
            2,
        ),
        "reconciled_value": round(
            reconciled_value,
            2,
        ),
        "exception_value": round(
            exception_value,
            2,
        ),
    }


def _is_automatically_resolvable(
    result: dict[str, Any],
) -> bool:
    """
    Determine whether an exception is suitable for automatic handling.

    Currently, only delayed settlements are considered automatically
    resolvable. Financial mismatches and malformed records require
    review.
    """

    issues = result.get("issues", [])

    if not issues:
        return False

    return set(issues) == {"DELAYED_SETTLEMENT"}


def _safe_float(value: Any) -> float | None:
    """Safely convert a value to float."""

    if isinstance(value, bool):
        return None

    try:
        return float(value)
    except (TypeError, ValueError):
        return None


if __name__ == "__main__":
    from backend.finance.data_generator import generate_financial_data
    from backend.finance.reconciliation_engine import (
        reconcile_financial_data,
    )

    data = generate_financial_data()

    results = reconcile_financial_data(data)

    metrics = calculate_metrics(
        data,
        results,
    )

    print("CHIMERA FINANCE METRICS")
    print("=" * 40)

    for key, value in metrics.items():
        print(f"{key:25}: {value}")