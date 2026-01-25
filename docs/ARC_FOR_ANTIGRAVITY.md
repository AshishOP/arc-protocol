# 🤖 ARC for Antigravity AI

Antigravity AI is the native home of the ARC Protocol. It is designed to work seamlessly with the parallel execution model and the Textual TUI dashboard.

---

## 1. Prerequisites
- **Antigravity AI installed.**
- **Gemini CLI installed:** `npm install -g @google/generative-ai`
- **Authenticated:** `gemini login`

---

## 2. Setting up the MCP Server
Antigravity automatically detects the `arc-bridge` if configured in your local settings.

### **Configuration (mcp_config.json):**
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

## 3. Workflow Usage
Antigravity follows the strict **Analyse-Run-Confirm** loop. 

### **The Initialization Phase**
Start by running:
`@[/arc-new]`

This will trigger the initialization script which creates your `.arc/` folder with the single source of truth files.

### **The Execution Phase**
When you reach the implementation task, use:
`@[/arc-execute]`

Antigravity will look at the `.arc/planning/` folder and begin spawning subagents via the bridge.

---

## 4. Best Practices for Antigravity users
- **Keep Dash Open:** Always run `./dash` in a side terminal. Antigravity will update the dashboard state automatically through the `update.py` tool.
- **Utilize Skills:** Antigravity is skill-aware. When you spawn an agent, use a skill from `.agent/skills/` (e.g., `auditor` or `researcher`).
- **Leverage the 50/50 Rule:** Don't do all the coding yourself. Ask Antigravity to: *"Spawn Alpha to research the API while you build the UI."*

---
*ARC Protocol v2.0 - Optimized for Antigravity AI.*
