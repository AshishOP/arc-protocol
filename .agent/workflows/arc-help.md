---
description: Show help and available ARC commands
---

# ARC Workflow Commands

## Core Workflow (in order)

| Command | Purpose |
|---------|---------|
| `/arc-new` | Initialize a new project (defines goals, creates roadmap) |
| `/arc-discuss` | Capture preferences before planning a phase (optional) |
| `/arc-plan` | Create detailed task plan for a phase |
| `/arc-execute` | Execute the plan, task by task |
| `/arc-verify` | Verify the completed phase works |

## Session Management

| Command | Purpose |
|---------|---------|
| `/arc-pause` | Save state before leaving |
| `/arc-resume` | Load context when starting a new session |
| `/arc-status` | Quick view of current progress |

## Roadmap Management

| Command | Purpose |
|---------|---------|
| `/arc-add-phase` | Insert a new phase into the roadmap |

## Special Workflows

| Command | Purpose |
|---------|---------|
| `/arc-map` | Analyze existing codebase (brownfield projects) |
| `/arc-quick` | Small ad-hoc tasks outside phase structure |

## Typical Flow

```
New Project:     /arc-new → /arc-plan → /arc-execute → /arc-verify
With Discuss:    /arc-new → /arc-discuss → /arc-plan → /arc-execute → /arc-verify
Existing Code:   /arc-map → /arc-new → /arc-plan → /arc-execute → /arc-verify
New Session:     /arc-resume → continue where you left off
End of Day:      /arc-pause
```

## Key Files

| File | Purpose |
|------|---------|
| `.arc/PROJECT.md` | Vision, goals, constraints |
| `.arc/ROADMAP.md` | Phases and progress |
| `.arc/STATE.md` | Current session state |
| `.arc/CONTRACTS.md` | Shared definitions (APIs, models) |
| `.arc/CODEBASE.md` | Existing codebase map (brownfield) |

## Tips

- Always run `/arc-pause` before ending a session
- Use `/arc-quick` for small fixes, not new features
- `/arc-discuss` is optional but helps with UI-heavy phases
- Check CONTRACTS.md before adding new endpoints or models
