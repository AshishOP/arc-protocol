# 🔌 Integrations Guide

ARC is built on the **Model Context Protocol (MCP)**, which means it works with any modern AI editor. Here is how to connect it to your favorite tools.

---

## 1. Antigravity AI (Native)

Antigravity has first-class support for ARC.

**Setup:**
1.  Open **Settings > MCP Servers**.
2.  Click **Add Server**.
3.  **Name:** `arc-bridge`
4.  **Command:** `python3` (or your venv path)
5.  **Args:** `/ABSOLUTE/PATH/TO/.agent/mcp/arc_mcp_server.py`

**Usage:**
Just type `/arc-new` in the main chat.

---

## 2. Claude Desktop (Official)

Claude Desktop allows you to run ARC locally while talking to Claude 3.5 Sonnet.

**Setup:**
1.  Open your config file:
    *   **Mac:** `~/Library/Application Support/Claude/claude_desktop_config.json`
    *   **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
2.  Add this entry:

```json
{
  "mcpServers": {
    "arc-bridge": {
      "command": "python3",
      "args": ["/ABSOLUTE/PATH/TO/.agent/mcp/arc_mcp_server.py"]
    }
  }
}
```

**Usage:**
Claude will now see the `arc_spawn_agent` tool. You can say:
> "Initialize a new ARC project."
> "Run the researcher agent on this task."

---

## 3. VS Code (via Roo Code / Cline)

VS Code doesn't support MCP natively yet, but the **Roo Code** (formerly Cline) extension does.

**Setup:**
1.  Install **Roo Code** from the Marketplace.
2.  Open Roo settings -> **MCP Servers**.
3.  Add a new server:
    *   **Name:** `arc`
    *   **Type:** `stdio`
    *   **Command:** `python3 /ABSOLUTE/PATH/TO/.agent/mcp/arc_mcp_server.py`

**Usage:**
In the Roo sidebar, ask it to "Plan a new phase using ARC." It will utilize the ARC tools to create the `.arc/` structure.

---

## 4. OpenCode / Windsurf

Most forks of VS Code with AI follow the same MCP pattern.

**Setup:**
Look for `mcp_config.json` or "MCP Server Settings" in the command palette.
Use the same stdio configuration as Claude Desktop.

---

## 5. GitHub Copilot

Copilot does not natively support MCP tools yet. To use ARC effectively:

**Setup:**
1.  Create a file at `.github/copilot-instructions.md`.
2.  Add this rule:
    > "You are an ARC-compliant Orchestrator. Always refer to `.arc/CONTRACTS.md` before suggesting code. Follow the workflows in `.agent/workflows/`."

**Usage:**
Since Copilot cannot "click" the tools:
1.  Ask Copilot to **Plan** the work (`/arc-plan`).
2.  Spawn agents manually in the terminal:
    ```bash
    # Manually spawn a subagent
    python3 .agent/workers/background_agent.py "Research-1" "Find the docs for X"
    ```
3.  Watch the dashboard.

---

## 🔒 Authentication Note for All Integrations

ARC uses the **Gemini CLI** for its background workers.
regardless of which editor you use, you must have run:
```bash
gemini login
```
in your terminal *before* interacting with the agents.
