# CURRENT PROJECT STATE — LifePath India

Last reviewed: 2026-10-24 (Member 1 workstream, branch `task3`)

## Source-of-truth and branch safety
- Repository: https://github.com/morevijay08/caffinnovators
- **This snapshot describes `task3`, not necessarily `main` or `integration`.** Other members may have newer changes. Always fetch the live branch and its .ai files before editing.
- Original Streamlit prototype remains in root files; it is legacy, not the approved target architecture. Do not delete it without a coordinated decision.
- Task branches build sequentially: `task1` (TASK-002 scaffold) → `task2` (TASK-003 landing) → `task3` (TASK-004 onboarding). Their pushes do not by themselves mean those tasks are integrated into `integration`.

## Project and locked stack
LifePath India — Every Interest Has a Future. Interest-first career guidance with explainable pathways and non-judgmental improvement feedback.
- Frontend: React, TypeScript, Vite, React Router, plain CSS, Fetch API.
- Backend: Python 3.11+, FastAPI, Pydantic, Uvicorn; pytest for backend tests.
- Demo data; no database or authentication. Temporary onboarding data lives in React memory and resets on full reload.
- Gemma 4 is the preferred development coding assistant when available and the approved runtime Career Assistant for TASK-014, through FastAPI → Ollama; **not** implemented by TASK-004.

## Verified current implementation on `task3`
- TASK-002 files: React/Vite app, shared typed API health client, FastAPI GET /health, backend smoke tests and setup instructions (`TASK_002_SETUP.md`).
- TASK-003 files: responsive landing page, site header/footer, informational career cluster cards, working internal links (`TASK_003_REVIEW.md`).
- TASK-004 files: `frontend/src/pages/OnboardingPage.tsx`, `frontend/src/state/StudentJourney.tsx`, `frontend/src/styles/onboarding.css`, and route/CTA wiring. Three-step onboarding: education level, interests + optional favourite subjects, goal + conditional career idea; validation, summary, edit, clear (`TASK_004_REVIEW.md`).
- User confirmed the React app launched under Vite on localhost:5173 and subsequently confirmed the onboarding route opened after correcting the browser URL. User earlier reported TASK-002 and TASK-003 review as done, but exact build/test command output was not supplied here. Treat comprehensive automated verification as outstanding until recorded.
- Incorrect URL `/onboarding**?utm_source=chatgpt.com` rendered the intended React 404 route; **correct URL is `http://localhost:5173/onboarding`**. No routing defect established.

## Next gate / pending checks
1. Member 1 runs `cd frontend && npm run build`, reviews all onboarding steps, validation, editing, clearing and responsive layout, and documents actual results.
2. Verify backend tests from `backend/` and frontend ↔ FastAPI health response where relevant.
3. Review and merge task branches to `integration` through PRs; no direct pushes to shared branches.
4. TASK-011 (Change My Path) requires the onboarding state contract and Member 2 recommendation data/API contract (TASK-007). Do not fabricate dependent APIs; check their state on `integration` before implementing.

## Coordination rule
Read `.ai/AI_RULES.md`, `.ai/TECH_STACK.md`, `.ai/API_CONTRACTS.md`, `.ai/TEAM_WORKFLOW.md`, roadmap, assignments, and current task documentation on the *actual working branch* at every new task. Preserve decisions from other member branches; update progress only with observed facts.

## TASK-005 branch work (2026-10-25, branch task4)
- New branch `task4` based on `task3`; other Member 2 TASK-007 branch was not merged.
- Implemented six-question illustrative interest assessment, deterministic Python scoring, Pydantic schemas, GET/POST FastAPI routes, API tests, React timed UI and onboarding navigation.
- Task details and exact manual checks are in `TASK_005_REVIEW.md`.
- No backend server-enforced timeout and no durable result persistence. Career recommendations belong to TASK-007.
- GitHub file commits completed; npm build, pytest and browser interaction checks require local user verification. **Do not mark DONE or merged yet.**
- Next Member 2 task once tested: TASK-006 career catalogue. Career ranking TASK-007 requires TASK-005 and TASK-006 to share signals/tags.

## TASK-006 implementation (branch task5)
- Built illustrative twelve-career dataset, catalogue service, FastAPI GET /api/v1/careers with search/cluster, GET /api/v1/careers/{career_id}, typed React Career Explorer and detail pages.
- TASK-005 signal tags are aligned with career interest_tags; no recommendation ranking until TASK-007.
- GitHub implementation committed, but browser tests, npm build and pytest still require user verification. See TASK_006_REVIEW.md.
- Branch chain: task1 → task2 → task3 → task4 → task5. Shared integration merge remains separate.
