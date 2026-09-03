from backend.finance.audit_logger import log_reconciliation_run
from backend.finance.data_generator import generate_financial_data
from backend.finance.exception_analyzer import ExceptionAnalyzer
from backend.finance.metrics import calculate_metrics
from backend.finance.reconciliation_engine import reconcile_financial_data


def run_finance_controller():

    data = generate_financial_data()

    results = reconcile_financial_data(data)

    metrics = calculate_metrics(
        data,
        results,
    )

    exceptions = [
        result
        for result in results
        if result["status"] == "EXCEPTION"
    ]

    analyses = []

    analyzer = ExceptionAnalyzer()

    for exception in exceptions:
        analysis = analyzer.analyze(exception)

        analyses.append(
            {
                "transaction_id": exception["transaction_id"],
                "issues": exception["issues"],
                **analysis,
            }
        )

    log_reconciliation_run(metrics)

    return {
        "metrics": metrics,
        "exceptions": exceptions,
        "analyses": analyses,
    }