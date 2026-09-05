# Chimera

## AI Finance Controller

Chimera is an open-source AI assistant platform built around local LLMs, memory, RAG, tool execution, and autonomous agents.

For the Razorpay AI Buildathon 2026, Chimera has been extended with an **AI Finance Controller** that automates a complete financial reconciliation workflow over synthetic transaction records.

The system ingests financial records, reconciles transactions, detects discrepancies, calculates operational metrics, explains exceptions using an LLM, and maintains an audit trail.

---

## Razorpay AI Buildathon 2026

### Track 04: AI Finance Controller

**Problem:** Finance operations teams spend significant time reconciling transactions across multiple records and manually investigating discrepancies.

**Solution:** Chimera provides an AI-assisted finance operations workflow that:

- Processes 100+ financial records
- Matches transactions across financial sources
- Detects reconciliation exceptions
- Identifies duplicate and unknown transactions
- Calculates reconciliation metrics
- Explains exceptions using an LLM
- Recommends corrective actions
- Maintains an audit trail
- Presents results through a dashboard

The finance processing layer is deterministic for reliable financial calculations, while the LLM is used for exception reasoning and explanation.

---

## Finance Workflow

```text
Synthetic Financial Data
          |
          v
     Data Ingestion
          |
          v
 Reconciliation Engine
          |
          v
     Finance Tools
          |
          v
    Chimera Agent
          |
          v
   Exception Analysis
          |
          v
     Audit Logging
          |
          v
      Dashboard
Current Results

The controller currently processes 101 financial records.

Metric	Result
Records Received	101
Records Processed	101
Matched	88
Exceptions	13
Match Rate	87.13%
Automatically Resolved	1
Unresolved	12
Total Transaction Value	₹206,500
Reconciled Value	₹175,250
Exception Value	₹31,250

The dataset intentionally contains multiple anomaly types so that the reconciliation engine can demonstrate both successful matches and exception handling.

Detected Exceptions

The reconciliation engine checks for:

Missing settlement records
Missing invoice records
Missing payout records
Settlement amount mismatches
Incorrect fees
Delayed settlements
Invoice amount mismatches
Partial payouts
Duplicate transactions
Unknown transactions
Malformed transaction amounts
Payout mismatches

Each exception is returned with its transaction ID, status, amount, and detected issues.

AI Exception Analysis

Financial arithmetic and reconciliation decisions are handled deterministically.

The LLM is used only when an exception requires explanation.

For an exception, Chimera can generate:

Severity
Explanation
Recommended Action

Example:

Transaction: TXN-0020

Severity:
HIGH

Explanation:
Settlement record is missing.

Recommended Action:
Process settlement.

This separation prevents the LLM from being responsible for financial arithmetic while still using AI where reasoning and explanation are useful.

Finance Tools

The finance workflow exposes dedicated tools through Chimera's existing tool architecture.

load_financial_batch

Loads the financial dataset into the workflow.

reconcile_batch

Runs deterministic reconciliation across transactions, settlements, invoices, and payouts.

get_exceptions

Returns transactions that require investigation.

calculate_metrics

Calculates operational reconciliation metrics.

The tools are registered through Chimera's existing tool registry and can be used by the agent workflow.

Reconciliation Logic

Each transaction is checked across the available financial records.

The engine verifies:

Transaction
   |
   +-- Settlement
   |
   +-- Invoice
   |
   +-- Payout

A transaction is considered matched only when the required records exist and their values satisfy the reconciliation rules.

Exceptions are generated when records are missing, amounts differ, transactions are duplicated, or transaction identifiers are unknown.

Audit Logging

Each reconciliation run records an audit entry containing the generated metrics.

Audit records are stored locally at:

backend/storage/finance_audit.json

This provides a persistent history of reconciliation runs without requiring an external database.

Dashboard

The React dashboard provides:

Finance Controller navigation
Run Reconciliation button
Records processed
Matched records
Exception count
Match rate
Total transaction value
Reconciled value
Exception value
Automatically resolved count
Detailed exception table

The dashboard communicates with the FastAPI backend through:

POST /finance/reconcile
Architecture
                    CHIMERA
                       |
        +--------------+--------------+
        |                             |
   Existing AI Layer            Finance Layer
        |                             |
   Local LLM / Ollama          Data Generator
        |                       Reconciliation
   Memory / RAG                     Metrics
        |                       Exception Logic
   Tool Registry                Audit Logger
        |                             |
        +--------------+--------------+
                       |
                Finance Controller
                       |
                    FastAPI
                       |
                React Dashboard
Project Structure
Chimera/
│
├── backend/
│   ├── agents/
│   │   ├── agent_loop.py
│   │   └── agent_planner.py
│   │
│   ├── api/
│   │   └── routes/
│   │       ├── chat.py
│   │       ├── chats.py
│   │       ├── documents.py
│   │       ├── finance.py
│   │       └── health.py
│   │
│   ├── finance/
│   │   ├── __init__.py
│   │   ├── audit_logger.py
│   │   ├── controller.py
│   │   ├── data_generator.py
│   │   ├── exception_analyzer.py
│   │   ├── metrics.py
│   │   └── reconciliation_engine.py
│   │
│   ├── tools/
│   │   ├── base.py
│   │   ├── calculator.py
│   │   ├── executor.py
│   │   ├── finance.py
│   │   └── registry.py
│   │
│   └── main.py
│
├── frontend/
│   └── src/
│       ├── pages/
│       │   ├── FinanceDashboard.jsx
│       │   └── Home.jsx
│       │
│       ├── services/
│       │   └── financeService.js
│       │
│       ├── App.jsx
│       └── App.css
│
├── scripts/
│   └── test_finance_engine.py
│
├── backend/storage/
│   └── finance_audit.json
│
└── README.md
Technology Stack
Backend
Python
FastAPI
Ollama
Local LLMs
NumPy / Python data processing
FAISS
Sentence Transformers
Frontend
React
Vite
JavaScript
CSS
AI
Local LLM inference through Ollama
Agent planning
Tool execution
Exception explanation
Storage
JSON
FAISS vector database
Local filesystem
Running Chimera
1. Clone the repository
git clone https://github.com/husna-fathima-713/Chimera.git
cd Chimera
2. Create the Python environment
python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Start Ollama

Make sure Ollama is installed and a supported local model is available.

Example:

ollama list
5. Start the backend

From the project root:

python -m uvicorn backend.main:app --reload

The API runs at:

http://127.0.0.1:8000
6. Start the frontend

Open another terminal:

cd frontend
npm install
npm run dev

The frontend runs through Vite, normally at:

http://localhost:5173
Finance API
Reconcile Financial Batch
POST /finance/reconcile

Example:

curl -X POST http://127.0.0.1:8000/finance/reconcile

The response contains:

{
  "metrics": {},
  "exceptions": []
}
Testing

The deterministic reconciliation engine can be tested without running the LLM.

From the project root:

python -m scripts.test_finance_engine

Expected output includes:

Finance reconciliation engine test passed.

Records received  : 101
Records processed : 101
Matched           : 88
Exceptions        : 13
Match rate        : 87.13

Duplicate records : 2
Unknown records   : 1
Why the Finance Controller Uses Deterministic Logic

Financial reconciliation requires predictable arithmetic and matching.

The system therefore separates:

Deterministic Layer

Responsible for:

Amount comparison
Transaction matching
Duplicate detection
Missing record detection
Exception generation
Metrics
Audit logging
AI Layer

Responsible for:

Exception explanation
Severity classification
Recommended actions
Agent planning

This prevents unpredictable LLM output from directly controlling financial calculations.

Failure Handling

During development several issues were identified and corrected.

Duplicate Detection

The initial synthetic duplicate anomaly did not actually create a duplicate transaction.

The dataset was corrected so that a transaction record is genuinely duplicated and the reconciliation engine detects both occurrences.

Unknown Transaction Detection

The original unknown transaction anomaly changed the transaction identifier without creating a detectable cross-record condition.

The dataset was corrected so that the reconciliation engine can explicitly identify the unknown transaction.

Agent Iteration

The initial agent loop had a low iteration limit for multi-step workflows.

The iteration limit was increased so the finance workflow can execute multiple tool steps.

LLM Usage

The first finance design attempted to use the LLM for every exception.

This created unnecessary model calls.

The architecture was changed so that deterministic reconciliation happens first and the LLM is invoked only when an exception requires explanation.

Limitations

This prototype currently uses synthetic financial data.

It does not connect directly to:

Banking systems
Payment gateways
ERP systems
Production accounting databases

The reconciliation rules are designed for the buildathon prototype and would require additional validation before production deployment.

Future Improvements

Potential production extensions include:

Real Razorpay payment integration
Real-time transaction ingestion
PostgreSQL storage
Role-based access control
Human approval workflows
More advanced anomaly detection
Historical reconciliation analytics
Automated exception resolution
Financial reporting exports
Multi-agent finance workflows
Production-grade observability
Buildathon Demo Flow

The intended demonstration is:

1. Open Chimera
       |
2. Open Finance Controller
       |
3. Run Reconciliation
       |
4. Process 101 records
       |
5. Display 88 matched records
       |
6. Display 13 exceptions
       |
7. Show 87.13% match rate
       |
8. Inspect exception details
       |
9. Demonstrate AI exception analysis
       |
10. Show audit record

The complete flow demonstrates a finance operations loop from ingestion to reconciliation, exception analysis, and reporting.

Project Goal

Chimera's AI Finance Controller demonstrates how an existing local AI agent platform can be extended into a practical finance operations system.

The goal is not to replace deterministic financial systems with an LLM.

The goal is to combine reliable financial computation with AI reasoning where it provides the most value.

License

This project is open source and intended for educational, research, and prototype development.
