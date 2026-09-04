const API_BASE_URL = "http://127.0.0.1:8000";

export async function runFinanceReconciliation() {
    const response = await fetch(
        `${API_BASE_URL}/finance/reconcile`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
        }
    );

    if (!response.ok) {
        throw new Error(
            `Finance reconciliation failed: ${response.status}`
        );
    }

    return response.json();
}