# 🚀 The ARC Protocol v2.0

```text
   █████╗ ██████╗  ██████╗ 
  ██╔══██╗██╔══██╗██╔════╝ 
  ███████║██████╔╝██║      
  ██╔══██║██╔══██╗██║      
  ██║  ██║██║  ██║╚██████╗ 
  ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ 
   ANALYZE. RUN. CONFIRM.
```

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Workflow](https://img.shields.io/badge/Workflow-Parallel-success)](.agent/workflows/)
[![Interface](https://img.shields.io/badge/Interface-Textual%20TUI-orange)](#-interactive-dashboard)

> **The first high-discipline, parallel agentic workflow for AI engineers.** 
> ARC transforms your AI from a stateless chatbot into a structured **Autonomous Engineering Team**.

---

## 🧠 Why ARC?

Standard AI chats are **stateless and chaotic**. The AI forgets context, violates standards, and breaks builds because it lacks a persistent "Neural Architecture." 

**ARC v2.0 solves this by introducing the Orchestrator-Worker model:**
*   **The Orchestrator (Cortex):** The high-reasoning Main Agent (you + your primary AI) who plans and decides.
*   **The Subagents (Workers):** Specialized background processes that execute tactical tasks in parallel using the `flash` model.

---

## 🖥️ Interactive TUI Dashboard

ARC features a professional terminal-based dashboard built with **Textual**. It gives you a "NASA-style" view of your entire AI fleet.

### ✨ Key Features:
- **Live Ticking Clock:** Track exactly how long a development phase takes.
- **Interactive Command Box:** Run system commands like `/clean` or `/help` directly in the UI.
- **Native Scrolling:** Use your mouse wheel or trackpad to browse 500+ lines of log history.
- **Hyperlinked Files:** Click on generated reports in the log to open them instantly in your editor.
- **Rainbow Fleet:** Visual tracking of 5 specialized skills with distinct color identities.

---

## 🛠️ The Specialized Fleet

ARC uses 5 distinct subagents, each optimized for a specific engineering role:

| Agent | Color | Skill | Primary Goal |
| :--- | :--- | :--- | :--- |
| **Alpha** | 🟣 | `Researcher` | Gathers info, reads documentation, summarizes intent. |
| **Beta** | 🟢 | `Coder` | Implements logic and follows `.arc/CONTRACTS.md` strictly. |
| **Gamma** | 🔴 | `Auditor` | Scans for security flaws, bugs, and naming violations. |
| **Delta** | 🔵 | `Architect` | Designs file structures and system data flows. |
| **Epsilon**| 🟡 | `Debugger` | Analyzes stack traces and identifies root causes. |

---

## 🛡️ The "Rule of Two" (Performance)

To ensure stability and respect API quotas, ARC enforces the **Rule of Two**:
1.  **1 Orchestrator** (Primary Brain).
2.  **Max 2 Subagents** active simultaneously.

All agents are optimized for a **2500-token context window**, ensuring they stay fast, accurate, and cheap.

---

## 🌉 The ARC Bridge (MCP Server)

The project includes a built-in **Model Context Protocol (MCP)** server. This acts as the "Nervous System," connecting the AI to your local machine.

- **`arc_spawn_agent`**: Launches parallel sub-processes.
- **`arc_read_file` / `arc_write_file`**: Unified, safe file access.
- **`arc_update_dashboard`**: Real-time visualization sync.

---

## 🛠️ One-Click Installation

Choose the command for your system to initialize the ARC environment:

| Platform | Command |
| :--- | :--- |
| **Bash / Zsh / Mac / WSL** | `bash install.sh` |
| **Windows PowerShell** | `powershell ./install.ps1` |
| **Fish Shell** | `fish install.fish` |
| **Universal (Python)** | `python install_arc.py` |

---

## ⚡ Quick Start Guide

### 1. The Core Files (The Brain)
ARC relies on four Markdown files in your `.arc/` folder as the "Single Source of Truth":
- `PROJECT.md`: The Vision.
- `ROADMAP.md`: The Plan.
- `CONTRACTS.md`: The Rules (APIs, naming, etc).
- `STATE.md`: The Current Progress.

### 2. Complete Workflow Commands
Run these slash commands in your AI side-bar to drive the workflow:

| Command | Action | Output / Goal |
| :--- | :--- | :--- |
| `/arc-new` | **Initialize** | Define project vision and create roadmap. |
| `/arc-map` | **Discover** | Sync ARC with an existing codebase. |
| `/arc-discuss` | **Capture** | Preferences and technical decisions for a phase. |
| `/arc-plan` | **Architect** | Create a detailed task-by-task execution plan. |
| `/arc-execute` | **Build** | Launch parallel subagents to implement code. |
| `/arc-verify` | **Audit** | Final QA, syntax check, and contract verification. |
| `/arc-quick` | **Patch** | Handle small ad-hoc tasks outside the roadmap. |
| `/arc-multi-agent`| **Orchestrator** | Manage complex parallel subagent workflows. |
| `/arc-dual-agent` | **Collaboration**| Sync two separate AI instances for heavy-duty dev. |
| `/arc-add-phase` | **Expand** | Insert new phases into an existing roadmap. |
| `/arc-status` | **Report** | Get a summary of current project progress. |
| `/arc-health` | **Diagnostics** | Verify system configuration and API health. |
| `/arc-pause` | **Snapshot** | Save session state before exiting. |
| `/arc-resume` | **Restore** | Load state and context from a previous session. |
| `/arc-help` | **Guidance** | List all available commands and best practices. |

### 3. Monitoring
Keep your dashboard open in a separate terminal to watch the magic happen:
```bash
./dash
```

---

## 📜 License
MIT — Created by Ashish. Optimized for the next generation of AI-assisted engineering.

## 🚀 Deployment Checklist for New Users

Copy these files/folders into any new project repo (keep at root):
- `.arc/` (all templates and state management)
- `.agent/` (workflows, dashboard, tools, bridge, skills)
- Optional: `venv/` with `rich` installed for the Textual dashboard
- Optional: root install scripts (`install.sh`, `install.ps1`, `install_arc.py`)

### Initial Setup in New Project
1. Copy the files above.
2. Run `python install_arc.py` (or platform script) to ensure dependencies.
3. Start the dashboard: `./dash`
4. Run `/arc-new` to initialize your project.
5. Continue with `/arc-plan` → `/arc-execute` → `/arc-verify`.

### What You Don't Need to Copy
- Any `src/`, `planning/`, `archive/`, or generated per‑project files. ARC creates these automatically when you start a new project.

---
*Inspired by Get Shit Done and RALPH Loop. Re-engineered for parallel agentic autonomy.*
