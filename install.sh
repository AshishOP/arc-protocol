#!/usr/bin/env bash

# ARC Protocol v2.0 - One-Click Installer
# For Linux, Mac, and WSL

set -e

echo "🚀 Initializing ARC Protocol Installation..."

# 1. Environment Setup
if [ ! -d "venv" ]; then
    echo "📦 Creating Virtual Environment..."
    python3 -m venv venv
fi

echo "📥 Installing dependencies..."
./venv/bin/pip install -q -r requirements.txt

# 2. Scaffolding Folders
echo "📂 Scaffolding project structure..."
mkdir -p .arc/archive/subagent_logs
mkdir -p .arc/planning
mkdir -p .arc/state

# 3. Create Dashboard Shortcut
echo "🔗 Creating dash shortcut..."
cat <<EOF > dash
#!/usr/bin/env bash
./venv/bin/python .agent/dashboard/monitor.py
EOF
chmod +x dash

# 4. MCP Server Info
PROJECT_PATH=$(pwd)
echo ""
echo "✨ Installation Complete!"
echo "---------------------------------------------------"
echo "🛠️  TO CONFIGURE MCP (Model Context Protocol):"
echo "Add this to your AI IDE's MCP config file:"
echo ""
echo "{"
echo "  \"mcpServers\": {"
    echo "    \"arc-bridge\": {"
      echo "      \"command\": \"python3\",\"
      echo "      \"args\": [\"$PROJECT_PATH/.agent/mcp/arc_mcp_server.py\"],\"
      echo "      \"env\": {\"
        echo "        \"GEMINI_MODEL\": \"flash\"\"
      echo "      }"
    echo "    }"
  echo "  }"
echo "}"
echo "---------------------------------------------------"
echo "🚀 To start the dashboard, run: ./dash"
echo "---------------------------------------------------"
