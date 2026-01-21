---
description: Verify a completed phase
---

Let's verify Phase [N] works correctly.

0. **Dashboard Initialization**:
   - Run `./venv/bin/python3 .agent/dashboard/update.py agent="Reviewer" status="WORKING" task="Verifying Phase [N]" main_status="AUDITING" main_action="Final Verification"`

Process:
1. Read .arc/planning/phase-[N]-SUMMARY.md
2. Extract what should be testable now
3. Walk me through testing EACH item:
   - Tell me what to test
   - Ask me if it worked (yes/no)
   - If yes: ask for evidence (screenshot/output)
   - If no: ask what went wrong

4. Create .arc/planning/phase-[N]-VERIFICATION.md with:
   - All test results
   - Evidence for passes
   - Issues list for failures

5. If any failures:
   - Create .arc/planning/phase-[N]-FIXES.md
   - List specific fix tasks
   - Ask if I want to execute fixes now

Use template at .arc/templates/VERIFICATION.md
