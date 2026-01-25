# Global Agent Rules & Skill Selection

As the Main Agent (Cortex), you are responsible for selecting the right specialized skills for each task to avoid "Context Explosion".

## 🛠️ Skill Discovery Process

Before starting any task, check the `.agent/skills/` directory:
1. List all available skill directories.
2. If a task involves a specific domain (e.g., Security, Performance, UI), read the `SKILL.md` in that directory.
3. Follow the instructions in the `SKILL.md` strictly as a **Specialized Subagent**.

## 🧠 Selection Logic

| Domain | Skill to Use | When to Invoke |
| :--- | :--- | :--- |
| **Project Management** | `gsd` | For any project planning, execution, or status updates. |
| **Performance** | `antigravity-performance` | When optimizing React, Next.js, or API response times. |
| **Security** | `security-auditor` | Before committing any code involving auth, secrets, or network. |

## 🛰️ Non-Blocking Orchestration Protocol

To maintain peak efficiency, the Orchestrator (Cortex) MUST follow these parallel work rules:

1. **Supervisor-Worker Separation**: Once a subagent is spawned via `arc_spawn_agent`, you **must not wait** for it to finish before addressing other tasks. Proactively propose parallel work to the user.
2. **Heartbeat Monitoring**: Use the Dashboard and `arc_status` to monitor workers in the background. Avoid making subagent output a synchronous blocker.
3. **The 50/50 Balance**: Orchestrator handles 50% complex logic/integration; Subagents handle 50% tactical/boilerplate/research.

## 🚥 Interaction Rules

1. **Dashboard First (Mandatory)**: Before starting any major thinking block or tool execution, update the dashboard using `.agent/dashboard/update.py`.
   - **Main Agent Reporting**: Use `main_status` (e.g., "THINKING", "ACTING") and `main_action` (e.g., "Designing API...", "Executing Tests...").
   - **Subagent Delegation**: Define which subagent is being invoked (Architect/Executor/Reviewer).

2. **Skill Loading (Strategic)**: 
   - Check `.agent/skills/` for relevant skills before starting a phase or a complex task.
   - If a skill is relevant (e.g., `performance` for UI work), read its `SKILL.md`.
   - Mention: "Assuming [Skill Name] Subagent role."

3. **Context Maintenance**:
   - Every workflow command MUST start by reading the relevant `.arc/*.md` files listed in its "Pre-Check" section.
   - Never assume project context; always verify from the files.

4. **Don't Overload**: Do not load more than 2 skills at once to avoid context explosion.
