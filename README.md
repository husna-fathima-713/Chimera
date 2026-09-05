# Chimera

## AI Finance Controller

Chimera is an open-source AI assistant platform built around local LLMs, memory, RAG, tool execution, and autonomous agents.

For the Razorpay AI Buildathon 2026, Chimera has been extended with an **AI Finance Controller** that automates a complete financial reconciliation workflow over synthetic transaction records.

The system ingests financial records, reconciles transactions, detects discrepancies, calculates operational metrics, explains exceptions using an LLM, and maintains an audit trail.

---

## Razorpay AI Buildathon 2026

### Track 04: AI Finance Controller

Finance operations teams spend significant time reconciling transactions across multiple financial records and manually investigating discrepancies.

Chimera addresses this by providing an AI-assisted finance operations workflow that:

- Processes 100+ financial records
- Matches transactions across financial sources
- Detects reconciliation exceptions
- Identifies duplicate transactions
- Identifies unknown transactions
- Detects missing financial records
- Calculates reconciliation metrics
- Explains exceptions using an LLM
- Recommends corrective actions
- Maintains an audit trail
- Presents reconciliation results through a dashboard

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
```
Current Results

The finance controller currently processes 101 financial records.

| Metric                  |   Result |
| ----------------------- | -------: |
| Records Received        |      101 |
| Records Processed       |      101 |
| Matched                 |       88 |
| Exceptions              |       13 |
| Match Rate              |   87.13% |
| Automatically Resolved  |        1 |
| Unresolved              |       12 |
| Total Transaction Value | ₹206,500 |
| Reconciled Value        | ₹175,250 |
| Exception Value         |  ₹31,250 |


The synthetic dataset intentionally contains multiple anomaly types so that the reconciliation engine can demonstrate both successful matches and exception handling.

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

Each exception contains information such as:

Transaction ID
Transaction amount
Status
Detected issue
Related financial records

AI Exception Analysis

Financial arithmetic and reconciliation decisions are handled deterministically.

The LLM is used when an exception requires explanation.

For an exception, Chimera generates:
```
Severity
Explanation
Recommended Action
```

Example:
```
Transaction: TXN-0020

Severity:
HIGH

Explanation:
Settlement record is missing.

Recommended Action:
Process settlement.
```
This separation prevents the LLM from being responsible for financial arithmetic while still using AI where reasoning and explanation are useful.

Finance Tools

The finance workflow exposes dedicated tools through Chimera's existing tool architecture.
```
load_financial_batch
```
Loads the synthetic financial dataset into the workflow.
```
reconcile_batch
```
Runs deterministic reconciliation across transactions, settlements, invoices, and payouts.
```
get_exceptions
```
Returns transactions that require investigation.
```
calculate_metrics
```
Calculates reconciliation and operational metrics.

These tools are registered through Chimera's existing tool registry and can be used by the agent workflow.

Reconciliation Logic

Each transaction is checked against the available financial records.
```
Transaction
    |
    +---- Settlement
    |
    +---- Invoice
    |
    +---- Payout
```
The reconciliation engine verifies whether the required records exist and whether their values satisfy the reconciliation rules.

A transaction is marked as matched when the required records are present and consistent.

An exception is generated when:

A required record is missing
Amounts do not match
Fees are incorrect
A transaction is duplicated
A transaction is unknown
A transaction contains malformed data
A settlement is delayed
A payout is inconsistent

Deterministic Finance Layer

The finance controller deliberately keeps critical financial operations deterministic.

The deterministic layer is responsible for:

Transaction matching
Amount comparison
Duplicate detection
Missing record detection
Unknown transaction detection
Exception generation
Metrics calculation
Audit logging

This makes the reconciliation results predictable and reproducible.

AI Reasoning Layer

The AI layer is responsible for tasks where language-model reasoning is useful.

It handles:

Exception explanation
Severity classification
Recommended corrective actions
Agent planning
Tool orchestration

The LLM therefore complements the finance engine instead of replacing it.

Audit Logging

Each reconciliation run records an audit entry containing the generated metrics.

Audit records are stored locally at:
```
backend/storage/finance_audit.json
```
This provides a persistent history of reconciliation runs without requiring an external database.

Finance Dashboard

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
```
POST /finance/reconcile
```

Architecture
```
                         CHIMERA
                            |
             +--------------+--------------+
             |                             |
             v                             v
       Existing AI Layer             Finance Layer
             |                             |
       Local LLM / Ollama          Data Generator
             |                     Reconciliation
       Memory / RAG                    Metrics
             |                     Exception Logic
       Tool Registry                 Audit Logger
             |                             |
             +--------------+--------------+
                            |
                            v
                   Finance Controller
                            |
                            v
                         FastAPI
                            |
                            v
                    React Dashboard
```
Project Structure
```
Chimera/
│
├── backend/
│   │
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
│   │
│   └── src/
│       ├── components/
│       ├── pages/
│       │   ├── FinanceDashboard.jsx
│       │   └── Home.jsx
│       │
│       ├── services/
│       │   ├── financeService.js
│       │   └── ...
│       │
│       ├── App.jsx
│       └── App.css
│
├── scripts/
│   └── test_finance_engine.py
│
├── backend/
│   └── storage/
│       └── finance_audit.json
│
├── requirements.txt
└── README.md
```
Technology Stack

Backend
Python
FastAPI
Ollama
Local LLMs
FAISS
Sentence Transformers
JSON-based local storage

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
1. Clone the Repository
```
git clone https://github.com/husna-fathima-713/Chimera.git
cd Chimera
```
3. Create the Python Environment
```
python3 -m venv .venv
source .venv/bin/activate
```
5. Install Dependencies
```
pip install -r requirements.txt
```
7. Start Ollama

Make sure Ollama is installed and a supported local model is available.

Check available models:
```
ollama list
```
5. Start the Backend

From the project root:

python -m uvicorn backend.main:app --reload

The backend runs at:
```
http://127.0.0.1:8000
```
6. Start the Frontend

Open another terminal:
```
cd frontend
npm install
npm run dev
```

The frontend normally runs at:
```
http://localhost:5173
```
Finance API

Reconcile Financial Batch
```
POST /finance/reconcile
```
You can test the endpoint directly:
```
curl -X POST http://127.0.0.1:8000/finance/reconcile
```
The response contains:
```

{
  "metrics": {},
  "exceptions": []
}
```

The actual response contains the calculated reconciliation metrics and the detected exceptions.

Testing

The deterministic reconciliation engine can be tested without running the LLM.

From the project root:
```
python -m scripts.test_finance_engine
```
Expected output:

Finance reconciliation engine test passed.
```
Records received  : 101
Records processed : 101
Matched           : 88
Exceptions        : 13
Match rate        : 87.13

Duplicate records : 2
Unknown records   : 1
Agent Workflow
```
Chimera's agent planner can execute finance operations through the registered finance tools.

The intended workflow is:
```
1. load_financial_batch
        |
        v
2. reconcile_batch
        |
        v
3. get_exceptions
        |
        v
4. calculate_metrics
```
The agent is instructed not to repeat tools that have already completed successfully.

The finance controller itself remains deterministic, while the agent layer provides orchestration and AI-assisted reasoning.

Failure Handling

Several implementation issues were identified and corrected during development.

Duplicate Detection

The initial synthetic duplicate anomaly did not actually create a duplicate transaction.

The dataset was corrected so that a transaction record is genuinely duplicated and the reconciliation engine detects both occurrences.

Unknown Transaction Detection

The original unknown transaction anomaly did not create a detectable cross-record condition.

The dataset was corrected so that the reconciliation engine can explicitly identify the unknown transaction.

Agent Iteration

The initial agent loop had a low iteration limit for multi-step workflows.

The iteration limit was increased so the finance workflow can execute multiple tool steps.

Excessive LLM Usage

The initial finance design attempted to use the LLM for every exception.

This created unnecessary model calls and increased processing overhead.

The architecture was changed so that:
```
Deterministic Reconciliation
            |
            v
      Detect Exceptions
            |
            v
    LLM Only When Needed
```
This reduced unnecessary model usage and keeps financial calculations deterministic.

Frontend Integration

The initial frontend integration did not immediately display the new Finance Controller navigation and dashboard.

The React application routing and dashboard integration were corrected and verified.

Why This Architecture

A finance controller should not ask a language model to decide whether:
```
₹10,000 == ₹10,000
```
That is a job for deterministic code.

The LLM is more useful for questions such as:

Why did this transaction fail reconciliation?

How severe is the issue?

What should an operations team investigate next?

Therefore, Chimera separates financial computation from AI reasoning.

                    Finance Controller
                           |
              +------------+------------+
              |                         |
              v                         v
      Deterministic Logic         AI Reasoning
              |                         |
        Calculations              Explanations
        Matching                  Severity
        Validation                Actions
        Metrics                   Planning
        Audit
Limitations

This implementation currently uses synthetic financial data.

It does not directly connect to:

Banking systems
Payment gateways
ERP systems
Production accounting databases

The reconciliation rules are designed for a buildathon prototype and would require additional validation before production deployment.

The current audit storage also uses local JSON rather than a production database.

Future Improvements

Potential production extensions include:

Real Razorpay payment integration
Real-time transaction ingestion
PostgreSQL storage
Role-based access control
Human approval workflows
Advanced anomaly detection
Historical reconciliation analytics
Automated exception resolution
Financial report exports
Multi-agent finance workflows
Production observability
Alerting for high-severity exceptions
Buildathon Demo Flow

The intended demonstration flow is:
```
1. Open Chimera
        |
        v
2. Open Finance Controller
        |
        v
3. Run Reconciliation
        |
        v
4. Process 101 records
        |
        v
5. Display 88 matched records
        |
        v
6. Display 13 exceptions
        |
        v
7. Show 87.13% match rate
        |
        v
8. Inspect exception details
        |
        v
9. Demonstrate AI exception analysis
        |
        v
10. Show audit record
```
This demonstrates the complete finance operations loop:
```
Ingestion
    ↓
Reconciliation
    ↓
Exception Detection
    ↓
AI Explanation
    ↓
Audit
    ↓
Reporting
Project Goal
```
Chimera's AI Finance Controller demonstrates how an existing local AI agent platform can be extended into a practical finance operations system.

The goal is not to replace deterministic financial systems with an LLM.

The goal is to combine reliable financial computation with AI reasoning where it provides practical value.

Repository

GitHub:
```
https://github.com/husna-fathima-713/Chimera
```
License
This project is open source and intended for educational, research, and prototype development.

This project is open source and intended for educational, research, and prototype development.
