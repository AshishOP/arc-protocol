# 🚀 The ARC Protocol

```text
    ___     ____     ______
   /   |   / __ \   / ____/
  / /| |  / /_/ /  / /     
 / ___ | / _, _/  / /___   
/_/  |_|/_/ |_|   \____/   
                           
   ANALYZE. RUN. CONFIRM.
```

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Multi-AI Support](https://img.shields.io/badge/AI-Antigravity%20%7C%20Claude-blueviolet)](CLAUDE.md)
[![Workflow](https://img.shields.io/badge/Workflow-Ready-success)](.arc/templates/)
[![Stars](https://img.shields.io/github/stars/AshishOP/arc-protocol?style=social)](https://github.com/AshishOP/arc-protocol)

> A high-discipline, agentic workflow system for AI-assisted development.

---

## 🧠 Why ARC?

Standard AI chats are **stateless and chaotic**. You ask for a feature, the AI writes some code, forgets the context 10 minutes later, and eventually breaks your production build because it forgot the "Contract" established 3 sessions ago.

**ARC solves this by enforcing a Neural Architecture on your development loop:**

1.  **Analyze (Architect)**: No code is written until the "Contract" is defined.
2.  **Run (Executor)**: Code is implemented in atomic, verifiable tasks.
3.  **Confirm (Reviewer)**: Every change is audited against the project state.

## 📊 Real-time Trajectory Tracking

Unlike standard logs, ARC provides a **Live Dashboard** that shows you exactly what the "Brain" (Main Agent) and the "Trajectory Workers" (Subagents) are doing in real-time.

---

## 🚀 What is ARC?

ARC is a context-engineered, spec-driven development framework. It transforms the AI from a simple code generator into a structured **Autonomous Agent Suite** with three specialized roles:

- **Architect (Analyze)**: Designs the plan, identifies edge cases, and enforces technical standards.
- **Executor (Run)**: Implements the code task-by-task, following the Architect's blueprint.
- **Reviewer (Confirm)**: Verifies the work against requirements and ensures codebase integrity.

## ✨ Features

- 🎯 **No Scope Creep**: Clear transitions between Discussion, Planning, and Execution.
- 🧠 **Infinite Context**: Persistent state files (`STATE.md`) allow agents to resume work across sessions without loss of intent.
- 🔧 **Contract-First Design**: Shared definitions (`CONTRACTS.md`) ensure consistency across APIs, schemas, and UI components.
- 📊 **Real-time Trajectory Dashboard**: A live CLI dashboard to track subagent thoughts, actions, and progress.
- 🛡️ **Skill Integration**: Optimized for tactical skills like performance, security, and rendering efficiency.

Inspired by [Get Shit Done](https://github.com/glittercowboy/get-shit-done) and [RALPH Loop](https://github.com/frankbria/ralph-claude-code), re-engineered for agentic autonomy.

## Quick Start

### New Project (Greenfield)
```
/arc-new          → Define project, create roadmap
/arc-discuss      → Capture preferences for a phase (optional)
/arc-plan         → Create detailed task plan
/arc-execute      → Build it, task by task
/arc-verify       → Confirm it works
```

### Existing Project (Brownfield)
```
/arc-map          → Analyze existing codebase first
/arc-new          → Define what you're adding
...continue as above
```

### Session Management
```
/arc-pause        → Save state before leaving
/arc-resume       → Load context when returning
/arc-status       → See current progress
```

### Quick Tasks
```
/arc-quick        → Small fixes outside the phase structure
```

### Roadmap Changes
```
/arc-add-phase    → Insert a new phase into roadmap
```

## File Structure

```
.arc/
├── PROJECT.md           # What you're building (vision, goals, constraints)
├── ROADMAP.md           # Phases and progress
├── STATE.md             # Current session state (for pause/resume)
├── CONTRACTS.md         # Shared definitions (APIs, models, conventions)
├── CODEBASE.md          # Existing codebase map (brownfield only)
├── planning/
│   ├── phase-1-CONTEXT.md   # Preferences from discuss phase
│   ├── phase-1-PLAN.md      # Detailed task plan
│   └── phase-1-SUMMARY.md   # Completion record
├── archive/             # Completed phase plans
├── state/               # State snapshots
└── templates/           # Templates for all document types
    ├── PROJECT.md
    ├── CONTRACTS.md
    ├── CONTEXT.md
    ├── PHASE-PLAN.md
    ├── PHASE-SUMMARY.md
    ├── CODEBASE.md
    └── VERIFICATION.md

.agent/
└── workflows/           # Antigravity workflow definitions
    ├── arc-new.md
    ├── arc-discuss.md
    ├── arc-plan.md
    ├── arc-execute.md
    ├── arc-verify.md
    ├── arc-pause.md
    ├── arc-resume.md
    ├── arc-status.md
    ├── arc-quick.md
    ├── arc-add-phase.md
    └── arc-map.md
```

## Workflow Commands

| Command | When to Use | Creates/Updates |
|---------|-------------|-----------------|
| `/arc-new` | Starting a new project | PROJECT.md, ROADMAP.md |
| `/arc-map` | Before modifying existing code | CODEBASE.md, CONTRACTS.md |
| `/arc-discuss` | Before planning, to capture preferences | phase-N-CONTEXT.md |
| `/arc-plan` | Ready to plan a phase | phase-N-PLAN.md |
| `/arc-add-phase` | Need to insert a new phase | ROADMAP.md |
| `/arc-execute` | Ready to build | Code, CONTRACTS.md, STATE.md |
| `/arc-verify` | After execution, test it works | phase-N-VERIFICATION.md |
| `/arc-pause` | Leaving for the day | STATE.md |
| `/arc-resume` | Starting a new session | Loads all context |
| `/arc-status` | Quick progress check | Nothing, just reports |
| `/arc-quick` | Small ad-hoc tasks | Code, CONTRACTS.md |

## The Contract System

`CONTRACTS.md` is the **single source of truth** for everything shared:

- API endpoints and their request/response formats
- Data models and schemas
- Environment variables
- Naming conventions
- Design tokens and colors
- Component props

**Rule:** If you CREATE something another part uses, add it to CONTRACTS.md immediately.

## Typical Workflow

```
Day 1 Morning:
  /arc-new              → Define Authent8, create 5-phase roadmap

Day 1 Afternoon:  
  /arc-discuss          → Discuss Phase 1 preferences
  /arc-plan             → Plan Phase 1 (Backend API)
  /arc-execute          → Build it
  /arc-verify           → Test it works
  /arc-pause            → Save state, take a break

Day 1 Evening:
  /arc-resume           → Load context
  /arc-plan             → Plan Phase 2 (Frontend)
  /arc-execute          → Build it
  ...

Mid-project realization:
  /arc-add-phase        → Insert "Authentication" phase
  /arc-plan             → Plan the new phase
  ...
```

## Why This Works

1. **Context never rots** — Each workflow loads exactly what it needs
2. **Decisions persist** — CONTRACTS.md and CONTEXT.md survive session resets
3. **Progress is visible** — ROADMAP.md and STATE.md show where you are
4. **Focus is maintained** — One task at a time, one phase at a time
5. **Nothing is guessed** — Discuss phase captures preferences before planning

## 🛠️ Installation & Setup

1. **One-Click Install**:
   Run the following command in your project root to initialize ARC:
   ```bash
   curl -sSL https://raw.githubusercontent.com/[your-repo]/main/setup.sh | bash
   ```

2. **Manual Setup**:
   - Copy the `.arc/` and `.agent/` folders to your project.
   - Run `python3 .agent/dashboard/setup_dashboard.py` to prepare the environment.

3. **Start Building**:
   Run `/arc-new` to define your project roadmap.

## 🤖 Multi-AI Support

ARC is designed to be the bridge between different AI agents:

- **Antigravity**: Full native support via Slash Commands (`/arc-plan`, etc.) and trajectory tracking.
- **Claude Code**: Native support via `CLAUDE.md`. Claude will automatically follow the ARC protocols, update the dashboard, and respect project contracts.
- **Other Agents**: Manual adherence to the `.agent/workflows/` allows any LLM-based agent to maintain high context and project integrity.

## Comparison to Other Systems

| Feature | ARC Protocol | GetShitDone | RALPH Loop |
|---------|----------|--------------|------------|
| Multi-AI (Claude/Antigravity) | ✅ Native | ❌ No | ❌ No |
| Real-time Dashboard | ✅ Yes (CLI) | ❌ No | ❌ No |
| Contract tracking | ✅ Comprehensive | ❌ None | ❌ None |
| Session continuity | ✅ STATE.md | ✅ STATE.md | ✅ tmux |
| Discuss phase | ✅ Yes | ✅ Yes | ❌ No |

## License

MIT — Use it, adapt it, share it.

## Credits

- Inspired by [Get Shit Done](https://github.com/glittercowboy/get-shit-done) by glittercowboy
- Inspired by [RALPH Loop](https://github.com/frankbria/ralph-claude-code) by frankbria
- Adapted for Antigravity by you!
