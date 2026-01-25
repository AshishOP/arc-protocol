---
description: Execute a planned phase
---

Execute Phase [N] from .arc/planning/phase-[N]-PLAN.md

## Pre-Execution: Load All Context

**MANDATORY - Read these files FIRST:**
1. `.arc/PROJECT.md` - Understand what we're building
2. `.arc/ROADMAP.md` - See the big picture
3. `.arc/STATE.md` - Check what's in progress, avoid conflicts
4. `.arc/CONTRACTS.md` - Use exact names/formats defined here
5. `.arc/planning/phase-[N]-CONTEXT.md` - Honor user preferences from discuss phase
6. `.arc/CODEBASE.md` - If exists, follow existing patterns (brownfield projects)

## Execution Process

1. **Dashboard Initialization**:
   - Count total tasks in the plan
   - Run `./venv/bin/python3 .agent/dashboard/update.py project="[Project Name]" phase="Phase [N]" tasks_total=[COUNT] tasks_completed=0`
   - Provide the user with the command to view the dashboard: `./dash`

2. Read the phase plan from `.arc/planning/phase-[N]-PLAN.md`
3. Show me the tasks
4. **Track session start time**
5. Execute tasks ONE AT A TIME with **Parallel Orchestration**:
   - **Force Delegation Audit:** For each task, the Main Agent MUST answer: *"Can a subagent do the research, boilerplate, or auditing for this?"*
   - **Mandatory Delegation:** Use `arc_spawn_agent` to delegate tactical parts (boilerplates, documentation, data types) to specialized subagents.
   - **Proactive Auditing:** For every task involving implementation, spawn an `Auditor` subagent in parallel to review the code for security and contract compliance.
   - **Strategic Integration:** While subagents are `WORKING`, the Main Agent focuses on high-level orchestration, state management, and the next strategic task.
   - **Integration and Sign-off:** For every delegated task:
     1.  Read the subagent's log in `.arc/archive/subagent_logs/`.
     2.  Verify the output for contract compliance (CONTRACTS.md).
     3.  Integrate the code/research into the main repo.
     4.  Run a final manual/automated check.
     5.  **Log Integration:** `update.py log="Integrated [Subagent ID]'s work into [File Path]"`
   - **Update CONTRACTS.md** for all changes:
     - API endpoints, Data models, Env vars, Components.
   - Run verification.
   - **Git Commit:** Use message from plan and commit after EACH task.
   - Wait for user confirmation before next task.

6. After each task:
   - **Update metrics**: Run `./venv/bin/python3 .agent/dashboard/update.py tasks_completed=[N]` where N increments
   - Update `.arc/STATE.md` with progress
   - Tell me what's next

7. After all tasks complete:
   - **Calculate time**: Note session duration
   - Update Dashboard: Run `./venv/bin/python3 .agent/dashboard/update.py agent="Executor" status="DONE" task="Phase Complete" main_status="IDLE" main_action="Waiting..." time_elapsed="[TIME]"`
   - Create `.arc/planning/phase-[N]-SUMMARY.md` (use template at `.arc/templates/PHASE-SUMMARY.md`)
   - Move plan to `.arc/archive/`
   - Move CONTEXT.md to `.arc/archive/` (if exists)
   - Update `ROADMAP.md` to mark phase ✅ Complete
   - **Generate changelog**: Run `./venv/bin/python3 .agent/tools/generate_changelog.py`

## Contract Update Rule

> **If you CREATE something that another part of the system will USE, add it to CONTRACTS.md immediately.**

Examples:
- Created `/api/scan` endpoint → Add to CONTRACTS.md Section 1
- Created `Finding` model → Add to CONTRACTS.md Section 2
- Used new env var `OPENAI_API_KEY` → Add to CONTRACTS.md Section 5
- Created `Terminal` component → Add props to CONTRACTS.md Section 8

## Important

- Commit after EACH task, not at the end
- Update CONTRACTS.md BEFORE moving to next task
- Log contract updates in the "Update Log" section at bottom of CONTRACTS.md
