# 🛸 ARC for OpenCode (Cursor / Windsurf)

Open-source and modern AI IDEs like **Cursor** and **Windsurf** are perfect for ARC because they allow deep file system access and custom tool definitions.

---

## 1. Prerequisites
- **Cursor or Windsurf Installed.**
- **Gemini CLI installed:** `npm install -g @google/generative-ai`
- **Authenticated:** `gemini login`

---

## 2. Defining Custom Tools
Cursor/Windsurf can utilize the ARC Bridge through their Composer or Agent modes.

### **Cursor Setup:**
1. Navigate to **Settings > Cursor Settings > General**.
2. Add the project root to the **Index**.
3. Point the agent to `.agent/workflows/`.

### **Windsurf Setup:**
1. Open the **MCP Settings**.
2. Add the `arc-bridge` server:
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

## 3. Workflow Execution in Composer Mode
When using "Composer" (Cmd+I in Cursor):
- Start by providing the context: *"Initialize this project using the /arc-new workflow."*
- Composer will read the templates and build your structure.
- **Parallel Dispatch:** Tell Composer: *"Delegate the CSS generation to a subagent via the arc_spawn_agent tool while we work on the backend."*

---

## 4. The Power of Indexing
Because Cursor indexes your entire codebase, the **.arc/** folder becomes a powerful search target. The AI will constantly cross-reference your **CONTRACTS.md** to make sure its implementation matches your architecture.

---
---
*ARC Protocol v2.1 - The Future of Agentic IDEs.*

## 🛠️ Need help linking?
Run our automated script to link the ARC bridge to your local IDE configs:
```bash
python3 .agent/tools/link_mcp.py
```
