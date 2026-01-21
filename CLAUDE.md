# ARC Protocol Rules for Claude Code

You are an AI-powered software engineer using the **ARC (Analyze, Run, Confirm) Protocol**. Your primary goal is to maintain absolute context through the `.arc/` directory and keep the user updated via the **ARC Dashboard**.

Refer to `README.md` for full context.

## 📊 Dashboard Integration
You MUST update the dashboard before and after every major action using the following command:
```bash
python .agent/dashboard/update.py "Updating state..." --status "Executing" --step "Phase X: Task Y"
```

## 📜 ARC Commands
Always use the ARC workflows for consistency:
- `/arc-new`: Start a new project.
- `/arc-plan`: Plan the next phase.
- `/arc-execute`: Execute the current plan.
- `/arc-verify`: Verify the work done.
- `/arc-status`: Check project status.
- `/arc-resume`: Resume a session.
- `/arc-pause`: Save state and pause.
- `/arc-quick`: Handle ad-hoc tasks.

## 📁 Key Files
- `README.md`: Protocol overview.
- `.arc/templates/`: Master templates for workflows.
- `.arc/state/STATE.md`: Current execution context.
- `.arc/planning/ROADMAP.md`: Project milestones.
- `.arc/PHASE-PLAN.md`: Active phase details.

## 🛡️ Best Practices
1. **Never skip the dashboard**: It is the user's only visibility into your internal state.
2. **Commit often**: Use descriptive commit messages.
3. **Verify everything**: Do not consider a task done until it passes `/arc-verify`.
4. **Skills first**: Always check `.agent/skills/` for domain-specific expertise.
