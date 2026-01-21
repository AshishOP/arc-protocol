---
description: Discuss and capture preferences before planning a phase
---

I want to discuss Phase [N] before planning it.

## Pre-Discussion: Load Context

**MANDATORY - Read these files FIRST:**
1. `.arc/PROJECT.md` - Understand what we're building
2. `.arc/ROADMAP.md` - See what this phase should accomplish
3. `.arc/CONTRACTS.md` - Know existing patterns and conventions

## Discussion Process

1. **Dashboard Initialization**:
   - Run `./venv/bin/python3 .agent/dashboard/update.py agent="Architect" status="THINKING" task="Discussing Phase [N]" main_status="PLANNING" main_action="Phase Discussion"`

2. Show me what Phase [N] is about (from ROADMAP.md)

2. Identify the **type of work** in this phase:
   - **UI/UX work** → Ask about layout, interactions, empty states, mobile
   - **API/Backend** → Ask about response format, error handling, validation
   - **Data/Storage** → Ask about schema, caching, migrations
   - **Integration** → Ask about external APIs, auth, rate limits
   - **DevOps** → Ask about deployment, monitoring, secrets

3. Ask me preference questions based on the work type:

   **For UI work:**
   - Layout preference? (cards/table/list/grid)
   - Loading pattern? (pagination/infinite scroll/load more)
   - Empty states? (illustration/text only/CTA)
   - Error display? (inline/toast/modal)
   - Mobile approach? (responsive/mobile-first/desktop-only)

   **For API work:**
   - Response format? (REST conventions/custom)
   - Error structure? (HTTP codes only/detailed objects)
   - Validation style? (strict/lenient)
   - Rate limiting? (yes/no/token-based)

   **For Data work:**
   - Storage engine preference?
   - Caching strategy?
   - Data retention rules?

4. After I answer, create `.arc/planning/phase-[N]-CONTEXT.md`:

```markdown
# Phase [N] Context - [Phase Name]

## Work Type
[UI/API/Data/etc.]

## Decided Preferences
| Decision | My Choice | Rationale |
|----------|-----------|-----------|
| Layout | Cards | Better for scan results |
| Loading | Pagination | Simpler for MVP |

## Constraints Noted
- [Any constraints I mentioned]

## References
- Similar to: [any examples I mentioned]
- Avoid: [anything I said to avoid]

## Open Questions
- [Anything still undecided for planning phase]
```

5. Confirm the CONTEXT.md is saved and ask:
   "Ready to plan this phase? Run `/arc-plan` when ready."

## Why This Matters

This step ensures the planning phase doesn't guess about:
- Your visual preferences
- Technical approach
- Patterns you want to follow
- Things you explicitly want to avoid

The planner will READ this context file before creating tasks.
