---
description: Orchestrate multiple Antigravity agents for complex feature development  
---

# ARC Dual-Agent Mode

**TRUE multi-agent** using two separate Antigravity instances that coordinate through shared files.

## Prerequisites

You need TWO terminals/VS Code windows with Antigravity running:
- **Terminal 1**: Architect Agent (planning, design, review)
- **Terminal 2**: Executor Agent (implementation, testing)

## Setup

### 1. Start the Bridge Server (in project root)
```bash
python3 .agent/bridge/server.py &
```

### 2. Open Two Antigravity Instances
- Open VS Code in the project folder
- Open a SECOND VS Code window in the same project
- Both will share the `.arc/` directory

### 3. Initialize Both Agents
In Terminal 1 (Architect), say:
> I am the ARCHITECT agent. I will plan phases and write to .arc/planning/. When I'm done planning, I'll update arc_workflow_state.json with status "READY_FOR_EXECUTOR".

In Terminal 2 (Executor), say:
> I am the EXECUTOR agent. I will watch for plans in .arc/planning/ and implement them. I'll check arc_workflow_state.json for the "READY_FOR_EXECUTOR" signal.

## Coordination Protocol

### Step 1: Architect Plans
```
ARCHITECT writes:
  .arc/planning/phase-N-PLAN.md
  .arc/planning/phase-N-CONTEXT.md

ARCHITECT updates state:
  arc_update_dashboard agent="Architect" status="DONE" task="Plan ready for Executor"
  
ARCHITECT writes signal:
  echo '{"executor_signal": "START", "phase": N}' > .arc/state/executor_signal.json
```

### Step 2: Executor Implements
```
EXECUTOR reads:
  .arc/state/executor_signal.json
  .arc/planning/phase-N-PLAN.md

EXECUTOR updates state:
  arc_update_dashboard agent="Executor" status="WORKING" task="Implementing phase N"

EXECUTOR implements each task, then:
  arc_update_dashboard agent="Executor" status="DONE" task="Phase N complete"
  echo '{"reviewer_signal": "REVIEW", "phase": N}' > .arc/state/reviewer_signal.json
```

### Step 3: Review (Architect or Third Agent)
```
ARCHITECT/REVIEWER reads:
  .arc/state/reviewer_signal.json

Reviews the changes, writes:
  .arc/planning/phase-N-VERIFICATION.md
```

## Dashboard Visualization

Both agents update the same dashboard, so you can run `./dash` to see:
- Architect status
- Executor status
- Logs from both agents

## Communication Signals

| File | Meaning |
|------|---------|
| `.arc/state/executor_signal.json` | Architect → Executor |
| `.arc/state/reviewer_signal.json` | Executor → Reviewer |
| `.arc/state/architect_signal.json` | Reviewer → Architect |

## Example Session

**Architect (Terminal 1):**
```
You: Plan phase 1 - user authentication
AI: [Creates .arc/planning/phase-1-PLAN.md]
    [Updates dashboard: Architect=DONE]
    [Writes executor_signal.json: START phase 1]
```

**Executor (Terminal 2):**
```
You: Check for work
AI: [Reads executor_signal.json - sees START]
    [Reads phase-1-PLAN.md]
    [Implements tasks one by one]
    [Updates dashboard: Executor=DONE]
```

## Why This Works

- Both instances have FULL tool access (file, terminal, MCP)
- They coordinate through shared files
- Dashboard shows both agents' status
- No browser overhead
- TRUE parallel execution possible

## Tips

1. **Keep both agents focused** - Architect only plans, Executor only implements
2. **Use clear signals** - Always write signal files when handing off
3. **Monitor dashboard** - Run `./dash` in a third terminal
4. **Git frequently** - Both agents should commit their work
