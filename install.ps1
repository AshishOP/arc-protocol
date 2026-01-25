# ARC Protocol v2.1 - PowerShell Bootstrapper
# This script delegates all logic to setup_arc.py for consistency.

Write-Host "🚀 Bootstrapping ARC Installation via Python Wizard..." -ForegroundColor Cyan

# Check for Python
if (!(get-command python3 -erroraction silentlycontinue)) {
    Write-Host "❌ ERROR: python3 is required to install ARC." -ForegroundColor Red
    exit 1
}

# Run the Universal Setup Wizard
python3 setup_arc.py
