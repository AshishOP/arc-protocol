#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path

# ARC Protocol v2.0 - Universal Python Installer

def run_cmd(cmd):
    try:
        subprocess.check_call(cmd, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing: {cmd}")
        sys.exit(1)

def install():
    print("🚀 Initializing ARC Protocol Universal Installation...")
    
    root = Path.cwd()
    venv_path = root / "venv"
    
    # 1. Environment Setup
    if not venv_path.exists():
        print("📦 Creating Virtual Environment...")
        subprocess.check_call([sys.executable, "-m", "venv", "venv"])

    print("📥 Installing dependencies...")
    pip_exe = venv_path / ("Scripts" if os.name == "nt" else "bin") / "pip"
    run_cmd(f"{pip_exe} install -q -r requirements.txt")

    # 2. Scaffolding
    print("📂 Scaffolding project structure...")
    folders = [".arc/archive/subagent_logs", ".arc/planning", ".arc/state"]
    for f in folders:
        (root / f).mkdir(parents=True, exist_ok=True)

    # 3. Shortcut
    print("🔗 Creating dashboard shortcut...")
    py_exe = venv_path / ("Scripts" if os.name == "nt" else "bin") / "python"
    if os.name == "nt":
        with open("dash.bat", "w") as f:
            f.write(f"{py_exe} .agent/dashboard/monitor.py")
    else:
        with open("dash", "w") as f:
            f.write(f"#!/usr/bin/env bash\n{py_exe} .agent/dashboard/monitor.py")
        os.chmod("dash", 0o755)

    # 4. Final Info
    print("\n✨ Installation Complete!")
    print("-" * 50)
    print("🚀 To start the dashboard, run:")
    print("   ./dash (Linux/Mac)")
    print("   .\\dash.bat (Windows)")
    print("-" * 50)

if __name__ == "__main__":
    install()
