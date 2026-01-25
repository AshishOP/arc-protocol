# Phase 4 Plan - Deployment & Final Polish

## Overview
The final phase focuses on shipping AUTHENT8 to production. We will deploy the FastAPI backend to Railway and the Next.js frontend to Vercel, ensuring all environment variables and OAuth callbacks are correctly configured for a live environment.

## Work Type
- Deployment (Railway, Vercel)
- Configuration (Environment Variables, CORS, OAuth)
- Testing (E2E)
- UI/UX Polish

## Technical Standards
- **Infrastructure:** Use Docker for the backend.
- **Security:** Ensure production environment variables are stored securely. No secrets in the codebase.
- **Performance:** Verify production builds for both backend and frontend.

## Tasks

### Task 1: Productization & Docker Audit
- **File Paths:** `backend/Dockerfile`, `backend/main.py`, `frontend/next.config.ts`
- **Steps:**
    1. Audit Dockerfile for production readiness (ensure all scanners are correctly installed).
    2. Configure production CORS in FastAPI to allow the Vercel domain.
    3. Ensure logging is set to INFO/ERROR for production.
- **Verification:** Docker image builds locally and API health check passes inside container.
- **Git Commit:** `chore: production readiness audit and docker optimization`
- **Delegation:** Use `Auditor` subagent to check for security misconfigurations.

### Task 2: Backend Deployment (Railway)
- **File Paths:** `backend/`, Railway Dashboard
- **Steps:**
    1. Connect GitHub repo to Railway.
    2. Setup PostgreSQL database on Railway (replacing local SQLite).
    3. Configure `DATABASE_URL`, `AI_API_KEY`, etc., in Railway.
- **Verification:** Backend is live and `/health` returns 200.
- **Git Commit:** `deploy: backend to railway`

### Task 3: Frontend Deployment (Vercel)
- **File Paths:** `frontend/`, Vercel Dashboard
- **Steps:**
    1. Connect GitHub repo to Vercel.
    2. Configure GitHub OAuth for the production domain (update homepage and callback URLs).
    3. Configure `NEXT_PUBLIC_BACKEND_URL`, `GITHUB_ID`, `GITHUB_SECRET`, `DATABASE_URL` (pointing to Railway PG).
- **Verification:** Frontend is live and user can sign in with GitHub.
- **Git Commit:** `deploy: frontend to vercel`

### Task 4: Final Polish & E2E Verification
- **File Paths:** Full Codebase
- **Steps:**
    1. Conduct E2E scans on real-world repositories.
    2. Fix any minor UI/UX issues (transitions, responsive behavior).
    3. Final check of the "Security Grade" logic.
- **Verification:** App is fully functional at the production URL.
- **Git Commit:** `chore: final polish and e2e verification`

## Ready to execute?
Run `/arc-execute phase 4` when ready.
