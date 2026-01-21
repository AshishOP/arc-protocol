import json
import os
from datetime import datetime

STATE_FILE = os.path.join(os.path.dirname(__file__), "../../.arc/arc_workflow_state.json")

def update_gsd_state(agent=None, status=None, task=None, log=None, project=None, phase=None, main_status=None, main_action=None):
    if not os.path.exists(STATE_FILE):
        data = {
            "project_name": "Antigravity", 
            "phase": "N/A", 
            "agents": {}, 
            "main_agent": {"status": "IDLE", "action": "Waiting..."},
            "logs": []
        }
    else:
        with open(STATE_FILE, "r") as f:
            data = json.load(f)
        if "main_agent" not in data:
            data["main_agent"] = {"status": "IDLE", "action": "Waiting..."}

    if project: data["project_name"] = project
    if phase: data["phase"] = phase
    
    if main_status: data["main_agent"]["status"] = main_status
    if main_action: data["main_agent"]["action"] = main_action

    if agent:
        if "agents" not in data: data["agents"] = {}
        if agent not in data["agents"]:
            colors = {"Architect": "blue", "Executor": "green", "Reviewer": "yellow"}
            data["agents"][agent] = {"status": "IDLE", "task": "N/A", "color": colors.get(agent, "magenta")}
        
        if status: data["agents"][agent]["status"] = status
        if task: data["agents"][agent]["task"] = task

    if log:
        timestamp = datetime.now().strftime("%H:%M:%S")
        color = data["agents"].get(agent, {}).get("color", "white") if agent else "white"
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
    update_gsd_state(**args)
