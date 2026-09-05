````markdown
# Chimera

## AI Finance Controller

Chimera is an open-source AI assistant platform built around local LLMs, memory, RAG, tool execution, and autonomous agents.

For the Razorpay AI Buildathon, Chimera has been extended with an **AI Finance Controller** that automates a complete financial reconciliation workflow over synthetic transaction records.

The system ingests financial records, reconciles transactions, detects discrepancies, calculates operational metrics, explains exceptions using an LLM, and maintains an audit trail.

---

# Razorpay AI Buildathon 2026

### Track 04: AI Finance Controller

### Problem

Finance operations teams often spend significant time reconciling transactions across different financial records and manually investigating exceptions.

The goal of this implementation is to automate one complete finance-operations loop:

```text
Financial Records
       ↓
Data Ingestion
       ↓
Reconciliation
       ↓
Exception Detection
       ↓
Exception Analysis
       ↓
Metrics
       ↓
Audit Report
````

The system works with a synthetic dataset containing more than 50 financial records and produces a reconciliation result that can be inspected through the Chimera dashboard.

---

# What Chimera Does

The Finance Controller performs the following operations:

* Generates a synthetic financial dataset
* Processes 100+ financial records
* Matches transactions across financial records
* Detects missing records
* Detects duplicate transactions
* Detects unknown transactions
* Detects amount mismatches
* Detects incorrect fees
* Detects delayed settlements
* Detects malformed financial data
* Calculates reconciliation metrics
* Generates an exception list
* Uses a local LLM to explain selected exceptions
* Produces recommended actions
* Records reconciliation runs in an audit log
* Displays the results through a web dashboard

---

# Current Reconciliation Results

The current synthetic dataset contains:

| Metric                  |  Result |
| ----------------------- | ------: |
| Records received        |     101 |
| Records processed       |     101 |
| Matched records         |      88 |
| Exceptions              |      13 |
| Match rate              |  87.13% |
| Automatically resolved  |       1 |
| Unresolved              |      12 |
| Total transaction value | 206,500 |
| Reconciled value        | 175,250 |
| Exception value         |  31,250 |

The dataset intentionally contains multiple types of financial anomalies so that the reconciliation engine can demonstrate both successful matches and exception handling.

---

# Architecture

```text
                 ┌──────────────────────┐
                 │   Synthetic Finance  │
                 │       Dataset        │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    Data Generator    │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Reconciliation Engine│
                 │                      │
                 │ Match Transactions   │
                 │ Detect Exceptions    │
                 └──────────┬───────────┘
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
     ┌─────────────────┐        ┌─────────────────┐
     │  Finance Tools  │        │ Metrics Engine  │
     │                 │        │                 │
     │ Load Batch      │        │ Match Rate      │
     │ Reconcile       │        │ Processed       │
     │ Exceptions      │        │ Exception Value │
     │ Metrics         │        │                 │
     └────────┬────────┘        └────────┬────────┘
              │                          │
              └─────────────┬────────────┘
                            ▼
                 ┌─────────────────────┐
                 │     Chimera Agent   │
                 │      AgentLoop      │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ LLM Exception       │
                 │ Analysis             │
                 │                     │
                 │ Severity            │
                 │ Explanation         │
                 │ Recommended Action  │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │     Audit Logger    │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │  Finance Dashboard  │
                 └─────────────────────┘
```

---

# Design Approach

The finance reconciliation itself is deterministic.

Financial calculations and transaction matching should not depend on an LLM because incorrect arithmetic or matching decisions can produce unreliable financial results.

Therefore, Chimera separates the workflow into two layers:

### Deterministic Finance Layer

Responsible for:

* Transaction matching
* Amount comparison
* Duplicate detection
* Missing record detection
* Exception classification
* Metrics calculation
* Audit logging

### AI Reasoning Layer

Responsible for:

* Explaining detected exceptions
* Assigning severity
* Suggesting a recommended action
* Helping an operator understand why an exception occurred

The LLM is therefore used for reasoning around exceptions rather than performing the underlying financial calculations.

---

# Finance Tools

The agent can access the finance workflow through dedicated tools:

```text
load_financial_batch
reconcile_batch
get_exceptions
calculate_metrics
```

These tools allow the Chimera AgentLoop to execute the finance workflow as a sequence of operations.

The intended workflow is:

```text
load_financial_batch
        ↓
reconcile_batch
        ↓
get_exceptions
        ↓
calculate_metrics
```

---

# Exception Detection

The synthetic dataset contains several intentionally introduced anomalies.

Examples include:

* Amount mismatch
* Missing settlement
* Duplicate transaction
* Delayed settlement
* Incorrect fee
* Invoice mismatch
* Unknown transaction
* Partial settlement
* Malformed transaction amount
* Malformed settlement amount
* Missing payout

This allows the system to demonstrate reconciliation rather than simply returning a successful result for every record.

---

# LLM Exception Analysis

When an exception requires additional reasoning, Chimera can send the detected exception to the local LLM.

The analysis produces:

```text
Severity
Explanation
Recommended Action
```

Example workflow:

```text
Detected Exception
       ↓
Exception Analyzer
       ↓
Local LLM
       ↓
Severity
Explanation
Recommended Action
```

The analysis is performed on demand rather than sending every transaction through the LLM.

This keeps the core financial processing deterministic and avoids unnecessary model calls.

---

# Audit Logging

Each reconciliation run records the resulting operational metrics in:

```text
backend/storage/finance_audit.json
```

This provides a basic audit trail showing when reconciliation was executed and what the resulting metrics were.

---

# Dashboard

The Finance Controller dashboard provides:

* Reconciliation controls
* Records processed
* Matched records
* Exception count
* Match rate
* Transaction value
* Reconciled value
* Exception value
* Automatically resolved exceptions
* Exception transaction table
* Detected exception types

The dashboard is designed to make the reconciliation result directly inspectable rather than hiding the output behind the agent.

---

# Project Structure

```text
Chimera/
│
├── backend/
│   ├── agents/
│   │   ├── agent_loop.py
│   │   └── agent_planner.py
│   │
│   ├── api/
│   │   └── routes/
│   │       └── finance.py
│   │
│   ├── finance/
│   │   ├── data_generator.py
│   │   ├── reconciliation_engine.py
│   │   ├── metrics.py
│   │   ├── audit_logger.py
│   │   ├── exception_analyzer.py
│   │   └── controller.py
│   │
│   ├── tools/
│   │   ├── base.py
│   │   ├── registry.py
│   │   ├── executor.py
│   │   └── finance.py
│   │
│   └── main.py
│
├── frontend/
│   └── src/
│       ├── pages/
│       │   ├── Home.jsx
│       │   └── FinanceDashboard.jsx
│       │
│       └── services/
│           └── financeService.js
│
├── scripts/
│   └── test_finance_engine.py
│
└── README.md
```

---

# Technology Stack

### Backend

* Python
* FastAPI
* Ollama
* Local LLMs
* JSON-based persistence

### AI

* Local LLM through Ollama
* AgentLoop
* Tool execution
* Exception reasoning

### Frontend

* React
* Vite
* JavaScript
* CSS

### Development

* Git
* GitHub
* VS Code
* macOS / Linux-compatible development environment

---

# Running the Project

## 1. Clone the repository

```bash
git clone https://github.com/husna-fathima-713/Chimera.git
cd Chimera
```

## 2. Create and activate the virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

## 4. Start Ollama

Make sure Ollama is installed and the required local model is available.

Example:

```bash
ollama list
```

The current development environment uses:

```text
qwen3:4b
```

## 5. Start the backend

From the project root:

```bash
python -m uvicorn backend.main:app --reload
```

The API runs at:

```text
http://127.0.0.1:8000
```

## 6. Start the frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

The frontend is then available through the Vite development server.

---

# Finance API

The Finance Controller exposes:

```text
POST /finance/reconcile
```

Example:

```bash
curl -X POST http://127.0.0.1:8000/finance/reconcile
```

The endpoint returns:

```text
metrics
exceptions
```

The metrics contain the reconciliation summary, while the exceptions contain the individual records that require attention.

---

# Testing

The deterministic finance reconciliation engine can be tested with:

```bash
python -m scripts.test_finance_engine
```

The test verifies:

* 101 records received
* 101 records processed
* 88 matched
* 13 exceptions
* 87.13% match rate
* Two duplicate transaction results
* One unknown transaction result

---

# What Broke During Development

The build was developed iteratively and several issues were identified during implementation.

### AgentLoop execution limit

The initial AgentLoop did not allow enough iterations for the complete finance workflow.

The iteration limit was increased from 3 to 4 so the finance sequence could complete:

```text
Load
↓
Reconcile
↓
Exceptions
↓
Metrics
```

### Duplicate anomaly

The first duplicate test used a different transaction ID rather than actually duplicating an existing transaction.

The data generator was changed to copy an existing transaction so the reconciliation engine could detect a real duplicate.

### Unknown transaction anomaly

The initial unknown transaction setup did not create a detectable unknown relationship.

The transaction and settlement IDs were aligned to:

```text
TXN-UNKNOWN-0070
```

so that the reconciliation engine could correctly identify the transaction as unknown.

### Excessive LLM calls

The first Finance Controller design attempted to send every detected exception through the LLM.

That created unnecessary model calls.

The controller was changed so that:

```text
Financial processing → deterministic
Exception reasoning  → LLM on demand
```

This reduced unnecessary model usage while keeping AI reasoning in the workflow.

---

# Limitations

This build uses synthetic financial data and is intended as a prototype.

It does not currently connect to live banking, payment processor, or accounting systems.

The reconciliation rules are deterministic and designed for the synthetic dataset.

The audit log is currently stored locally as JSON rather than in a production database.

These choices keep the prototype simple and reproducible while demonstrating the complete finance-operations workflow.

---

# Future Improvements

Potential future extensions include:

* Real payment gateway integrations
* Database-backed financial records
* Scheduled reconciliation jobs
* Role-based finance operations
* More advanced anomaly detection
* Historical reconciliation analytics
* Human approval workflows
* Exportable reconciliation reports
* Production-grade audit storage
* Automated exception resolution policies

---

# Buildathon Demo Flow

The intended demonstration follows this sequence:

```text
1. Open Chimera
        ↓
2. Open Finance Controller
        ↓
3. Run Reconciliation
        ↓
4. Process 101 records
        ↓
5. Show 88 matched / 13 exceptions
        ↓
6. Show 87.13% match rate
        ↓
7. Inspect exception table
        ↓
8. Analyze a selected exception with the LLM
        ↓
9. Show severity and recommended action
        ↓
10. Show audit record
```

This demonstrates the complete finance-operations loop from ingestion to reconciliation, exception handling, AI reasoning, and auditability.

---

# Project Goal

Chimera is being developed as a modular local AI assistant rather than a single-purpose chatbot.

The Finance Controller demonstrates how the same agent and tool architecture can be extended into a domain-specific operational system where deterministic business logic and AI reasoning work together.

For this buildathon implementation, the focus is a single complete finance workflow:

**reconcile financial records, identify exceptions, explain them, and produce an auditable result.**

````
