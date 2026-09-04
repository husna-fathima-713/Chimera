import { useState } from "react";

import { runFinanceReconciliation } from "../services/financeService";


function FinanceDashboard() {

    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);


    async function handleReconciliation() {

        setLoading(true);
        setError(null);

        try {

            const result = await runFinanceReconciliation();

            setData(result);

        }
        catch (err) {

            console.error(err);

            setError(
                "Unable to run reconciliation. Make sure the Chimera backend is running."
            );

        }
        finally {

            setLoading(false);

        }

    }


    const metrics = data?.metrics;


    return (

        <div className="finance-dashboard">

            <header className="finance-header">

                <div>

                    <p className="finance-label">
                        CHIMERA FINANCE CONTROLLER
                    </p>

                    <h1>
                        Financial Reconciliation
                    </h1>

                    <p className="finance-subtitle">
                        Reconcile transactions, detect exceptions,
                        and maintain an auditable financial record.
                    </p>

                </div>


                <button
                    className="reconcile-button"
                    onClick={handleReconciliation}
                    disabled={loading}
                >

                    {loading
                        ? "Running..."
                        : "Run Reconciliation"}

                </button>

            </header>


            {error && (

                <div className="finance-error">
                    {error}
                </div>

            )}


            {!data && !loading && (

                <div className="finance-empty">

                    <div className="finance-empty-icon">
                        ₹
                    </div>

                    <h2>
                        No reconciliation run yet
                    </h2>

                    <p>
                        Run the reconciliation engine to analyze
                        the current financial batch.
                    </p>

                </div>

            )}


            {loading && (

                <div className="finance-empty">

                    <div className="finance-spinner" />

                    <h2>
                        Reconciling financial records
                    </h2>

                    <p>
                        Comparing transactions, settlements,
                        invoices, and payouts.
                    </p>

                </div>

            )}


            {metrics && (

                <>

                    <section className="metrics-grid">

                        <div className="metric-card">

                            <span>
                                Records Processed
                            </span>

                            <strong>
                                {metrics.records_processed}
                            </strong>

                        </div>


                        <div className="metric-card">

                            <span>
                                Matched
                            </span>

                            <strong className="metric-success">
                                {metrics.matched}
                            </strong>

                        </div>


                        <div className="metric-card">

                            <span>
                                Exceptions
                            </span>

                            <strong className="metric-danger">
                                {metrics.exceptions}
                            </strong>

                        </div>


                        <div className="metric-card">

                            <span>
                                Match Rate
                            </span>

                            <strong>
                                {metrics.match_rate}%
                            </strong>

                        </div>

                    </section>


                    <section className="finance-summary">

                        <div>

                            <span>
                                Transaction Value
                            </span>

                            <strong>
                                ₹{metrics.total_transaction_value.toLocaleString("en-IN")}
                            </strong>

                        </div>


                        <div>

                            <span>
                                Reconciled Value
                            </span>

                            <strong>
                                ₹{metrics.reconciled_value.toLocaleString("en-IN")}
                            </strong>

                        </div>


                        <div>

                            <span>
                                Exception Value
                            </span>

                            <strong>
                                ₹{metrics.exception_value.toLocaleString("en-IN")}
                            </strong>

                        </div>


                        <div>

                            <span>
                                Auto Resolved
                            </span>

                            <strong className="metric-success">
                                {metrics.automatically_resolved}
                            </strong>

                        </div>

                    </section>


                    <section className="exceptions-section">

                        <div className="section-heading">

                            <div>

                                <p className="finance-label">
                                    EXCEPTION MONITOR
                                </p>

                                <h2>
                                    Detected Exceptions
                                </h2>

                            </div>

                            <span className="exception-count">
                                {data.exceptions.length} unresolved
                            </span>

                        </div>


                        <div className="exception-table">

                            <div className="exception-table-header">

                                <span>
                                    Transaction
                                </span>

                                <span>
                                    Status
                                </span>

                                <span>
                                    Amount
                                </span>

                                <span>
                                    Issues
                                </span>

                            </div>


                            {data.exceptions.map((exception, index) => (

                                <div
                                    className="exception-row"
                                    key={`${exception.transaction_id}-${index}`}
                                >

                                    <strong>
                                        {exception.transaction_id}
                                    </strong>


                                    <span className="status-badge">
                                        EXCEPTION
                                    </span>


                                    <span>
                                        {exception.transaction_amount === null
                                            ? "Invalid"
                                            : `₹${exception.transaction_amount.toLocaleString("en-IN")}`}
                                    </span>


                                    <div className="issue-list">

                                        {exception.issues.map((issue) => (

                                            <span
                                                className="issue-badge"
                                                key={issue}
                                            >
                                                {issue}
                                            </span>

                                        ))}

                                    </div>

                                </div>

                            ))}

                        </div>

                    </section>

                </>

            )}

        </div>

    );

}


export default FinanceDashboard;