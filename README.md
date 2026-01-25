# ARC Protocol v2.1 (Technical Preview)

```text
   █████╗ ██████╗  ██████╗ 
  ██╔══██╗██╔══██╗██╔════╝ 
  ███████║██████╔╝██║      
  ██╔══██║██╔══██╗██║      
  ██║  ██║██║  ██║╚██████╗ 
  ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ 
   ANALYZE. RUN. CONFIRM.
```

> **Why I Built This:**
> I'm a developer, not a "Prompt Engineer." I got tired of AI writing code that broke two days later because it forgot my file structure.
>
> Other tools try to be "Magic Employees" that run your whole company. ARC is different. It's a **Managed Context Protocol**. It forces the AI to check `CONTRACTS.md` before it commits a single line of code. No magic. Just guardrails.

---

## ⚡ Quick Start

### 1. Installation
You need Python 3.10+ and Node.js 18+. No API Key required (we use your Google account).

```bash
# 1. Initialize the environment
python3 setup_arc.py

# 2. Login to Gemini (One time only)
npm install -g @google/generative-ai
gemini login

# 3. Connect your IDE
# Copy the config from docs/INTEGRATIONS.md to your MCP settings.
```
[👉 Comprehensive Integrations Guide](docs/INTEGRATIONS.md)

---

## 🏎️ Tutorial: Build a To-Do App in 5 Minutes

See it in action. Open your AI editor (Claude/Windsurf/Antigravity) and type:

1.  **"Initialize a new project. Run `/arc-new`."**
    *   *AI asks:* "What are we building?"
    *   *You say:* "A simple Python CLI To-Do app."
2.  **"Okay, let's build Phase 1. Run `/arc-plan`."**
    *   *AI acts:* It reads `PROJECT.md`, checks for existing code (none), and drafts a plan: "Create file `todo.py`, Add `add_task` function..."
3.  **"Looks good. Run `/arc-execute`."**
    *   *AI acts:* It spawns background agents. You watch the dashboard.
        *   `Research-Agent` checks `argparse` docs.
        *   `Build-Agent` writes the `.py` file.
        *   `Audit-Agent` checks for PEP8 violations.
4.  **"Verify it works. Run `/arc-verify`."**
    *   *AI acts:* It runs the script and confirms tasks can be added.

**Result:** You have a working app, and you didn't write a single line of code.

---

## 📖 How to Use

### 🆕 Starting a New Project
Don't write code yet. Let the ARC process structure it for you.
1.  Initialize: **`/arc-new`**
2.  Plan the work: **`/arc-plan`**
3.  Build it: **`/arc-execute`**

[👉 Read the full "New Project" Guide](HOW_IT_WORKS.md#-5-starting-a-new-project)

### 🏢 Working on an Existing Codebase
Don't let the AI guess your architecture. Map it first.
1.  Scan the files: **`/arc-map`**
2.  This generates a `CODEBASE_MAP.md` that teaches the agents your style.
3.  Then proceed with planning.

[👉 Read the full "Existing Project" Guide](HOW_IT_WORKS.md#-6-integrating-into-an-existing-project)

### 🤖 The Workflow Commands
We use specific trigger words to switch modes.
*   **`/arc-discuss`**: Brainstorm before you build.
*   **`/arc-quick`**: Fast, one-off tasks.
*   **`/arc-verify`**: Make sure it actually works.

[👉 See all Workflow Commands](HOW_IT_WORKS.md#%EF%B8%8F-2-workflow-commands)

---

## 📂 Documentation
*   **[How It Works (Deep Dive)](HOW_IT_WORKS.md)**: The internal mechanics of MCP and Gemini.
*   **[Contracts & Rules](.arc/CONTRACTS.md)**: How we enforce code quality.

---
*Open Source. MIT License.*
