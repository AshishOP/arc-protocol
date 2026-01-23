---
description: Check ARC system health and configuration
---

# ARC Health Check

Run a diagnostic on your ARC installation and project setup.

## Process

1. **Check Installation**:
   - ✅ Verify `.arc/` folder exists
   - ✅ Verify `.agent/workflows/` folder exists
   - ✅ Verify `venv/` exists and has `rich` installed
   - ✅ Verify `dash` command is in PATH

2. **Check Project Files**:
   - `.arc/PROJECT.md` - Project definition
   - `.arc/ROADMAP.md` - Phase planning
   - `.arc/CONTRACTS.md` - Shared definitions
   - `.arc/STATE.md` - Session state

3. **Check Templates**:
   - Count templates in `.arc/templates/`
   - Verify all required templates exist

4. **Check Dashboard**:
   - Verify `.agent/dashboard/monitor.py` exists
   - Verify `.agent/dashboard/update.py` exists
   - Check if state file `.arc/arc_workflow_state.json` exists

5. **Check Workflows**:
   - List all workflows in `.agent/workflows/`
   - Confirm count: 13 expected

6. **Report**:

```markdown
# ARC Health Report

## ✅ Installation
- ARC folders: OK
- Virtual environment: OK
- Dependencies: rich installed
- Dashboard shortcut: OK

## ⚠️ Project Setup
- PROJECT.md: Missing (run /arc-new)
- ROADMAP.md: Missing (run /arc-new)
- CONTRACTS.md: Empty template
- STATE.md: Not initialized

## 📊 System
- Templates: 9/9 found
- Workflows: 13/13 found
- Skills: 6 found
- Dashboard: Functional

## 🎯 Next Steps
1. Run `/arc-new` to initialize your project
2. Run `dash` to open the dashboard
```

7. **Fix Common Issues**:
   - If venv missing: "Run: python3 -m venv venv"
   - If rich missing: "Run: ./venv/bin/pip install rich"
   - If PROJECT.md missing: "Run /arc-new to initialize"
