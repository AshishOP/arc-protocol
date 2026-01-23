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
5. Execute tasks ONE AT A TIME or DELEGATE:
   - **Update Dashboard**: Run `./venv/bin/python3 .agent/dashboard/update.py agent="Executor" status="WORKING" task="[Task Name]"`
   - **Parallel Delegation**: If a task is tactical (boilerplate, research, audit), use `arc_spawn_agent` to delegate it to a subagent using the `flash` model.
   - **Assume Role**: If doing the task yourself, state: "Assuming [Skill Name] Subagent role."
   - Do the task
   - **Monitor Subagents**: Keep an eye on the dashboard logs for subagent completion.
   - **Update CONTRACTS.md** if you create any new:
     - API endpoints
     - Data models
     - Environment variables
     - Components
   - Run verification
   - **Dashboard Log**: Update dashboard with current task results.
   - Show me the results
   - Git commit with message from plan
   - Wait for my confirmation before next task

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
