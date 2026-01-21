#!/usr/bin/env python3
import json
import os
import sys
import time
from datetime import datetime
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from rich.text import Text

# Path to the state file
STATE_FILE = os.path.join(os.path.dirname(__file__), "../../arc_workflow_state.json")

console = Console()

class ARCDashboard:
    def __init__(self):
        self.logs = []
        self.default_agents = {
            "Architect": {"status": "IDLE", "task": "Waiting...", "color": "blue"},
            "Executor": {"status": "IDLE", "task": "Waiting...", "color": "green"},
            "Reviewer": {"status": "IDLE", "task": "Waiting...", "color": "yellow"}
        }
        self.agents = self.default_agents.copy()
        self.main_agent = {"status": "IDLE", "action": "Waiting..."}
        self.project_name = "ARC Project"
        self.phase = "N/A"
        self.last_update = "N/A"

    def load_state(self):
        if os.path.exists(STATE_FILE):
            try:
                with open(STATE_FILE, "r") as f:
                    data = json.load(f)
                    
                    # Merge loaded agents with defaults to ensure all 3 appear
                    loaded_agents = data.get("agents", {})
                    new_agents = self.default_agents.copy()
                    for k, v in loaded_agents.items():
                        new_agents[k] = v
                    self.agents = new_agents
                    
                    self.main_agent = data.get("main_agent", self.main_agent)
                    self.logs = data.get("logs", self.logs)[-12:] # Reduced from 20 to prevent overflow
                    self.project_name = data.get("project_name", self.project_name)
                    self.phase = data.get("phase", self.phase)
                    self.last_update = datetime.now().strftime("%H:%M:%S")
            except:
                pass

    def generate_layout(self) -> Layout:
        layout = Layout()
        layout.split(
            Layout(name="header", size=10),
            Layout(name="main", ratio=1),
            Layout(name="footer", size=3),
        )
        layout["main"].split_row(
            Layout(name="side", ratio=1),
            Layout(name="body", ratio=2),
        )
        
        # Header
        ascii_logo = """
   ___     ____     ______ 
  /   |   / __ \   / ____/ 
 / /| |  / /_/ /  / /      
/ ___ | / _, _/  / /___    
/_/  |_|/_/ |_|   \____/    
"""
        layout["header"].update(
            Panel(
                Text(f"{ascii_logo}\nARC PROTOCOL DASHBOARD | {self.project_name}", justify="center", style="bold cyan"),
                style="blue"
            )
        )

        # Side - Subagent Status + Main Agent Action
        side_layout = Layout()
        side_layout.split(
            Layout(name="main_status", size=5),
            Layout(name="worker_status", ratio=1)
        )

        # Main Agent Panel
        main_status_text = Text.from_markup(
            f"Status: [bold cyan]{self.main_agent['status']}[/]\n"
            f"Action: [italic]{self.main_agent['action']}[/]"
        )
        side_layout["main_status"].update(Panel(main_status_text, title="🧠 Cortex", border_style="cyan"))

        # Workers Table
        table = Table(expand=True, box=None, padding=(0, 1))
        table.add_column("Worker", style="bold", min_width=10)
        table.add_column("Status", min_width=8)
        table.add_column("Task", ratio=1)

        for agent, info in self.agents.items():
            status_style = "bold green" if info["status"] == "DONE" else "bold yellow" if info["status"] in ["WORKING", "THINKING", "DESIGNING"] else "white"
            table.add_row(
                f"[{info['color']}]{agent}[/]", 
                f"[{status_style}]{info['status']}[/]", 
                info["task"]
            )
        side_layout["worker_status"].update(Panel(table, title="🛠️ Workers", border_style="white"))

        layout["side"].update(side_layout)

        # Body - Logs
        log_text = Text.from_markup("\n".join(self.logs))
        layout["body"].update(Panel(log_text, title="📜 Execution Stream", border_style="magenta"))

        # Footer
        layout["footer"].update(
            Panel(
                Text(f"LAST SYNC: {self.last_update} | ARC ENGINE: ACTIVE", justify="center", style="bold green"),
                style="green"
            )
        )
        
        return layout

if __name__ == "__main__":
    dash = ARCDashboard()
    try:
        # Re-enabling screen=True for dedicated buffer, which prevents duplication
        with Live(dash.generate_layout(), refresh_per_second=4, screen=True) as live:
            while True:
                dash.load_state()
                live.update(dash.generate_layout())
                time.sleep(0.2)
    except Exception as e:
        console.print(f"[bold red]Dashboard Error:[/] {e}")
