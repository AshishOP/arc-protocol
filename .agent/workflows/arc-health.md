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
   - Confirm count: 14 expected

6. **Check Subagents**:
   - ✅ Verify `npm list -g @google/generative-ai` (Gemini CLI)
   - ✅ Verify `gemini --version`
   - ✅ Check if `~/.config/gemini/config.json` (or equivalent) exists (Authentication)

7. **Report**:

```markdown
# ARC Health Report

## ✅ Installation
- ARC folders: OK
- Virtual environment: OK
- Dependencies: rich installed
- Dashboard shortcut: OK

## 🤖 Subagents (The Fleet)
- Gemini CLI: [OK / Missing]
- Authentication: [Logged In / Not Authenticated]
- Bridge Connection: [Active / Inactive]

## ⚠️ Project Setup
...
```

8. **Fix Common Issues**:
...
- If Subagents missing: "Run: npm install -g @google/generative-ai && gemini login"
- If Authentication missing: "Run: gemini login"
