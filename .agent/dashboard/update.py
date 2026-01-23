import json
import os
from datetime import datetime
from pathlib import Path

# Path to the state file
SCRIPT_DIR = Path(__file__).parent.absolute()
PROJECT_ROOT = SCRIPT_DIR.parent.parent
STATE_FILE = PROJECT_ROOT / ".arc" / "arc_workflow_state.json"

def update_arc_state(agent=None, status=None, task=None, log=None, project=None, phase=None, main_status=None, main_action=None, tasks_completed=None, tasks_total=None, time_elapsed=None):
    if not STATE_FILE.exists():
        data = {
            "project_name": "ARC Project", 
            "phase": "N/A", 
            "agents": {}, 
            "main_agent": {"status": "IDLE", "action": "Waiting..."},
            "logs": [],
            "metrics": {"tasks_completed": 0, "tasks_total": 0, "time_elapsed": "0m"}
        }
    else:
        with open(STATE_FILE, "r") as f:
            data = json.load(f)
        if "main_agent" not in data:
            data["main_agent"] = {"status": "IDLE", "action": "Waiting..."}
        if "metrics" not in data:
            data["metrics"] = {"tasks_completed": 0, "tasks_total": 0, "time_elapsed": "0m"}

    if project: data["project_name"] = project
    if phase: 
        data["phase"] = phase
        # Reset timer on new phase
        data["metrics"]["phase_start_time"] = datetime.now().timestamp()
    
    if main_status: data["main_agent"]["status"] = main_status
    if main_action: data["main_agent"]["action"] = main_action

    # Update metrics
    if tasks_completed is not None: data["metrics"]["tasks_completed"] = int(tasks_completed)
    if tasks_total is not None: data["metrics"]["tasks_total"] = int(tasks_total)
    if time_elapsed: data["metrics"]["time_elapsed"] = time_elapsed
    
    # Ensure start time exists for live clock
    if "phase_start_time" not in data["metrics"]:
        data["metrics"]["phase_start_time"] = datetime.now().timestamp()

    if agent:
        if "agents" not in data: data["agents"] = {}
        if agent not in data["agents"]:
            colors = {"Architect": "blue", "Executor": "green", "Reviewer": "yellow"}
            data["agents"][agent] = {"status": "IDLE", "task": "N/A", "color": colors.get(agent, "magenta")}
        
        if status: data["agents"][agent]["status"] = status
        if task: data["agents"][agent]["task"] = task

    if log:
        timestamp = datetime.now().strftime("%H:%M:%S")
        color = data.get("agents", {}).get(agent, {}).get("color", "white") if agent else "white"
        prefix = f"[[bold {color}]{agent.upper()}[/]] " if agent else "[[bold cyan]MAIN[/]] "
        data["logs"].append(f"[grey70]{timestamp}[/] {prefix}{log}")
        if len(data["logs"]) > 100:
            data["logs"].pop(0)

    with open(STATE_FILE, "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    import sys
    args = {}
    for arg in sys.argv[1:]:
        if "=" in arg:
            k, v = arg.split("=", 1)
            args[k] = v
    update_arc_state(**args)
