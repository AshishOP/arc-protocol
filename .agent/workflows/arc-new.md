---
description: Initialize a new ARC project
---

I want to initialize a new ARC project. Follow this process:

0. **Dashboard Initialization**:
   - Run `./venv/bin/python3 .agent/dashboard/update.py project="New Project" phase="Initialization" main_status="SETUP" main_action="Discovery Phase"`
   - Provide the user with the command: `./dash`

## Pre-Check: System Alignment
1. Check if `.arc/` directory already exists. 
2. If it exists, warn the user and suggest `/arc-map` instead.

1. ASK ME QUESTIONS
   - What are you building?
   - Why does it need to exist?
   - Who is it for?
   - What's the ONE core goal?
   - What tech stack?
   - What are you NOT building in v1?
   - What are your constraints (time/scope)?
   - How will you know it's successful?

2. After I answer all questions, create:
   - .arc/PROJECT.md (use template at .arc/templates/PROJECT.md)
   - .arc/ROADMAP.md with suggested phases

3. Show me the roadmap and ask if I want to adjust phases.

Don't start building yet. Just create the planning documents.
