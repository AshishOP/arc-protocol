# ARC Protocol v2.0 - PowerShell Installer
# For Windows Users

Write-Host "🚀 Initializing ARC Protocol Installation..." -ForegroundColor Cyan

# 1. Environment Setup
if (!(Test-Path "venv")) {
    Write-Host "📦 Creating Virtual Environment..." -ForegroundColor Yellow
    python -m venv venv
}

Write-Host "📥 Installing dependencies..." -ForegroundColor Yellow
.\venv\Scripts\pip install -q -r requirements.txt

# 2. Scaffolding Folders
Write-Host "📂 Scaffolding project structure..." -ForegroundColor Yellow
New-Item -ItemType Directory -Force -Path ".arc\archive\subagent_logs", ".arc\planning", ".arc\state" | Out-Null

# 3. Create Dashboard Shortcut
Write-Host "🔗 Creating dash shortcut..." -ForegroundColor Yellow
$dashContent = @"
.\venv\Scripts\python .agent\dashboard\monitor.py
"@
$dashContent | Out-File -FilePath "dash.bat" -Encoding ASCII

# 4. MCP Info
$currentPath = (Get-Location).Path.Replace('\', '/')
Write-Host "`n✨ Installation Complete!" -ForegroundColor Green
Write-Host "---------------------------------------------------"
Write-Host "🛠️  TO CONFIGURE MCP:"
Write-Host "Add this to your IDE's MCP config:"
Write-Host ""
Write-Host "{"
Write-Host "  `"mcpServers`": {"
Write-Host "    `"arc-bridge`": {"
Write-Host "      `"command`": `"python`",
Write-Host "      `"args`": [`"$currentPath/.agent/mcp/arc_mcp_server.py`"],
Write-Host "      `"env`": { `"GEMINI_MODEL`": `"flash`" }"
Write-Host "    }"
Write-Host "  }"
Write-Host "}"
Write-Host "---------------------------------------------------"
Write-Host "🚀 To start the dashboard, run: .\dash.bat"
Write-Host "---------------------------------------------------"
