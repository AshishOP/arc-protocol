#!/usr/bin/env python3
"""
ARC Protocol - Velocity Tracker
Track development velocity and productivity metrics
"""
import json
import os
from datetime import datetime, timedelta

STATE_FILE = ".arc/arc_workflow_state.json"
VELOCITY_FILE = ".arc/velocity_history.json"

def load_velocity_history():
    if os.path.exists(VELOCITY_FILE):
        with open(VELOCITY_FILE, 'r') as f:
            return json.load(f)
    return {"sessions": [], "total_tasks": 0, "total_time_minutes": 0}

def save_velocity_history(data):
    with open(VELOCITY_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def track_session(tasks_completed, time_minutes):
    """Record a completed session"""
    history = load_velocity_history()
    
    session = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "tasks": tasks_completed,
        "time_minutes": time_minutes,
        "velocity": round(tasks_completed / (time_minutes / 60), 2) if time_minutes > 0 else 0
    }
    
    history["sessions"].append(session)
    history["total_tasks"] += tasks_completed
    history["total_time_minutes"] += time_minutes
    
    save_velocity_history(history)
    print(f"📊 Session tracked: {tasks_completed} tasks in {time_minutes}m (velocity: {session['velocity']} tasks/hour)")

def show_velocity_report():
    """Display velocity metrics"""
    history = load_velocity_history()
    
    if not history["sessions"]:
        print("⚠️  No sessions tracked yet. Complete some tasks first!")
        return
    
    recent_sessions = history["sessions"][-5:]  # Last 5 sessions
    avg_velocity = sum(s["velocity"] for s in recent_sessions) / len(recent_sessions)
    
    total_hours = history["total_time_minutes"] / 60
    overall_velocity = history["total_tasks"] / total_hours if total_hours > 0 else 0
    
    print("\n📊 ARC Velocity Report")
    print("=" * 50)
    print(f"Total Tasks Completed: {history['total_tasks']}")
    print(f"Total Time Invested: {int(total_hours)}h {int(history['total_time_minutes'] % 60)}m")
    print(f"Overall Velocity: {overall_velocity:.2f} tasks/hour")
    print(f"\nRecent Velocity (last 5): {avg_velocity:.2f} tasks/hour")
    print("\nRecent Sessions:")
    for s in reversed(recent_sessions):
        print(f"  {s['date']}: {s['tasks']} tasks in {s['time_minutes']}m ({s['velocity']} t/h)")
    print("=" * 50)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "track":
            tasks = int(sys.argv[2])
            time_m = int(sys.argv[3])
            track_session(tasks, time_m)
        elif sys.argv[1] == "report":
            show_velocity_report()
    else:
        show_velocity_report()
