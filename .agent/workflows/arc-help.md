---
description: Show help and available ARC commands
---

# ARC Workflow Commands & System Guide

## Core Workflow (in order)

| Command | Purpose |
|---------|---------|
| `/arc-new` | Initialize a new project (defines goals, creates roadmap) |
| `/arc-discuss` | Capture preferences before planning a phase (optional) |
| `/arc-plan` | Create detailed task plan for a phase |
| `/arc-execute` | Execute the plan, task by task (can delegate to subagents) |
| `/arc-verify` | Verify the completed phase works |

## Session & Roadmap Management

| Command | Purpose |
|---------|---------|
| `/arc-pause` | Save session state before leaving |
| `/arc-resume` | Load context when starting a new session |
| `/arc-status` | Quick view of current progress |
| `/arc-add-phase` | Insert a new phase into the roadmap |

## Advanced Orchestration (Multi-Agent)

| Command | Purpose |
|---------|---------|
| `/arc-quick` | Small ad-hoc tasks outside phase structure |
| `/arc-map` | Analyze existing codebase (brownfield projects) |
| `/arc-multi-agent` | Orchestrate true parallel subagents (Recommended) |
| `/arc-dual-agent` | Coordinate two separate AI instances (Advanced) |
| `/arc-health` | Check ARC system health and configuration |

## The Multi-Agent System

ARC v2.1 introduces **True Parallelism** with specialized subagents.

### Key Concepts:
- **Orchestrator (Main AI):** Manages the workflow, makes strategic decisions, and delegates tasks.
- **Subagents (Workers):** Background processes executing tactical tasks (Researcher, Coder, Auditor, Architect, Debugger).
- **Dashboard:** A Textual TUI to monitor all agents in real-time.
- **Model:** Subagents use the `flash` model (recommended for speed and quota efficiency).

## Typical Flow

```
New Project:     /arc-new → /arc-plan → /arc-execute → /arc-verify
With Discuss:    /arc-new → /arc-discuss → /arc-plan → /arc-execute → /arc-verify
Existing Code:   /arc-map → /arc-new → /arc-plan → /arc-execute → /arc-verify
New Session:     /arc-resume → continue where you left off
End of Day:      /arc-pause
```

## Key Files (Single Source of Truth)

| File | Purpose |
|------|---------|
| `.arc/PROJECT.md` | Vision, goals, constraints |
| `.arc/ROADMAP.md` | Phases and progress |
| `.arc/STATE.md` | Current session state |
| `.arc/CONTRACTS.md` | Shared definitions (APIs, models) |
| `.arc/CODEBASE.md` | Existing codebase map (brownfield) |

## Tips

- Always run `/arc-pause` before ending a session.
- Use `/arc-quick` for small fixes, not new features.
- `/arc-discuss` is optional but helps with UI-heavy phases.
- Check `CONTRACTS.md` before adding new endpoints or models.
- **Delegate tactical tasks** to subagents using `arc_spawn_agent` via the Orchestrator.
- Keep the dashboard (`./dash`) open in a separate terminal.
