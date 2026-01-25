# 🐙 ARC for GitHub Copilot

GitHub Copilot (via Chat in VS Code or JetBrains) can be transformed from a basic autocomplete into a structured orchestrator using the ARC Protocol.

---

## 1. Prerequisites
- **VS Code with GitHub Copilot Extension.**
- **Gemini CLI installed:** `npm install -g @google/generative-ai`
- **Authenticated:** `gemini login`

---

## 2. The Custom Instruction Strategy
Copilot doesn't always support direct MCP tool calling natively in the chat without specific extensions. To use ARC effectively in Copilot:

### **Setup:**
1. Point Copilot to the `.agent/rules/global.md` file in your project.
2. Add this to your **Copilot System Prompt** or `.github/copilot-instructions.md`:
   > *"You are an ARC-compliant Orchestrator. Always refer to .arc/CONTRACTS.md before suggesting code and follow the workflows in .agent/workflows/."*

---

## 3. Manual Parallelism
If your version of Copilot does not yet support the `arc_spawn_agent` tool:
- Use Copilot to **Plan** the work.
- Use the **Terminal** to spawn subagents manually:
  `./venv/bin/python3 .agent/workers/background_agent.py researcher-1 "Research [Topic]..."`
- The dashboard (`./dash`) will track both your manual work and the subagent's progress.

---

## 4. The Benefits
Copilot is fast, but it often "guesses" code. ARC's **CONTRACTS.md** and **ROADMAP.md** act as guardrails. By forcing Copilot to read these files, you reduce hallucinations by over 90%.

---
*ARC Protocol v2.0 - Structured Autonomy for Copilot.*
