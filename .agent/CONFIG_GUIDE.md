# 🛠️ ARC Protocol - System Configuration Guide

This guide ensures your ARC environment is correctly connected and your subagents are ready for parallel work.

---

## 1. The Nervous System: MCP Server
The **Model Context Protocol (MCP)** server is what allows your AI (Claude/Antigravity) to talk to your local file system and spawn workers.

### **How to Configure:**
1. Open your AI IDE's **MCP Settings** (usually in Settings > Developer > MCP).
2. Add a new server named `arc-bridge`.
3. Set the configuration based on your setup:

**Linux / Mac / WSL:**
```json
{
  "mcpServers": {
    "arc-bridge": {
      "command": "python3",
      "args": ["/ABS/PATH/TO/YOUR/PROJECT/.agent/mcp/arc_mcp_server.py"],
      "env": {
        "GEMINI_MODEL": "flash"
      }
    }
  }
}
```

**Windows:**
```json
{
  "mcpServers": {
    "arc-bridge": {
      "command": "python.exe",
      "args": ["C:\\PATH\\TO\\YOUR\\PROJECT\\.agent\\mcp\\arc_mcp_server.py"],
      "env": {
        "GEMINI_MODEL": "flash"
      }
    }
  }
}
```

---

## 2. The Muscle: Gemini CLI
ARC subagents execute tasks using the **Gemini CLI**. They do not use your web-browser window; they run as independent terminal processes.

### **Installation:**
1. Install Node.js if you haven't.
2. Run: `npm install -g @google/generative-ai`
3. **Crucial:** Run `gemini login` and follow the browser prompt to authenticate.

### **Why Flash?**
We use `gemini-1.5-flash` for subagents because it is optimized for high-speed, low-latency tactical tasks. You can change this in your MCP `env` block, but `flash` is recommended to keep your primary AI's "brain" (the Main Agent) focused on strategy.

---

## 3. The Dashboard: Real-time Monitoring
Always keep the ARC Dashboard (`./dash`) open in a separate panel. It is the only way to see what your subagents are doing while you continue coding.

- **WORKING:** The agent has received the dispatch and is calling the Gemini CLI.
- **DONE:** The agent has saved its report to `.arc/archive/subagent_logs/`.
- **ERROR:** Check the subagent log or your terminal for specific failure reasons (usually authentication or path errors).

---

## 4. Troubleshooting
- **Subagent "Spawned" but did nothing?** Check if you ran `gemini login`.
- **MCP Tool Not Found?** Restart your Main Agent session after updating the MCP config.
- **Paths are wrong?** Ensure you use **Absolute Paths** in your MCP configuration.

---
*ARC Protocol v2.0 — Structured Autonomy.*
