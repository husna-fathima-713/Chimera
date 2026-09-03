"""
Audit logging for Chimera Finance Controller.

Stores reconciliation summaries as JSON records so each finance
run can be reviewed later.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


AUDIT_LOG_PATH = (
    Path(__file__).resolve().parent.parent
    / "storage"
    / "finance_audit.json"
)


def log_reconciliation_run(
    metrics: dict[str, Any],
) -> dict[str, Any]:

    AUDIT_LOG_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    audit_record = {
        "timestamp": datetime.now(
            timezone.utc
        ).isoformat(),
        "metrics": metrics,
    }

    existing_records: list[dict[str, Any]] = []

    if AUDIT_LOG_PATH.exists():

        try:

            with AUDIT_LOG_PATH.open(
                "r",
                encoding="utf-8",
            ) as file:

                existing_records = json.load(file)

                if not isinstance(existing_records, list):
                    existing_records = []

        except (json.JSONDecodeError, OSError):

            existing_records = []

    existing_records.append(audit_record)

    with AUDIT_LOG_PATH.open(
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            existing_records,
            file,
            indent=2,
        )

    return audit_record


def get_audit_records() -> list[dict[str, Any]]:

    if not AUDIT_LOG_PATH.exists():
        return []

    try:

        with AUDIT_LOG_PATH.open(
            "r",
            encoding="utf-8",
        ) as file:

            records = json.load(file)

            if isinstance(records, list):
                return records

    except (json.JSONDecodeError, OSError):
        pass

    return []


if __name__ == "__main__":

    sample_metrics = {
        "records_processed": 101,
        "matched": 89,
        "exceptions": 12,
        "match_rate": 88.12,
    }

    record = log_reconciliation_run(
        sample_metrics
    )

    print("CHIMERA FINANCE AUDIT LOG")
    print("=" * 40)
    print(json.dumps(record, indent=2))