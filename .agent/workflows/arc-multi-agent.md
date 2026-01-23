---
description: Orchestrate true parallel subagents using the ARC Bridge
---

# ARC Multi-Agent Orchestration (Parallel Mode)

> **Modern ARC Architecture:** Unlike sequential AI chats, this system uses **True Parallel Processes**. The Main Agent acts as the **Orchestrator (Cortex)**, spawning specialized sub-processes to handle tactical tasks.

## 🛡️ The Rule of Two
To avoid API rate limits and context fragmentation, follow the **Rule of Two**:
- **1 Main Agent** (Orchestrator - high reasoning)
- **Max 2 Subagents** (Workers - tactical/fast)

## 0. Dashboard Initialization
- Ensure `./dash` is running in a separate terminal.
- Run `update.py` to set the project and phase.

## 1. Task Decomposition (Orchestration)
- Before coding, look at the task list.
- **Categorize Tasks:**
    - *Strategic:* Architecture, logic flows, complex bugs (Keep for Main Agent).
    - *Tactical:* Researching docs, writing boilerplate, auditing syntax (Delegate).

## 2. Delegation (The Dispatch)
- Use the `arc_spawn_agent` tool.
- **Assign Skill:** Choose from `researcher`, `coder`, `auditor`, `architect`, `debugger`.
- **Set Model:** Use `flash` for subagents to maximize speed and quota.
- **Context Injection:** Subagents will automatically read `PROJECT.md` and `CONTRACTS.md` based on their skill.

## 3. Parallel Execution
- While the Subagent is working (visible as `WORKING` on the dashboard), the Main Agent continues with strategic tasks.
- **DO NOT** block your chat waiting for the subagent. Keep building.

## 4. Result Aggregation
- Monitor the dashboard. When an agent turns `DONE`:
    1.  Read the resulting log file in `.arc/archive/subagent_logs/`.
    2.  Verify the work.
    3.  Integrate the results into the main codebase.
    4.  Update `.arc/CONTRACTS.md` if necessary.

## 5. Final Confirmation
- Once all bots and the orchestrator finish, run `/arc-verify` to ensure the system is stable.