---
description: Add a new phase to an existing roadmap
---

I need to add a new phase to my roadmap.

## Pre-Check: Load Context

**MANDATORY - Read these files FIRST:**
1. `.arc/PROJECT.md` - Understand what we're building
2. `.arc/ROADMAP.md` - See current phases
3. `.arc/STATE.md` - Check current progress

## Process

1. Show me the current ROADMAP.md phases

2. Ask me:
   - "What does this new phase need to accomplish?"
   - "Where should it go?" (options below)
     - **Before Phase [N]** - Insert and renumber
     - **After Phase [N]** - Insert and renumber  
     - **At the end** - Append as new final phase
     - **Replace Phase [N]** - Swap out an existing phase
   - "Is this blocking current work or can it wait?"

3. After I answer, update `.arc/ROADMAP.md`:
   - Insert the new phase at the specified position
   - Renumber all subsequent phases
   - Add a brief description (1-2 sentences)
   - Mark status as `⏳ Planned`

4. If inserting before the current phase:
   - Update `.arc/STATE.md` to reflect the renumbering
   - Warn me: "Note: Current phase number has changed"

5. Show me the updated roadmap and confirm:
   - "Phase [N] added. Run `/arc-discuss` or `/arc-plan` when ready."

## Phase Status Legend

Use these in ROADMAP.md:
- ⏳ Planned - Not started
- 🔄 In Progress - Currently working
- ✅ Complete - Done and verified
- ⏸️ Paused - Started but on hold
- ❌ Cancelled - No longer needed

## Example Update

**Before:**
```markdown
## Phases
1. ✅ Backend API
2. 🔄 Frontend UI
3. ⏳ Polish & Deploy
```

**After adding "Authentication" before Phase 2:**
```markdown
## Phases
1. ✅ Backend API
2. ⏳ Authentication ← NEW
3. 🔄 Frontend UI (was Phase 2)
4. ⏳ Polish & Deploy (was Phase 3)
```
