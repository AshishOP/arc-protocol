---
description: Quick ad-hoc task outside phase structure
---

Quick task: [description provided by user]

0. **Dashboard Update**:
   - Run `./venv/bin/python3 .agent/dashboard/update.py main_status="ACTING" main_action="Quick Fix/Task" log="Executing ad-hoc task..."`

## Pre-Task: Load Context

**Read these files FIRST:**
1. `.arc/PROJECT.md` - Maintain vision alignment
2. `.arc/CONTRACTS.md` - Follow existing conventions
3. `.arc/STATE.md` - Avoid conflicts

## Process

1. Understand what needs to be done
2. Ask 1-2 clarifying questions ONLY if absolutely necessary
3. Do the task immediately
4. **If you create/modify something shared:**
   - Update CONTRACTS.md
   - Add to Update Log
5. Show results
6. Git commit: `chore: [brief description]`
7. Update `.arc/STATE.md` → append to "Recent Quick Tasks"

## Use For

- Text changes
- Color tweaks  
- Small bug fixes
- Config updates
- Adding comments
- Renaming things

## NOT For

- New features (use `/arc-plan` instead)
- Complex logic changes
- Multi-file refactors
- New API endpoints
