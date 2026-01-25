#!/usr/bin/env python3
import json
import time
import re
from datetime import datetime, timedelta
from pathlib import Path

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Header, Footer, Static, Input, DataTable, RichLog
from textual.reactive import reactive
from textual.binding import Binding
from rich.table import Table
from rich.text import Text
from rich.panel import Panel
from rich.align import Align

# --- CONFIGURATION ---
SCRIPT_DIR = Path(__file__).parent.absolute()
PROJECT_ROOT = SCRIPT_DIR.parent.parent
STATE_FILE = PROJECT_ROOT / ".arc" / "arc_workflow_state.json"

class DashboardHeader(Static):
    """The top header with ASCII logo and metrics."""
    
    metrics = reactive({})
    
    def on_mount(self) -> None:
        self.update_stats()
        self.set_interval(1, self.update_stats)

    def update_stats(self) -> None:
        # Calculate time
        start_ts = self.metrics.get("phase_start_time")
        if start_ts:
            elapsed = datetime.now().timestamp() - start_ts
            # Fix: Reset if > 1 year (30M seconds)
            if elapsed > 30000000:
                time_str = "00:00:00"
            else:
                time_str = str(timedelta(seconds=int(elapsed)))
        else:
            time_str = "00:00:00"

        # Calculate Progress
        done = self.metrics.get("tasks_completed", 0)
        total = self.metrics.get("tasks_total", 0)
        pct = int((done / total) * 100) if total > 0 else 0
        
        # ASCII Logo
        logo = Text(r"""
   █████╗ ██████╗  ██████╗ 
  ██╔══██╗██╔══██╗██╔════╝ 
  ███████║██████╔╝██║      
  ██╔══██║██╔══██╗██║      
  ██║  ██║██║  ██║╚██████╗ 
  ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ 
""", style="bold cyan")

        # Stats Grid
        grid = Table.grid(expand=True, padding=(0, 2))
        grid.add_column(justify="right")
        grid.add_row(f"[bold white]PROJECT:[/]{self.metrics.get('project', 'ARC Protocol')}")
        grid.add_row(f"[bold yellow]PHASE:[/]{self.metrics.get('phase', 'N/A')}")
        grid.add_row(f"[bold green]TIME:[/]{time_str}")
        
        # Progress Bar
        bar_width = 15
        filled = int(bar_width * (pct / 100))
        bar = f"[magenta]{'█'*filled}[/][dim magenta]{'░'*(bar_width-filled)}[/]"
        grid.add_row(f"TASKS: {done}/{total} {bar}")

        # Combine
        layout = Table.grid(expand=True)
        layout.add_column(ratio=1)
        layout.add_column(ratio=1, justify="right")
        layout.add_row(logo, grid)
        
        self.update(Panel(layout, style="blue", border_style="blue"))

class OrchestratorPanel(Static):
    """The Orchestrator Status Panel."""
    status = reactive("IDLE")
    action = reactive("Waiting...")

    def render(self):
        color = "green" if self.status != "IDLE" else "white"
        content = Align.center(
            f"\n[bold {color}]{self.status}[/]\n\n[italic white]{self.action}[/]",
            vertical="middle"
        )
        return Panel(content, title="🧠 ORCHESTRATOR", border_style="cyan")

class AgentTable(Static):
    """The Subagents Table with Premium UI."""
    agents = reactive({})

    def render(self):
        table = Table(expand=True, show_header=True, header_style="bold cyan", box=None, padding=(0, 1))
        table.add_column("Agent", width=14)
        table.add_column("Status", width=10)
        table.add_column("Progress", width=12)
        table.add_column("Activity")

        # Define default fleet
        default_fleet = {
            "Research-Agent": {"skill": "researcher", "color": "magenta"},
            "Build-Agent": {"skill": "coder", "color": "green"},
            "Audit-Agent": {"skill": "auditor", "color": "red"},
            "Architect-Agent": {"skill": "architect", "color": "blue"},
            "Debug-Agent": {"skill": "debugger", "color": "yellow"}
        }
        
        # Merge live data
        display_agents = default_fleet.copy()
        for name, info in self.agents.items():
            if name in display_agents:
                display_agents[name].update(info)
            else:
                display_agents[name] = info 

        for i, (name, info) in enumerate(sorted(display_agents.items())):
            if i > 12: break
            s = info.get('status', 'IDLE')
            c = "dim"
            bar = "[dim]░░░░░░░░░░[/]"
            
            if s == "WORKING": 
                c = "bold white"
                # Animated flash effect for working (simulated)
                bar = "[cyan]█████[/][dim]░░░░░[/]" 
            elif s == "THINKING":
                c = "bold bright_magenta"
                bar = "[bright_magenta]▓▓▓▓▓▓[/][dim]░░░░[/]"
            elif s == "DONE": 
                c = "green"
                bar = "[green]██████████[/]"
            elif s == "ERROR": 
                c = "bold red"
                bar = "[red]!!!!!!!!!![/]"
            
            task = info.get('task', 'Waiting...')
            if len(task) > 30: task = task[:27] + "..."
            
            table.add_row(
                f"[{info.get('color', 'white')}]{name}[/]", 
                f"[{c}]{s}[/]", 
                bar,
                f"[italic]{task}[/]"
            )
            
        return Panel(table, title="🛠️  SUBAGENT FLEET", border_style="white", subtitle="[dim cyan]v2.1 Parallel Engine[/]")

class ARCDashboardApp(App):
    """The Main Application Class."""
    
    CSS = """
    Screen {
        layout: vertical;
        background: #0d1117;
    }
    #header-box {
        height: 10;
        dock: top;
    }
    #middle-row {
        height: 1fr;
        layout: horizontal;
    }
    #left-col {
        width: 1fr;
        layout: vertical;
    }
    #right-col {
        width: 2fr;
    }
    #cortex {
        height: 1fr;
    }
    #cmd-box {
        height: 8; 
        border: solid green;
        background: #0d1117;
    }
    #cmd-status {
        color: yellow;
        text-style: bold;
        padding-left: 1;
    }
    Input {
        dock: top;
        background: #0d1117;
        border: none;
        color: green;
    }
    #logs {
        height: 12;
        dock: bottom;
        border: solid magenta;
        background: #0d1117;
    }
    """

    def compose(self) -> ComposeResult:
        # Header
        yield DashboardHeader(id="header-box")
        
        # Middle Section
        with Horizontal(id="middle-row"):
            with Vertical(id="left-col"):
                yield OrchestratorPanel(id="cortex")
                
                # Command Input Box
                with Container(id="cmd-box"):
                    yield Static("⌨️  COMMAND", classes="box-title")
                    yield Input(placeholder="Type /help...", id="cmd-input")
                    yield Static("", id="cmd-status") 
            
            with Container(id="right-col"):
                yield AgentTable(id="agents")

        # Bottom Logs
        yield RichLog(id="logs", highlight=True, markup=True, wrap=True)

    def on_mount(self) -> None:
        self.query_one(RichLog).write("[bold magenta]📜 DATA UPLINK INITIALIZED...[/]")
        self.query_one(RichLog).border_title = "📜 DATA UPLINK"
        
        # Start the data refresh timer (100ms)
        self.set_interval(0.1, self.load_state)
        
        # Focus input immediately
        self.query_one(Input).focus()

    def load_state(self) -> None:
        if not STATE_FILE.exists():
            return

        try:
            with open(STATE_FILE, "r") as f:
                data = json.load(f)
            
            # Update Header Metrics
            header = self.query_one(DashboardHeader)
            header.metrics = {
                "project": data.get("project_name", "ARC"),
                "phase": data.get("phase", "N/A"),
                "phase_start_time": data.get("metrics", {}).get("phase_start_time"),
                "tasks_completed": data.get("metrics", {}).get("tasks_completed", 0),
                "tasks_total": data.get("metrics", {}).get("tasks_total", 0),
            }

            # Update Agents
            self.query_one(AgentTable).agents = data.get("agents", {})

            # Update Orchestrator
            cortex = self.query_one(OrchestratorPanel)
            main = data.get("main_agent", {})
            cortex.status = main.get("status", "IDLE")
            cortex.action = main.get("action", "Waiting...")

            # Update Logs
            logs = data.get("logs", [])
            log_widget = self.query_one(RichLog)
            
            # Append only new logs
            if not hasattr(self, "_last_log_count"):
                self._last_log_count = 0
            
            if len(logs) > self._last_log_count:
                new_lines = logs[self._last_log_count:]
                for line in new_lines:
                    # Regex to find paths like 'Saved to X.md' and add links
                    def link_replacer(match):
                        path_str = match.group(0)
                        if path_str.startswith("/"):
                            abs_path = path_str
                        else:
                            abs_path = str(PROJECT_ROOT / path_str)
                        return f"[link=file://{abs_path}]{path_str}[/link]"

                    # Apply link formatting
                    line_linked = re.sub(r'[\w\-\./\\]+\.(md|py|json|txt|log)', link_replacer, line)
                    
                    # Add space padding
                    log_widget.write(" " + line_linked)
                self._last_log_count = len(logs)

        except Exception:
            pass

    def on_input_submitted(self, event: Input.Submitted) -> None:
        cmd = event.value.strip()
        status_label = self.query_one("#cmd-status", Static)
        
        if not cmd: return
        
        if cmd == "/clean":
            status_label.update("✅ Dashboard Reset")
            # Reset the file with clean state
            with open(STATE_FILE, "w") as f:
                json.dump({
                    "project_name": "ARC Protocol",
                    "phase": "System Reset",
                    "agents": {},
                    "main_agent": {"status": "ONLINE", "action": "Ready"},
                    "logs": ["[SYSTEM] Dashboard cleared."],
                    "metrics": {"tasks_completed": 0, "tasks_total": 0, "time_elapsed": "0m", "phase_start_time": time.time()}
                }, f)
            
            self.query_one(RichLog).clear()
            self._last_log_count = 0
            self.load_state() # Force immediate refresh
            
        elif cmd == "/exit":
            self.exit()
            
        elif cmd == "/help":
            status_label.update("ℹ️  Available: /clean, /exit")
            
        else:
            status_label.update(f"❌ Unknown: {cmd}")
        
        # Clear input
        self.query_one(Input).value = ""

if __name__ == "__main__":
    app = ARCDashboardApp()
    app.run()