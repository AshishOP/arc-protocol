#!/usr/bin/env python3
"""
ARC Protocol - Background AI Agent
Implementing TRUE PARALLELISM within Antigravity.

This script acts as a secondary AI agent that works in the background.
It can be spawned by the main agent to perform tasks independently.
"""

import sys
import json
import os
import time
import fcntl
from datetime import datetime
from pathlib import Path

# Paths - use absolute path from the script location
SCRIPT_DIR = Path(__file__).parent.absolute()
BASE_DIR = SCRIPT_DIR.parent.parent  # Go up from .agent/workers/ to project root
ARC_DIR = BASE_DIR / ".arc"
STATE_FILE = ARC_DIR / "arc_workflow_state.json"

class BackgroundAgent:
    def __init__(self, agent_id, task, model="gemini-1.5-flash", skill="general", extra_files=""):
        self.agent_id = agent_id
        self.task = task
        self.model = model
        self.skill = skill
        self.extra_files = extra_files.split(",") if extra_files else []
        self.workspace = str(BASE_DIR)
        ARC_DIR.mkdir(parents=True, exist_ok=True)
        
    def update_dashboard(self, status, task_desc):
        try:
            # Skill to Color Mapping
            skill_colors = {
                "researcher": "magenta",
                "coder": "green",
                "auditor": "red",
                "architect": "blue",
                "debugger": "yellow",
                "general": "cyan"
            }
            agent_color = skill_colors.get(self.skill.lower(), "white")

            # Ensure file exists
            if not STATE_FILE.exists():
                with open(STATE_FILE, 'w') as f:
                    json.dump({"agents": {}, "logs": []}, f)

            # Use file locking to prevent race conditions
            with open(STATE_FILE, 'r+') as f:
                fcntl.flock(f, fcntl.LOCK_EX) # Exclusive Lock
                try:
                    content = f.read()
                    try:
                        state = json.loads(content) if content else {}
                    except json.JSONDecodeError:
                        state = {}
                        
                    # Ensure defaults if file was corrupted
                    if "agents" not in state: state["agents"] = {}
                    if "logs" not in state: state["logs"] = []

                    # Update Agent
                    state["agents"][self.agent_id] = {
                        "status": status,
                        "task": task_desc,
                        "color": agent_color,
                        "skill": self.skill
                    }
                    
                    # Update Log
                    timestamp = datetime.now().strftime('%H:%M:%S')
                    log_entry = f"[grey70]{timestamp}[/] [[bold {agent_color}]{self.agent_id}[/]] [{self.skill.upper()}] {task_desc}"
                    state["logs"].append(log_entry)
                    if len(state["logs"]) > 50:
                        state["logs"] = state["logs"][-50:]
                    
                    # Write back
                    f.seek(0)
                    json.dump(state, f, indent=2)
                    f.truncate()
                    
                finally:
                    fcntl.flock(f, fcntl.LOCK_UN) # Unlock

            print(f"[{timestamp}] [{self.agent_id}] {status}: {task_desc}")
                
        except Exception as e:
            print(f"Dashboard update failed: {e}", file=sys.stderr)

    def load_context(self):
        """Loads critical project context to ensure the subagent isn't blind."""
        context = []
        
        # 1. Load Specific Skill Definition (Search multiple locations)
        paths = [
            SCRIPT_DIR.parent / "skills" / "definitions" / f"{self.skill}.md",
            SCRIPT_DIR.parent / "skills" / self.skill / "SKILL.md",
        ]
        
        found = False
        for p in paths:
            if p.exists():
                context.append(f"## ACTIVE SKILL: {self.skill.upper()}\n{p.read_text()}\n")
                found = True
                break
        
        if not found:
            # Fallback to general manifesto if skill not found
            manifest_file = SCRIPT_DIR.parent / "rules" / "SUBAGENT_MANIFEST.md"
            if manifest_file.exists():
                context.append(f"## SUBAGENT MANIFESTO\n{manifest_file.read_text()}\n")

        # 2. Context Strategy (Optimization)
        # Always load PROJECT.md (Vision)
        project_file = ARC_DIR / "PROJECT.md"
        if project_file.exists():
            context.append(f"## PROJECT CONTEXT\n{project_file.read_text()}\n")
            
        # Only load CONTRACTS if we are CODING or AUDITING
        if self.skill in ["coder", "auditor", "architect"]:
            contracts_file = ARC_DIR / "CONTRACTS.md"
            if contracts_file.exists():
                context.append(f"## CONTRACTS (STRICT COMPLIANCE)\n{contracts_file.read_text()}\n")
            
        # 3. Extra Context Files (Injected by Orchestrator)
        if hasattr(self, 'extra_files') and self.extra_files:
            context.append("## TARGET FILE CONTEXT\n")
            for fpath in self.extra_files:
                full_fpath = BASE_DIR / fpath
                if full_fpath.exists() and full_fpath.is_file():
                    context.append(f"### File: {fpath}\n{full_fpath.read_text()}\n")

        # 4. Current Session State (Single Source of Truth)
        state_md = ARC_DIR / "STATE.md"
        if state_md.exists():
            context.append(f"## CURRENT SESSION STATE\n{state_md.read_text()}\n")
            
        return "\n".join(context)

    def run(self):
        """Execute the background task using Gemini CLI"""
        print(f"\n{'='*50}")
        print(f"BACKGROUND AGENT: {self.agent_id}")
        print(f"TASK: {self.task}")
        print(f"MODEL: {self.model}")
        print(f"SKILL: {self.skill}")
        print(f"{'='*50}\n")
        
        self.update_dashboard("WORKING", f"Starting: {self.task}")
        
        try:
            # 1. Gather Context
            self.update_dashboard("WORKING", "[1/4] Loading Project Context...")
            project_context = self.load_context()
            
            # Create a rich prompt
            full_prompt = (
                f"You are a sub-agent named {self.agent_id} working on the ARC Protocol.\n"
                f"You have been assigned the SKILL: {self.skill.upper()}\n\n"
                f"### SAFETY PROTOCOLS (MANDATORY):\n"
                f"1. NEVER delete files or directories unless explicitly told in the TASK.\n"
                f"2. NEVER modify files outside the workspace directory: {self.workspace}\n"
                f"3. NEVER change ownership or permissions of system files.\n"
                f"4. If you are unsure, provide the code as a BLOCK in a markdown report instead of writing to disk.\n\n"
                f"Here is your project context:\n\n"
                f"{project_context}\n\n"
                f"--- END OF CONTEXT ---\n\n"
                f"YOUR TASK:\n{self.task}\n\n"
                f"Perform the task using your SKILL. Be professional, direct, and adhere to all contracts."
            )

            # 2. Ask Gemini
            self.update_dashboard("WORKING", f"[2/4] Executing via Gemini CLI...")
            
            # Construct command: gemini [-m <model>] "<full_prompt>"
            if self.model == "default":
                cmd = ["gemini", full_prompt]
            else:
                cmd = ["gemini", "-m", self.model, full_prompt]
            
            # Run subprocess
            import subprocess
            result = subprocess.run(
                cmd, 
                capture_output=True, 
                text=True,
                cwd=self.workspace
            )
            
            if result.returncode != 0:
                raise Exception(f"Gemini CLI failed: {result.stderr}")
            
            output = result.stdout.strip()
            
            # 3. Save Result
            self.update_dashboard("WORKING", "[3/4] Saving results...")
            
            # Create a filename
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"{self.agent_id}_{self.skill}_{timestamp}.md"
            output_dir = ARC_DIR / "archive" / "subagent_logs"
            output_dir.mkdir(parents=True, exist_ok=True)
            output_path = output_dir / filename
            
            with open(output_path, "w") as f:
                f.write(f"# Output from {self.agent_id} (Skill: {self.skill})\n\n")
                f.write(f"**Task:** {self.task}\n\n")
                f.write(f"**Model:** {self.model}\n\n")
                f.write("---\n\n")
                f.write(output)
            
            # 4. Finalize
            self.update_dashboard("DONE", f"Completed. Saved to {filename}")
            print(f"\nOUTPUT SAVED TO: {output_path}")
            
        except Exception as e:
            self.update_dashboard("ERROR", str(e))
            print(f"ERROR: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: background_agent.py <agent_id> <task> [model] [skill]")
        sys.exit(1)
    
    agent_id = sys.argv[1]
    task = sys.argv[2]
    # Check env var for default if not provided
    default_model = os.environ.get("GEMINI_MODEL", "flash")
    model = sys.argv[3] if len(sys.argv) > 3 else default_model
    skill = sys.argv[4] if len(sys.argv) > 4 else "general"
    extra_files = sys.argv[5] if len(sys.argv) > 5 else ""
        
    agent = BackgroundAgent(agent_id, task, model, skill, extra_files)
    agent.run()