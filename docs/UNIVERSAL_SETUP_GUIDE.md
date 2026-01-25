# Universal Setup Guide

This guide covers getting ARC running on Linux, macOS, or Windows (WSL2).

## Prerequisites
*   **Python:** Version 3.10+ (The Logic Engine).
*   **Node.js:** Version 18+ (Required for the Gemini Auth Bridge).
*   **A Google Account:** For secure, free authentication.

---

## 1. Install the Core Tools

Run the checking script included in the repo. It creates a virtual environment (`venv`) so we don't mess up your system python.

```bash
python3 setup_arc.py
```

## 2. Authenticate with Google

ARC delegates actual intelligence to Gemini. We use their official CLI to keep things secure.

```bash
# Install the CLI tool
npm install -g @google/generative-ai

# Log in (This will open a browser window)
gemini login
```

Once you see "Authentication successful" in the browser, you are done.

## 3. Connect Your Editor (MCP)

To let your AI editor (Cursor/Windsurf/Claude) control the agents, you need to tell it where our server lives.

> **What is MCP?**
> The **Model Context Protocol** is a standard that allows AI tools to talk to local files and scripts safely. It's the "USB cable" connecting your fancy AI editor to your actual hard drive.

1.  Open your IDE's **MCP Settings** (usually in a config JSON file).
2.  Add the `arc-bridge` server using the **absolute path** to the repo.

**Config Example:**
```json
{
  "mcpServers": {
    "arc-bridge": {
      "command": "python3", 
      "args": ["/ABSOLUTE/PATH/TO/arc-protocol/.agent/mcp/arc_mcp_server.py"]
    }
  }
}
```
*(Replace `/ABSOLUTE/PATH/TO/...` with the real path. You can find it by typing `pwd` in your terminal).*

## 4. Launch the Dashboard

Open a **NEW, SEPARATE terminal window**. Keep your previous one for general commands, but dedicate this new one solely to the dashboard. This is your "Mission Control" screen.
Navigate to the project folder and run:

```bash
./dash
```

You should see this:

![ARC Dashboard](../assets/Dashboard.png)

You are now ready to start using ARC.
