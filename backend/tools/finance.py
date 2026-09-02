"""
Finance tools for Chimera Finance Controller.

These tools expose the deterministic finance engine through
Chimera's existing BaseTool interface.
"""

from __future__ import annotations

from typing import Any

from backend.finance.data_generator import generate_financial_data
from backend.finance.metrics import calculate_metrics
from backend.finance.reconciliation_engine import reconcile_financial_data
from backend.tools.base import BaseTool


_financial_data: dict[str, list[dict[str, Any]]] | None = None
_reconciliation_results: list[dict[str, Any]] | None = None


class LoadFinancialBatchTool(BaseTool):

    name = "load_financial_batch"

    description = (
        "Load a deterministic financial batch containing transactions, "
        "settlements, invoices, and payouts."
    )

    def execute(self, prompt):

        global _financial_data

        _financial_data = generate_financial_data()

        return {
            "records": {
                category: len(records)
                for category, records in _financial_data.items()
            },
            "message": "Financial batch loaded successfully.",
        }


class ReconcileBatchTool(BaseTool):

    name = "reconcile_batch"

    description = (
        "Reconcile loaded transactions against settlements, "
        "invoices, and payouts and detect financial exceptions."
    )

    def execute(self, prompt):

        global _reconciliation_results

        if _financial_data is None:
            raise RuntimeError(
                "No financial batch loaded. "
                "Run load_financial_batch first."
            )

        _reconciliation_results = reconcile_financial_data(
            _financial_data
        )

        matched = sum(
            result["status"] == "MATCHED"
            for result in _reconciliation_results
        )

        exceptions = sum(
            result["status"] == "EXCEPTION"
            for result in _reconciliation_results
        )

        return {
            "records_processed": len(_reconciliation_results),
            "matched": matched,
            "exceptions": exceptions,
            "message": "Financial batch reconciled successfully.",
        }


class GetExceptionsTool(BaseTool):

    name = "get_exceptions"

    description = (
        "Return all financial reconciliation exceptions detected "
        "in the loaded batch."
    )

    def execute(self, prompt):

        if _reconciliation_results is None:
            raise RuntimeError(
                "No reconciliation results available. "
                "Run reconcile_batch first."
            )

        exceptions = [
            result
            for result in _reconciliation_results
            if result["status"] == "EXCEPTION"
        ]

        return {
            "count": len(exceptions),
            "exceptions": exceptions,
        }


class CalculateMetricsTool(BaseTool):

    name = "calculate_metrics"

    description = (
        "Calculate deterministic financial reconciliation metrics "
        "for the loaded batch."
    )

    def execute(self, prompt):

        if _financial_data is None:
            raise RuntimeError(
                "No financial batch loaded. "
                "Run load_financial_batch first."
            )

        if _reconciliation_results is None:
            raise RuntimeError(
                "No reconciliation results available. "
                "Run reconcile_batch first."
            )

        return calculate_metrics(
            _financial_data,
            _reconciliation_results,
        )