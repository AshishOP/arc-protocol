# How ARC Actually Works

This document breaks down the moving parts of the ARC Protocol. It's written for engineers who want to know what's happening under the hood when they type a command.

---

## 🏗️ 1. The Architecture (What & Why)

We built ARC to solve **Context Rot**.

In a long coding session, LLMs eventually degrade—they forget your file structure, hallucinate variable names, or get "lazy." This is unavoidable because context windows are finite and "Lost in the Middle" syndrome is real.

** The ARC Solution: Fresh Processes**
Instead of stuffing everything into one chat, ARC spawns **Background Subagents** for every task.
*   **Main Chat:** Handles strategy.
*   **Subagent:** Spawns with a *fresh, empty context*, reads *only* the specific files it needs (`CONTRACTS.md`, `TASK_FILE`), does the job, and dies.

This ensures that the 100th task is done with the same precision as the 1st task.

**The Stack:**
*   **Python (3.10+):** Runs the dashboard and the bridge. It's stable, cross-platform, and handles subprocesses well.
*   **Gemini CLI:** Google's official CLI tool. We use this because it handles authentication securely (OAuth) without us needing to manage your API keys.
*   **MCP (Model Context Protocol):** The standard way to connect LLMs to your file system.

## 🎛️ 2. Workflow Commands

Think of these as "Macros" for your development process. Instead of typing a 500-word prompt every time, you use these triggers.

### The Phases
*   **`/arc-new`**: **Start Here.** Use this to initialize a project. It asks you "What are we building?" and creates the `PROJECT.md` vision file.
*   **`/arc-plan`**: **The Architect (Solution Design).**
    *   It does NOT write code.
    *   It reads `CONTRACTS.md` and decides *function signatures*, *data models*, and *integration points*.
    *   It produces a detailed technical plan that acts as a blueprint for the "Coder" agents. This prevents logic hallucinations.
*   **`/arc-execute`**: **The Engine.** Takes that plan and starts running it. This is where you see agents spawning in the dashboard.
*   **`/arc-verify`**: **The Quality Check.** Runs after execution to ensure the code actually works.

### The Helpers
*   **`/arc-discuss`**: Use this if you are unsure about a design choice (e.g., "Should we use NextAuth or Clerk?"). It captures your preferences before planning.
*   **`/arc-map`**: **For Existing Projects.** Scans your current folder and creates a "Neural Map" of your codebase. Essential for brownfield work.
*   **`/arc-quick`**: For small fixes (e.g., "Change the button color"). Skips the heavy planning phase.

## 🔧 3. Under the Hood: MCP & Gemini

How does the AI actually touch your files?

1.  **The Bridge (`arc_mcp_server.py`)**: This script runs silently in the background. It listens for JSON commands like `read_file` or `write_file`.
2.  **The Subagents**: When you (or the Orchestrator) say "Spawn a Researcher," the Bridge launches a **brand new Python process**.
3.  **The Execution**: This new process (`background_agent.py`) loads the specific skill prompt (e.g., "You act as a Researcher...") and pipes your request to the **Gemini CLI**.
4.  **The Result**: The CLI streams the answer back, and the subagent saves it to an `.md` file in `.arc/archive/`.

**Why this matters:** Because the subagent is a *separate process*, it doesn't block your main chat. You can keep talking while it works.

## 📂 4. Folder Structure (Where things live)

When you install ARC, we add two folders to your project:

### `.agent/` ( The Engine )
*   **Don't touch these files** unless you are hacking the protocol itself.
*   Contains the dashboard logic, the MCP server, and the tool scripts.

## 4. The File Ecosystem (Your Context)

Every file in `.arc/` has a specific job in preventing Context Rot.

| File | Purpose | When it's read |
| :--- | :--- | :--- |
| `PROJECT.md` | The Vision. Goals, constraints, and "North Star". | Every session start. |
| `CONTRACTS.md` | The Law. API shapes, Types, Zod schemas, DB models. | Before ANY code is written. |
| `ROADMAP.md` | The Path. All phases, current status. | When running `/arc-plan`. |
| `STATE.md` | The Scratchpad. Current session memory. | Updated every chat turn. |
| `CODEBASE.md` | The Map. Directory structure and patterns. | Created by `/arc-map`. |
| `planning/*.md` | The Tactics. Atomic plans for subagents. | During execution. |


## 🚀 5. Starting a NEW Project

1.  **Install:** Run `python3 setup_arc.py` in an empty folder.
2.  **Authenticate:** Run `gemini login` in your terminal.
3.  **Launch Dash:** Run `./dash` in a separate terminal window.
4.  **Initialize:** In your AI chat, type:
    > "I want to start a new project. Run `/arc-new`."
5.  **Follow the flow:** The AI will ask you what you want to build. Answer honestly. Then run `/arc-plan` -> `/arc-execute`.

## 🦅 6. Integrating into an EXISTING Project

If you already have a 50,000 line codebase, **don't just run `/arc-new`**. You need to map the territory first.

1.  **Install:** Copy the ARC folders in (using `setup_arc.py`).
2.  **Map it:** Run this command first:
    > "Run `/arc-map` to analyze my current project structure."
3.  **Wait:** The agent will scan your files and build a `CODEBASE.md`.
4.  **Plan:** Now you can ask it to refactor or add features using the existing patterns it found.

## 7. Troubleshooting Hallucinations

AI agents sometimes make things up. Here is how ARC prevents that, and what you should watch for:

*   **"File Not Found":** The AI often forgets that it is running inside the project root. If it tries to access `../foo.txt`, it will fail. **Rule:** All paths in ARC are relative to the project root (e.g., `.arc/STATE.md`).
*   **"Contract Violation":** If the AI writes code that clashes with `CONTRACTS.md`, the audit step will catch it. Run `/arc-verify` to force a check.
*   **"Skill Not Found":** If the dashboard shows an agent spawned as `general` when you wanted `coder`, check that you didn't invent a new role name. Stick to: `researcher`, `coder`, `auditor`.

## 8. Operational Realities

ARC is not magic. It imposes structure. By forcing agents to read `CONTRACTS.md` before writing code, we eliminate the most common source of bugs: **Context Amnesia**.

**Where it still fails:**
1.  **Ghost Libraries:** It might try to import a library version you don't feature.
2.  **Logic Bugs:** The *code* will run, but the *logic* (e.g., an infinite loop) might still be flawed. The Linter checks for structure, not runtime logic.
3.  **Context Clutter:** If your `CONTRACTS.md` grows to 5000+ lines, the AI might start ignoring rules in the middle. Keep your contracts clean.

**Conclusion:** ARC is a **Manager**, not a Miracle Worker. You still need to verify the output.

