# 🌍 Universal Setup Guide: ARC Protocol v2.1

Welcome to the definitive guide for setting up the **ARC (Analyse. Run. Confirm.) Protocol v2.1** on any machine. This protocol is platform-agnostic, AI-agnostic, and designed for high-performance parallel engineering.

---

## ✨ What's New in v2.1 (The Parallel Engine)

1.  **Ghost Navigator:** Run `python3 .agent/tools/map_topology.py` to generate a 2D visual map of your architecture in `CODEBASE_MAP.md`.
2.  **AI Contract Enforcement:** Run `python3 .agent/tools/contract_check.py` to audit your code against the rules in `.arc/CONTRACTS.md`.
3.  **Premium TUI Dash:** The `./dash` interface now features animated progress and automated heartbeat tracking.
4.  **Universal Wizard:** `setup_arc.py` handles all OS-specific dependencies automatically.

---

## 🏗️ 1. System Requirements

Before you begin, ensure your machine meets the following criteria:

### **Supported OS**
- **Linux:** Ubuntu 20.04+, Fedora 34+, Arch (Optimized for standard Bash/Fish).
- **macOS:** Monterey (12.0) or newer (M1/M2/Intel).
- **Windows:** WSL2 (Highly Recommended) or PowerShell 7+.

### **Software Dependencies**
- **Python 3.10+**: Required for the MCP server, dashboard, and background daemon.
- **Node.js 18+**: Required for the Gemini CLI engine.
- **Git**: For version control and codebase mapping.
- **Rich (Python library)**: For the terminal TUI dashboard.

---

## ⚡ 2. The Core Installation

Follow these steps to initialize the ARC environment in your project.

### **Step A: Clone and Scaffold**
Copy the `.agent` and `.arc` directories from the ARC template repo into your project's root directory.

### **Step B: Universal Installation (Recommended)**
The fastest way to install ARC on any OS (Linux, Mac, Windows) is using the **ARC Setup Wizard**:

```bash
python3 setup_arc.py
```

### **Step C: Shell-Specific Bootstrappers**
If you prefer a native shell command, you can use these "Entry Point" scripts which will trigger the Python wizard:

| Shell | Command |
| :--- | :--- |
| **Bash / Zsh (Mac/Linux)** | `bash install.sh` |
| **Fish Shell** | `fish install.fish` |
| **Windows PowerShell** | `powershell ./install.ps1` |
| **Universal Python Check**| `python3 setup_arc.py` |

---

## 🧬 3. The Nervous System (MCP Setup)

The **Model Context Protocol (MCP)** is what allows your AI (Antigravity, Claude, etc.) to command your machine. In ARC, we use the `arc-bridge`.

### **Configuration Steps:**
1. Locate your IDE's MCP configuration file (e.g., `claude_desktop_config.json`, `mcp_config.json`).
2. Add the `arc-bridge` server. **You must use absolute paths.**

**Example JSON Config:**
```json
{
  "mcpServers": {
    "arc-bridge": {
      "command": "python3", 
      "args": ["/ABS/PATH/TO/antigravity_ai/.agent/mcp/arc_mcp_server.py"],
      "env": {
        "GEMINI_MODEL": "flash"
      }
    }
  }
}
```

---

## 🤖 4. Authenticating the Subagents

ARC uses the **Gemini CLI** to run background tasks. Subagents do not use your AI's main window; they run as independent terminal processes.

1. **Install the CLI:**
   ```bash
   npm install -g @google/generative-ai
   ```
2. **Login to Google:**
   ```bash
   gemini login
   ```
   *Follow the browser instructions to authorize the CLI.*

---

## 📡 5. Starting the Nerve Center (Dashboard)

The Dashboard is your "Mission Control." It is a Textual-based TUI that tracks your fleet's status.

**To start:**
```bash
./dash
```

**What you will see:**
- **The Fleet Status:** Alpha (Researcher), Beta (Coder), Gamma (Auditor), etc.
- **Work Logs:** Real-time logging of subagent activities.
- **Clock:** Time elapsed for the current development phase.

---

## 🚀 6. Your First Workflow

Once everything is installed, trigger your first ARC session:

1. **Initialize Phase:** Run `/arc-new` inside your AI agent.
2. **Architect Phase:** Run `/arc-plan` to create a tasks list and delegation matrix.
3. **Execution Phase:** Run `/arc-execute`. Watch the subagents spawn on your dashboard!
4. **Integration Phase:** Verify subagent reports and merge them into your code.

---

## 🛠️ 7. Troubleshooting

### **Error: Subagent spawned but "NOT RESPONDING"**
- **Fix:** Ensure you ran `gemini login`. Subagents fail silently if the CLI isn't authenticated.
- **Fix:** Check if your internet connection is stable.

### **Error: MCP Connection Failed**
- **Fix:** Verify the path in your JSON config is **ABSOLUTE**. Relative paths (e.g., `./.agent/...`) will fail.

### **Error: 'dash' permission denied**
- **Fix:** Run `chmod +x dash` and `chmod +x .agent/workers/background_agent.py`.

---
*ARC Protocol v2.1 - Universal Engineering Standard.*
