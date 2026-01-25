# Phase 4 Context - Deployment & Final Polish

## Work Type
- Hosting (Railway, Vercel)
- Production Ops
- Q&A

## Decided Preferences
| Decision | My Choice | Rationale |
|----------|-----------|-----------|
| DB | Postgres (Production) | SQLite is for local, Postgres for Railway scalability |
| Scanners | Pre-installed in Docker | Avoid runtime installation lag |
| CORS | Strict Domain | Allow only Vercel frontend |
| Logs | Info | Production visibility |

## Constraints Noted
- Final 4-6 hour window (Total 24h hackathon target).
- Zero-downtime transition from local to live.

## References
- Railway Docs: Docker deployments.
- Vercel Docs: Next.js + NextAuth production setup.
