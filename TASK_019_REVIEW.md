# TASK-019 — README and local setup documentation

Branch `task11` based on `task10`. Documentation-only update for Member 1.

## Changed
- Replaced the obsolete root README that described a Streamlit-only scaffold with verified-by-source React + FastAPI architecture, two-terminal commands, test commands, API endpoints, UI routes, demo flow and troubleshooting.
- Preserved the legacy Streamlit prototype files.
- Clarified current limitations: no database, login, persistence, readiness integration, roadmaps, affordability or running Gemma chatbot.
- Documented `VITE_API_BASE_URL` and `FRONTEND_ORIGIN` configuration, localhost ports and CORS expectations.

## Local verification checklist
- [ ] Check out task11 cleanly and read README.
- [ ] Start backend by running README's backend commands; check http://localhost:8000/health and /docs.
- [ ] Start frontend via README's npm commands; open http://localhost:5173/.
- [ ] Verify onboarding, interest assessment, recommendations, careers, change-path and dashboard routes.
- [ ] Run `python -m pytest -q` in backend; record actual pass count.
- [ ] Run `npm run build` in frontend; record actual output.
- [ ] Verify no extra external database or service is required.
- [ ] Confirm frontend restart or refresh resets session-only data.
- [ ] Review missing Member 3 integration notes with teammates before merging or demoing.

**Verification status:** Docs committed remotely; assistant did not run local server, npm build or pytest. No merge to `integration` or `main`.
