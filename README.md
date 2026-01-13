# Agentic AI System for Governed Financial Insights (Canada 🇨🇦)

## Enterprise-grade Agentic AI workflow built with LangGraph for governed, auditable financial insights in regulated environments.

This project demonstrates how autonomous AI agents can safely collaborate to analyze financial data, generate insights, enforce validation guardrails, and produce executive-ready reports — with a mandatory human-in-the-loop approval checkpoint.

The system is intentionally designed to reflect Canadian regulated environments, including:

- Banking & Credit Unions
- Insurance & Risk Analytics
- Public Sector / Regulatory Reporting

  <img width="1536" height="1024" alt="Agentic AI System" src="https://github.com/user-attachments/assets/b0010981-8b49-44bf-9cb6-3a9aee54ff15" />

## System Overview

The workflow is orchestrated using LangGraph, where each agent has a single, well-defined responsibility and communicates through a shared, typed state.

# End-to-end agent flow:

Planner Agent
   ↓
Data Analysis Agent
   ↓
Insight Generation Agent
   ↓
Validation / Guardrail Agent
   ↓
Executive Report Agent
   ↓
Human-in-the-Loop Approval

![Agentic Ai Financial Insights Workflow](https://github.com/user-attachments/assets/a691a495-0766-4594-be8a-1b8ebb49a995)


Each agent has a **single responsibility** and communicates through a shared, typed state managed by LangGraph.

## Agent Responsibilities

| Agent                | Responsibility                                              |
| -------------------- | ------------------------------------------------------------|
| Planner Agent        | Decomposes business goal into executable analytical tasks   |
| Data Analysis Agent  | Loads financial data and computes KPIs                      |
| Insight Agent        | Translates KPIs into business-readable insights             |
| Validation Agent     | Applies rule-based guardrails and sanity checks             |
| Report Agent         | Generates executive-ready financial reports                 |
| Human Approval Agent | Requires explicit human approval before workflow completion |

## Governance & Controls (Why this matters)

The system enforces responsible AI principles expected in regulated financial environments:

* KPI schema validation
* Sanity checks on financial metrics
* Automatic blocking of downstream steps if validation fails
* Mandatory human approval before final output
* Structured logging for traceability and audit readiness

No reports are finalized or released without passing governance checks and human validation.

## Tech Stack

* **LangGraph** – Agent orchestration & state management
* **Python** – Core implementation
* **Pandas** – Financial data analysis
* **Structured Logging** – Observability & audit trail

No local models or GPUs required — API-ready and lightweight.

## How to Run

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py

## Output

Draft / Final executive reports are generated in:

- outputs/

Reports are only finalized after successful validation and human approval.

# Human-in-the-Loop Example

## Approval granted

Approve report? (y/n): y
Human approved report
Workflow execution completed
![Approval granted](https://github.com/user-attachments/assets/030a1c47-3a47-4a84-8a78-da487c5cf9bf)

## Approval rejected

Approve report? (y/n): n
Human requested changes / rejected report
![Approval rejected](https://github.com/user-attachments/assets/8f7d9e56-9de5-4922-8d46-d42fe767697c)
