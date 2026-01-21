---
description: Save session state before leaving
---

I'm pausing work. Save the current state.

0. **Dashboard Update**:
   - Run `./venv/bin/python3 .agent/dashboard/update.py main_status="PAUSED" main_action="Saving Session State" log="Session state archived."`

Create/update .arc/STATE.md with:

## Last Updated
[Current date/time]

## Current Position
- Phase: [N]
- Task: [Current task number and name, or "between tasks"]
- Status: [In progress / blocked / waiting / complete]

## What I Was Doing
[Clear description of current work - be specific]

## Next Steps
[Exactly what to do when I return]

## Decisions Made This Session
[Any technical choices made today]

## Blockers
[Anything preventing progress]

## Files Changed
[List of files modified this session]

## Context For Next Session
[Anything future-me or a new AI session needs to know]

Make it detailed enough that I (or you in a new session) can pick up exactly where I left off.
