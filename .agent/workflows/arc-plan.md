---
description: Plan a phase of the project
---

I want to plan Phase [N] from my roadmap.

## Pre-Planning: Load All Context

**MANDATORY - Read these files FIRST:**
1. `.arc/PROJECT.md` - Understand what we're building
2. `.arc/ROADMAP.md` - See where this phase fits
3. `.arc/STATE.md` - Check current progress
4. `.arc/CONTRACTS.md` - Know existing APIs, models, conventions
5. `.arc/planning/phase-[N]-CONTEXT.md` - If exists, use preferences from discuss phase
6. `.arc/CODEBASE.md` - If exists, understand existing patterns (for brownfield projects)

## Planning Process

1. **Dashboard Initialization**:
   - Run `./venv/bin/python3 .agent/dashboard/update.py project="[Project Name]" phase="Phase [N]"`
   - Provide the user with the command to view the dashboard: `./dash`

2. Show me what Phase [N] is about (from ROADMAP.md)
3. **Update Dashboard**: Run `./venv/bin/python3 .agent/dashboard/update.py agent="Architect" status="THINKING" task="Clarifying requirements"`
4. Ask clarifying questions about:
   - UI/UX decisions (layout, interactions, etc.)
   - Technical approach (libraries, patterns, etc.)
   - Data handling (storage, validation, etc.)
   - Edge cases (errors, empty states, etc.)

5. **Skill Integration**:
   - Check `.agent/skills/` for skills relevant to this phase.
   - If found, read them and incorporate their standards into the plan.
   - Update Dashboard: `task="Incorporating [Skill Name] standards"`

6. After I answer, **Update Dashboard**: Run `./venv/bin/python3 .agent/dashboard/update.py agent="Architect" status="DESIGNING" task="Generating Phase Plan"`
7. Create a detailed plan
   - 3-5 atomic tasks (each can be done independently)
   - Clear file paths for each task
   - Specific implementation steps
   - Verification method for each task
   - Git commit message template
   - **What contracts will be added** (new endpoints, models, etc.)

7. Save to `.arc/planning/phase-[N]-PLAN.md` using the template

8. **Dashboard Log**: Run `./venv/bin/python3 .agent/dashboard/update.py agent="Architect" status="IDLE" task="Plan Ready" log="Phase [N] plan saved." main_status="IDLE" main_action="Waiting..."`
9. Show me the plan and ask if I want to adjust before executing

## Contract Awareness

When planning, check CONTRACTS.md for:
- Existing endpoints you can reuse
- Existing models you should extend
- Naming conventions to follow
- Colors/design tokens already defined

Note in the plan which NEW contracts will need to be added during execution.
