import os
import sys
import subprocess
import platform

def run_command(cmd, shell=False):
    try:
        subprocess.check_call(cmd, shell=shell)
        return True
    except subprocess.CalledProcessError:
        return False

def setup():
    print("🚀 ARC Protocol: Universal Installer")
    base_dir = os.getcwd()
    
    # 1. Create Structure
    dirs = [
        ".arc/planning", ".arc/archive", ".arc/state", ".arc/templates",
        ".agent/workflows", ".agent/dashboard", ".agent/rules", ".agent/skills"
    ]
    for d in dirs:
        os.makedirs(os.path.join(base_dir, d), exist_ok=True)
    
    # Ensure CLAUDE.md exists in root
    if not os.path.exists(os.path.join(base_dir, "CLAUDE.md")):
        with open(os.path.join(base_dir, "CLAUDE.md"), "w") as f:
            f.write("# ARC Protocol for Claude\n\nRefer to `README.md` for full context.\n")
            
    print("📁 Directory structure & CLAUDE.md: OK")

    # 2. Virtual Environment
    venv_dir = os.path.join(base_dir, "venv")
    if not os.path.exists(venv_dir):
        print("🐍 Creating virtual environment...")
        run_command([sys.executable, "-m", "venv", "venv"])
    
    # OS-Specific Paths
    if platform.system() == "Windows":
        python_exe = os.path.join(venv_dir, "Scripts", "python.exe")
        pip_exe = os.path.join(venv_dir, "Scripts", "pip.exe")
    else:
        python_exe = os.path.join(venv_dir, "bin", "python3")
        pip_exe = os.path.join(venv_dir, "bin", "pip")

    # 3. Dependencies
    print("📦 Installing dependencies (rich)...")
    run_command([pip_exe, "install", "rich"])

    # 4. Global Shortcut
    print("🔗 Setting up 'dash' shortcut...")
    if platform.system() != "Windows":
        # Mac/Linux Symlink
        bin_dir = os.path.expanduser("~/.local/bin")
        os.makedirs(bin_dir, exist_ok=True)
        dash_script = os.path.join(base_dir, "dash")
        with open(dash_script, "w") as f:
            f.write(f"#!/usr/bin/env bash\n{python_exe} {os.path.join(base_dir, '.agent/dashboard/monitor.py')}\n")
        os.chmod(dash_script, 0o755)
        
        target = os.path.join(bin_dir, "dash")
        if os.path.exists(target): os.remove(target)
        os.symlink(dash_script, target)
        print(f"✅ Shortcut created at {target}")
    else:
        # Windows Batch File
        bin_dir = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "WindowsApps")
        dash_bat = os.path.join(bin_dir, "dash.bat")
        with open(dash_bat, "w") as f:
            f.write(f'@echo off\n"{python_exe}" "{os.path.join(base_dir, ".agent/dashboard/monitor.py")}"\n')
        print(f"✅ Windows shortcut created at {dash_bat}")

    print("\n🎉 ARC Protocol is ready!")
    print("👉 Type 'dash' to open the dashboard.")

if __name__ == "__main__":
    setup()
