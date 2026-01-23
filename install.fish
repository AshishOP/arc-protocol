#!/usr/bin/fish

# ARC Protocol v2.0 - Fish Installer

echo (set_color cyan)"🚀 Initializing ARC Protocol Installation..."

# 1. Environment Setup
if not test -d venv
    echo (set_color yellow)"📦 Creating Virtual Environment..."
    python3 -m venv venv
end

echo (set_color yellow)"📥 Installing dependencies..."
./venv/bin/pip install -q -r requirements.txt

# 2. Scaffolding Folders
echo (set_color yellow)"📂 Scaffolding project structure..."
mkdir -p .arc/archive/subagent_logs
mkdir -p .arc/planning
mkdir -p .arc/state

# 3. Create Dashboard Shortcut
echo (set_color yellow)"🔗 Creating dash shortcut..."
echo "#!/usr/bin/env fish
./venv/bin/python .agent/dashboard/monitor.py" > dash
chmod +x dash

# 4. MCP Info
set PROJECT_PATH (pwd)
echo ""
echo (set_color green)"✨ Installation Complete!"
echo "---------------------------------------------------"
echo "🛠️  TO CONFIGURE MCP:"
echo "Add this to your IDE's MCP config:"
echo ""
echo "{"
echo "  \"mcpServers\": {"
echo "    \"arc-bridge\": {"
echo "      \"command\": \"python3\","
echo "      \"args\": [\"$PROJECT_PATH/.agent/mcp/arc_mcp_server.py\"],"
echo "      \"env\": { \"GEMINI_MODEL\": \"flash\" }"
echo "    }"
echo "  }"
echo "}"
echo "---------------------------------------------------"
echo "🚀 To start the dashboard, run: ./dash"
echo "---------------------------------------------------"
