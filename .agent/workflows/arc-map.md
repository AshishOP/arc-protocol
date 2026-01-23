---
description: Map and understand an existing codebase before modifying it
---

I want to understand this existing codebase before making changes.

0. **Dashboard Sync**:
   - Run `./venv/bin/python3 .agent/dashboard/update.py agent="Architect" status="WORKING" task="Mapping Codebase" main_status="ANALYZING" main_action="Codebase Discovery"`

## Pre-Mapping: Load All Context

**MANDATORY - Read these files FIRST:**
1. `.arc/PROJECT.md` - Understand the vision
2. `.arc/CONTRACTS.md` - Check for any existing standards
3. `.arc/STATE.md` - Check current session state

## Codebase Analysis Process

1. **Scan the project structure:**
   - List all top-level directories
   - Identify the tech stack from package.json, requirements.txt, etc.
   - Find configuration files (.env.example, config/, etc.)

2. **Analyze architecture:**
   - Frontend framework and structure
   - Backend framework and structure
   - Database/storage approach
   - API patterns (REST, GraphQL, etc.)

3. **Identify conventions:**
   - Naming patterns (files, functions, components)
   - Code style (formatting, imports organization)
   - Testing patterns (if tests exist)
   - Error handling patterns

4. **Find existing contracts:**
   - API endpoints (routes, handlers)
   - Data models/schemas
   - Environment variables used
   - Shared utilities/helpers

5. **Create `.arc/CODEBASE.md`:**

```markdown
# Codebase Map

## Generated
[Current date/time]

## Tech Stack
| Layer | Technology | Version |
|-------|------------|---------|
| Frontend | | |
| Backend | | |
| Database | | |
| Deployment | | |

## Project Structure
```
/
├── [directory descriptions]
```

## Architecture Pattern
[Describe: monolith, microservices, serverless, etc.]

## Key Files
| File | Purpose |
|------|---------|
| | |

## Existing Patterns

### Naming Conventions
- Files: [pattern]
- Components: [pattern]
- Functions: [pattern]

### Code Patterns
- State management: [approach]
- API calls: [pattern]
- Error handling: [pattern]

### Testing
- Framework: [if any]
- Coverage: [if measurable]

## Existing Endpoints
| Method | Route | Purpose |
|--------|-------|---------|
| | | |

## Data Models
[List discovered models/schemas]

## Environment Variables
| Variable | Purpose |
|----------|---------|
| | |

## Potential Issues
- [Any code smells, outdated deps, etc.]

## Entry Points
- Development: [how to run locally]
- API: [main entry file]
- Frontend: [main entry file]
```

6. **Auto-populate CONTRACTS.md:**
   - Add discovered endpoints to Section 1
   - Add discovered models to Section 2
   - Add discovered env vars to Section 5
   - Add file structure to Section 6
   - Note in Update Log: "Auto-populated from codebase mapping"

7. **Report to user:**
   - Summary of what was found
   - Any concerns or questions
   - Suggest: "Ready to start? Run `/arc-new` to define your project goals, or `/arc-plan` if roadmap exists."

## When to Use This

✅ Use when:
- Joining a new team's codebase
- Resuming an old project
- Before major refactoring
- Contributing to open source

❌ Skip when:
- Starting a completely new project
- You just wrote this code yourself
