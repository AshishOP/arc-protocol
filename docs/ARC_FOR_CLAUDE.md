# 🪄 ARC for ClaudeCode

ClaudeCode is a powerful CLI-based agent. By integrating the ARC Protocol, you give Claude the ability to perform background tasks while you continue your conversation.

---

## 1. Prerequisites
- **ClaudeCode CLI installed.**
- **Gemini CLI installed:** `npm install -g @google/generative-ai`
- **Authenticated:** `gemini login`

---

## 2. Setting up the MCP Server
ClaudeCode uses a global or project-based MCP configuration.

### **Step-by-Step Configuration:**
1. Open your ClaudeCode settings or the global `claude_desktop_config.json` (or equivalent for CLI).
2. Add the `arc-bridge` entry:

```json
{
  "mcpServers": {
    "arc-bridge": {
      "command": "python3",
      "args": ["/home/ashish/Desktop/antigravity_ai/.agent/mcp/arc_mcp_server.py"],
      "env": {
        "GEMINI_MODEL": "flash"
      }
    }
  }
}
```

---

## 3. Workflow Integration
Since ClaudeCode uses a text-heavy interface, the structure provided by the `.arc/` folder is essential to prevent context drift.

### **Strategy for ClaudeCode:**
- **Explicit Instruction:** Since ClaudeCode doesn't have "Slash Command" UI buttons like some IDEs, you should use the file paths directly:
  > *"Claude, follow the workflow in .agent/workflows/arc-plan.md to architect Task 1."*
- **Bridge Spawning:** Claude can use the `arc_spawn_agent` tool provided by the bridge to send tasks to Gemini. 

---

## 4. Why use ARC with Claude?
Claude has exceptional reasoning (3.5 Sonnet / 3 Opus), but it is a **single-process agent**. By using ARC, Claude becomes the **Manager**.
- Claude handles the **complex architecture**.
- Gemini (via the bridge) handles the **boilerplate and research**.
- This keeps Claude's tokens focused on the hard logic.

---
*ARC Protocol v2.0 - Bringing Parallelism to ClaudeCode.*
