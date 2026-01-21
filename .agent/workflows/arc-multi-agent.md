---
description: Orchestrate multiple subagents for complex feature development
---

# ARC Multi-Agent Orchestration

Use this workflow for high-complexity features that require distinct analysis, implementation, and verification phases.

## 0. Dashboard Initialization
- Run `./venv/bin/python3 .agent/dashboard/update.py project="[Project Name]" phase="Complex Feature Orchestration" main_status="ORCHESTRATING" main_action="Managing Subagent Handover" log="Starting Multi-Agent Loop..."`

## 1. Analyze (Architect Mode)
- **Role Assignment**: Assume the **Architect** role.
- **Update Dashboard**: Run `./venv/bin/python3 .agent/dashboard/update.py agent="Architect" status="THINKING" task="System Analysis & Design"`
- Analyze the project structure and existing contracts in `.arc/CONTRACTS.md`.
- Propose a technical design and get user approval.

## 2. Implement (Executor Mode)
- **Role Assignment**: Assume the **Executor** role.
- **Update Dashboard**: Run `./venv/bin/python3 .agent/dashboard/update.py agent="Executor" status="WORKING" task="Feature Implementation"`
- Execute the planned changes task-by-task.
- Update `.arc/CONTRACTS.md` for any new exports or APIs.

## 3. Verify (Reviewer Mode)
- **Role Assignment**: Assume the **Reviewer** role.
- **Update Dashboard**: Run `./venv/bin/python3 .agent/dashboard/update.py agent="Reviewer" status="WORKING" task="Validation & Testing"`
- Run tests or perform static analysis to ensure the implementation matches the design.
- Verify against the standards in `.agent/skills/`.

## 4. Final Review & Integration
- Update Dashboard: `status="DONE" task="Orchestration Complete" main_status="IDLE" main_action="Waiting..."`
- Summarize the changes and confirm all sub-tasks are integrated.
