# Output from Alpha (Skill: researcher)

**Task:** Test

**Model:** default

---

# 🧪 Research Test Result: ARC Protocol Context

## TL;DR
The current directory contains the **ARC Protocol** (Analyze. Run. Confirm.), a framework designed to enforce structured, context-aware workflows for AI-assisted software development. It moves beyond stateless chat by introducing persistent context, defined roles (Architect, Executor, Reviewer), and a "Contract" system.

## 📂 Project Structure Analysis

| Directory/File | Purpose |
| :--- | :--- |
| **`.arc/`** | The "Brain" of the project. Stores persistent state (`STATE.md`), contracts (`CONTRACTS.md`), project vision (`PROJECT.md`), and planning documents. |
| **`.agent/`** | The "Engine". Contains workflow definitions (`workflows/`), dashboard logic (`dashboard/`), and specialized skills (`skills/`). |
| **`README.md`** | Primary documentation explaining the philosophy: **Analyze** (Architect), **Run** (Executor), **Confirm** (Reviewer). |
| **`CLAUDE.md`** | Specific instructions for AI agents (like Claude/Gemini) to integrate with the ARC dashboard and follow protocol rules. |

## 🔑 Key Concepts

1.  **State Management**: Unlike standard AI sessions, ARC persists context across sessions using `.arc/STATE.md` and `.arc/planning/ROADMAP.md`.
2.  **Contract-First**: A shared `CONTRACTS.md` file acts as the single source of truth for APIs, schemas, and conventions to prevent drift.
3.  **Roles**:
    *   **Architect**: Designs plans and contracts.
    *   **Executor**: Implements atomic tasks.
    *   **Reviewer**: Audits work against the contract.
4.  **Dashboard**: A real-time CLI dashboard (`.agent/dashboard/`) tracks agent "thoughts" and status.

## 🛠️ Actionable Next Steps (How-To)

*   **Start a New Project**: Run `/arc-new`.
*   **Map Existing Code**: Run `/arc-map` (useful for "brownfield" projects).
*   **Plan a Phase**: Run `/arc-plan`.
*   **Execute Tasks**: Run `/arc-execute`.

**Status**: Research capability verified. Context loaded.