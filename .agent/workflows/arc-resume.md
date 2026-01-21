---
description: Resume work from a previous session
---

I'm resuming work. Load my project context.

0. **Dashboard Restore**:
   - Run `./venv/bin/python3 .agent/dashboard/update.py main_status="SYNCING" main_action="Restoring Context" log="Resuming session..."`

## Load All Context Files

**Read these files:**
1. `.arc/PROJECT.md` - What we're building
2. `.arc/ROADMAP.md` - All phases and progress
3. `.arc/STATE.md` - Where we left off
4. `.arc/CONTRACTS.md` - All shared definitions
5. `.arc/CODEBASE.md` - If exists, existing codebase patterns
6. Current phase plan from `.arc/planning/` (if exists)
7. Current phase CONTEXT from `.arc/planning/` (if exists)

## Tell Me

After reading, report:
- Project name and goal
- Current phase and task
- What I was doing when I paused
- Any blockers or decisions needed
- Recent contract changes (if any)
- Suggested next action

## Ask

"What do you want to do?"
- Continue current task
- Start new phase
- Review/adjust roadmap
- Update contracts
- Something else
