#!/usr/bin/env python3
"""
ARC Protocol - Background Worker Daemon

This daemon watches for tasks from the main agent and executes them
in the background. The main agent can delegate work and continue.

Usage:
    python3 .agent/workers/daemon.py

The main agent writes tasks to .arc/state/worker_queue.json
The daemon picks them up and executes them.
"""

import json
import os
import sys
import time
import subprocess
from datetime import datetime
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent.parent.parent
ARC_DIR = BASE_DIR / ".arc"
STATE_DIR = ARC_DIR / "state"
QUEUE_FILE = STATE_DIR / "worker_queue.json"
RESULTS_FILE = STATE_DIR / "worker_results.json"
DASHBOARD_FILE = ARC_DIR / "arc_workflow_state.json"

# Ensure directories exist
STATE_DIR.mkdir(parents=True, exist_ok=True)

class WorkerDaemon:
    def __init__(self):
        self.running = True
        self.worker_id = f"Worker-{os.getpid()}"
        
    def log(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] [{self.worker_id}] {message}")
        
    def update_dashboard(self, status, task):
        """Update the ARC dashboard with worker status"""
        try:
            if DASHBOARD_FILE.exists():
                with open(DASHBOARD_FILE, 'r') as f:
                    state = json.load(f)
            else:
                state = {"agents": {}, "logs": []}
            
            state.setdefault("agents", {})
            state["agents"]["Worker"] = {
                "status": status,
                "task": task,
                "color": "magenta"
            }
            
            # Add log entry
            log_entry = f"[grey70]{datetime.now().strftime('%H:%M:%S')}[/] [[bold magenta]WORKER[/]] {task}"
            state.setdefault("logs", []).append(log_entry)
            if len(state["logs"]) > 50:
                state["logs"] = state["logs"][-50:]
            
            with open(DASHBOARD_FILE, 'w') as f:
                json.dump(state, f, indent=2)
        except Exception as e:
            self.log(f"Dashboard update failed: {e}")
    
    def read_queue(self):
        """Read pending tasks from queue"""
        if not QUEUE_FILE.exists():
            return []
        try:
            with open(QUEUE_FILE, 'r') as f:
                data = json.load(f)
            return data.get("tasks", [])
        except:
            return []
    
    def clear_queue(self):
        """Clear the task queue"""
        with open(QUEUE_FILE, 'w') as f:
            json.dump({"tasks": []}, f)
    
    def save_result(self, task_id, result):
        """Save task result"""
        try:
            if RESULTS_FILE.exists():
                with open(RESULTS_FILE, 'r') as f:
                    results = json.load(f)
            else:
                results = {}
            
            results[task_id] = {
                "result": result,
                "completed_at": datetime.now().isoformat()
            }
            
            with open(RESULTS_FILE, 'w') as f:
                json.dump(results, f, indent=2)
        except Exception as e:
            self.log(f"Failed to save result: {e}")
    
    def execute_task(self, task):
        """Execute a single task"""
        task_type = task.get("type")
        task_id = task.get("id", "unknown")
        
        self.log(f"Executing task {task_id}: {task_type}")
        self.update_dashboard("WORKING", f"Task: {task_type}")
        
        try:
            if task_type == "read_file":
                path = task.get("path")
                with open(path, 'r') as f:
                    result = f.read()
                self.save_result(task_id, {"success": True, "content": result})
                
            elif task_type == "write_file":
                path = task.get("path")
                content = task.get("content")
                Path(path).parent.mkdir(parents=True, exist_ok=True)
                with open(path, 'w') as f:
                    f.write(content)
                self.save_result(task_id, {"success": True, "path": path})
                
            elif task_type == "exec":
                command = task.get("command")
                result = subprocess.run(
                    command, 
                    shell=True, 
                    capture_output=True, 
                    text=True,
                    cwd=str(BASE_DIR),
                    timeout=60
                )
                self.save_result(task_id, {
                    "success": result.returncode == 0,
                    "stdout": result.stdout,
                    "stderr": result.stderr
                })
                
            elif task_type == "batch_write":
                files = task.get("files", [])
                for file_task in files:
                    path = file_task.get("path")
                    content = file_task.get("content")
                    Path(path).parent.mkdir(parents=True, exist_ok=True)
                    with open(path, 'w') as f:
                        f.write(content)
                self.save_result(task_id, {"success": True, "files_written": len(files)})
                
            else:
                self.save_result(task_id, {"success": False, "error": f"Unknown task type: {task_type}"})
                
            self.log(f"Task {task_id} completed")
            
        except Exception as e:
            self.log(f"Task {task_id} failed: {e}")
            self.save_result(task_id, {"success": False, "error": str(e)})
        
        self.update_dashboard("IDLE", "Waiting for tasks...")
    
    def run(self):
        """Main daemon loop"""
        self.log("Starting ARC Background Worker Daemon")
        self.log(f"Watching: {QUEUE_FILE}")
        self.update_dashboard("IDLE", "Daemon started, waiting for tasks...")
        
        while self.running:
            try:
                tasks = self.read_queue()
                
                if tasks:
                    self.log(f"Found {len(tasks)} task(s)")
                    self.clear_queue()  # Clear before processing
                    
                    for task in tasks:
                        self.execute_task(task)
                
                time.sleep(1)  # Poll every second
                
            except KeyboardInterrupt:
                self.log("Shutting down...")
                self.running = False
            except Exception as e:
                self.log(f"Error: {e}")
                time.sleep(1)
        
        self.update_dashboard("OFFLINE", "Daemon stopped")
        self.log("Daemon stopped")

if __name__ == "__main__":
    daemon = WorkerDaemon()
    daemon.run()
