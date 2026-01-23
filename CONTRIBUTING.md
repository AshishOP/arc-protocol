# Contributing to ARC Protocol

We welcome contributions to make the ARC Protocol the most disciplined and powerful AI workflow system in the world.

## 🛠️ How You Can Help

### 1. Adding New Skills
The heart of ARC's subagents is the Skill System. You can contribute by adding new experts to `.agent/skills/definitions/`.
- **Requirement:** Keep the context low (aim for ~500 tokens for the definition).
- **Format:** Use Markdown with clear "Behavior Rules" and "Focus Areas".

### 2. Refining Workflows
If you find a slash command (e.g., `/arc-plan`) that loses context or needs better instructions, edit the files in `.agent/workflows/`.

### 3. Improving the Dashboard
The dashboard is built with **Textual** and **Rich**. Feel free to suggest better layouts, colors, or new metrics.

## 📜 Principles
- **Context First:** Every change must respect the "Load All Context" rule.
- **Single Source of Truth:** Never hardcode data that should live in `.arc/CONTRACTS.md`.
- **Concurrency Safety:** If modifying the state update logic, always use the `fcntl` locking mechanism built into `background_agent.py`.

## 🚀 Setup for Development
1. Clone the repo.
2. Create a venv: `python3 -m venv venv`.
3. Install dependencies: `./venv/bin/pip install rich textual google-generativeai`.
4. Run the dashboard: `./dash`.

---
Thank you for helping us build the future of agentic engineering!
