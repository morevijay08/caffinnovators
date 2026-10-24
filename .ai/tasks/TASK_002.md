# TASK-002 — Initialize React + TypeScript frontend and FastAPI backend skeleton

Status: NOT STARTED. This is the first runtime task. Do not begin unless the user explicitly asks to start application implementation.

## Goal
Create the smallest runnable full-stack skeleton for LifePath India, with a React + TypeScript frontend and Python FastAPI backend, and establish the initial API contract baseline. Do not implement feature journeys yet.

## Read first
- `.ai/PROJECT_CONTEXT.md`
- `.ai/AI_RULES.md`
- `.ai/TECH_STACK.md`
- `.ai/ARCHITECTURE.md`
- `.ai/API_CONTRACTS.md`
- `.ai/TEAM_WORKFLOW.md`
- `.ai/roadmap/MASTER_ROADMAP.md`
- `.ai/roadmap/MEMBER_TASK_ASSIGNMENTS.md`

## In scope
- Inspect the existing repository and preserve existing files.
- Create `frontend/` React + TypeScript + Vite scaffold with a minimal LifePath India shell.
- Create `backend/` FastAPI scaffold with `backend/app/main.py` and a health endpoint.
- Add frontend package scripts and backend dependency file with only necessary approved dependencies.
- Configure one frontend API base URL and safe local CORS for the frontend origin.
- Add `.gitignore` entries for Node/Python environments, build outputs, caches and local env files.
- Add accurate README instructions for installing and running both processes.
- Establish and follow `.ai/API_CONTRACTS.md`; agree the initial health/error response shapes with Members 2 and 3.
- Add minimal frontend/backend smoke checks supported by the selected test tooling.

## Out of scope
- Real assessments, career recommendations, catalogue, dashboards or other feature logic.
- Database, authentication, persistence, hosted AI, API keys or external services.
- Next.js, a second frontend framework, Tailwind/Bootstrap, or unapproved packages.
- Rewriting all task assignments or implementing later tasks.

## Acceptance criteria
- [ ] Frontend starts using the documented npm command.
- [ ] TypeScript/Vite production build succeeds.
- [ ] FastAPI starts using the documented Python command.
- [ ] Health endpoint returns the documented JSON response.
- [ ] Frontend can call the health endpoint using the configured API base URL.
- [ ] CORS is limited to the intended local frontend origin.
- [ ] Frontend/backend setup commands and dependencies are documented.
- [ ] No database, API key or external service is required.
- [ ] Relevant checks are run and results recorded truthfully.
- [ ] `.ai/CURRENT_STATE.md`, progress log and changelog are updated after verification.

## Verification
Record exact commands and outcomes for frontend installation/build, backend tests or health check, and frontend-to-backend connection. Do not mark DONE if any check was skipped or failed; document blockers.
