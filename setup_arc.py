#!/usr/bin/env python3
import os
import sys
import subprocess
import json
import time

def print_banner():
    print("""
    \033[1;96m   █████╗ ██████╗  ██████╗ 
      ██╔══██╗██╔══██╗██╔════╝ 
      ███████║██████╔╝██║      
      ██╔══██║██╔══██╗██║      
      ██║  ██║██║  ██║╚██████╗ 
      ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ \033[0m
                                                                        
                         \033[1;97mARC SETUP WIZARD v2.1\033[0m
    """)

def check_dependencies():
    deps = {
        "python3": "python3 --version",
        "node": "node --version",
        "npm": "npm --version",
        "gemini": "gemini --version"
    }
    
    missing = []
    print("\033[94m[*] Checking System Dependencies...\033[0m")
    for name, cmd in deps.items():
        try:
            subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
            print(f"  \033[92m[✓]\033[0m {name} detected.")
        except:
            missing.append(name)
            print(f"  \033[91m[✗]\033[0m {name} NOT detected.")
            
    if "gemini" in missing:
        if "npm" in missing:
            print("\033[91m[!] Node.js and npm are required to run the Gemini CLI.\033[0m")
            print("    1. Install Node.js v18+ from https://nodejs.org/")
            print("    2. Run 'npm install -g @google/generative-ai'")
        else:
            print("\033[93m[!] Gemini CLI missing. Attempting auto-install...\033[0m")
            try:
                subprocess.run("npm install -g @google/generative-ai", shell=True, check=True)
                missing.remove("gemini")
            except:
                print("\033[91m[ERROR] Failed to install Gemini CLI. Please run 'npm install -g @google/generative-ai' manually.\033[0m")

    return len(missing) == 0

def check_auth():
    print("\033[94m[*] Checking Gemini Authentication...\033[0m")
    # This is a heuristic check; usually gemini --version works if installed, 
    # but we want to know if 'gemini login' was run.
    # We can try to list models as a test.
    try:
        # If this fails, the user likely isn't logged in.
        subprocess.check_output("gemini models", shell=True, stderr=subprocess.STDOUT)
        print("  \033[92m[✓]\033[0m Gemini authenticated.")
        return True
    except:
        print("  \033[91m[✗]\033[0m Gemini NOT authenticated.")
        return False

def setup_environment():
    print("\033[94m[*] Setting up Virtual Environment...\033[0m")
    if not os.path.exists("venv"):
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
    
    pip_path = os.path.join("venv", "bin", "pip") if os.name != "nt" else os.path.join("venv", "Scripts", "pip")
    print("\033[94m[*] Installing Python Requirements...\033[0m")
    subprocess.run([pip_path, "install", "rich", "textual", "pydantic", "filelock"], check=True)

def scaffold_arc():
    print("\033[94m[*] Scaffolding .arc/ directory...\033[0m")
    dirs = [".arc/archive", ".arc/planning", ".agent/skills", ".agent/tools"]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        print(f"  \033[92m[+]\033[0m Created {d}")

    # Create dummy workflow state if it doesn't exist
    state_file = ".arc/arc_workflow_state.json"
    if not os.path.exists(state_file):
        with open(state_file, "w") as f:
            json.dump({
                "project": "New ARC Project",
                "phase": "Initialize",
                "agents": {},
                "logs": [],
                "metrics": {"tasks_total": 0, "tasks_completed": 0}
            }, f, indent=2)

def main():
    print_banner()
    
    if not check_dependencies():
        print("\033[91m[FAIL] Required dependencies missing. Setup aborted.\033[0m")
        sys.exit(1)
        
    if not check_auth():
        print("\033[93m[ACTION REQUIRED] Please run 'gemini login' in your terminal and restart this setup.\033[0m")
        # subprocess.run("gemini login", shell=True) # Usually opens browser, so we just wait
        sys.exit(1)
        
    setup_environment()
    scaffold_arc()
    
    # Create Dashboard Shortcut
    print("\033[94m[*] Creating dashboard shortcut ('dash')...\033[0m")
    venv_python = os.path.join("venv", "bin", "python") if os.name != "nt" else os.path.join("venv", "Scripts", "python.exe")
    monitor_script = os.path.join(".agent", "dashboard", "monitor.py")
    
    if os.name == "nt":
        with open("dash.bat", "w") as f:
            f.write(f"@echo off\n\"{os.path.abspath(venv_python)}\" \"{os.path.abspath(monitor_script)}\" %*")
        print("  \033[92m[+]\033[0m Created dash.bat (Windows)")
    else:
        with open("dash", "w") as f:
            f.write("#!/bin/bash\n")
            f.write("# Universal Dash Launcher\n")
            f.write("SCRIPT_DIR=\"$( cd \"$( dirname \"${BASH_SOURCE[0]}\" )\" &> /dev/null && pwd )\"\n")
            f.write("VENV_PYTHON=\"$SCRIPT_DIR/venv/bin/python\"\n")
            f.write("MONITOR_SCRIPT=\"$SCRIPT_DIR/.agent/dashboard/monitor.py\"\n\n")
            f.write("if [ ! -f \"$VENV_PYTHON\" ]; then\n")
            f.write("    echo \"❌ Virtual Environment not found at $VENV_PYTHON\"\n")
            f.write("    exit 1\n")
            f.write("fi\n\n")
            f.write("\"$VENV_PYTHON\" \"$MONITOR_SCRIPT\" \"$@\"\n")
        os.chmod("dash", 0o755)
        print("  \033[92m[+]\033[0m Created dash (Unix/Mac Portable)")

    print("\n\033[92m[SUCCESS] ARC Protocol v2.1 Ready.\033[0m")
    print("\033[94m---------------------------------------------------\033[0m")
    print("\033[1;97m🚀 NEXT STEPS:\033[0m")
    print(f"1. \033[93mAutomate IDE Linking:\033[0m Run 'python3 .agent/tools/link_mcp.py'")
    print(f"2. \033[93mManual IDE Linking:\033[0m Use absolute path below for MCP server:")
    print(f"   \033[96m{os.path.abspath('.agent/mcp/arc_mcp_server.py')}\033[0m")
    print(f"3. \033[93mStart Dashboard:\033[0m Run './dash' (or 'dash.bat')")
    print("\033[94m---------------------------------------------------\033[0m")

if __name__ == "__main__":
    main()
