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

## TASK-007 implementation — branch task6 (2026-10-25)
- Deterministic recommendation service uses TASK-005 validated answers and TASK-006 illustrative career catalogue, keyed by stable career IDs.
- POST /api/v1/recommendations returns sorted career matches, evidence-based explanations, interest tags and exploration steps. React assessment result provides a button to fetch suggestions, with retry/error UI and links to career profiles.
- See TASK_007_REVIEW.md for the exact API shape, local testing steps, safety caveats and TASK-011 handoff.
- Branch `task6` extends `task5`; old incompatible Member 2 discovery branch not merged. Local pytest/frontend build/manual review not observed; integration pending.

## TASK-011 — Member 1 Change My Path (branch task7)
- Built React career-switching page `/change-path` against TASK-006 catalogue IDs, with confirmation, session-only current path and path history.
- Extended `StudentJourney` to retain completed TASK-005 assessment answers/signals and TASK-004 profile during client-side navigation; changes of career do not clear these.
- Connected assessment completion and TASK-007 recommendations to change-path UI; see `TASK_011_REVIEW.md`.
- No dashboard, database, durable storage or backend feature changes. Committed on GitHub; local build, pytest and browser acceptance still require confirmation. Branch chain task1 → task2 → task3 → task4 → task5 → task6 → task7.

## TASK-012 — Dashboard and three-career comparison (branch task8)
- Added `/dashboard` React route and navigation, with onboarding/interest/current-career summary from shared StudentJourney memory state.
- Added up-to-three career comparison against TASK-006 catalogue: summaries, interests, skills and profile links. Loading/error/empty states included.
- TASK-010 readiness result contract is not yet integrated: no readiness scores fabricated; this acceptance criterion remains pending. See `TASK_012_REVIEW.md`.
- Branch chain task1 → task2 → task3 → task4 → task5 → task6 → task7 → task8. GitHub file commits confirmed, local build/pytest/browser testing pending. No shared branch merge performed.

## TASK-016 — Feedback and recovery polish (task9)
- `task9` is based on `fix/task8-backend-tests`, preserving the two backend test expectation corrections and all TASK-002–TASK-012 branch work.
- Added reusable accessible FeedbackState loading/error/empty component, career catalogue error/empty/loading feedback, interest question reload retry, career recommendation error/empty feedback and updated onboarding summary copy.
- No new endpoints, dependencies, persistence, readiness data or Gemma integration. Review: `TASK_016_REVIEW.md`.
- User previously indicated the backend test fix was done; exact rerun stdout was not supplied. npm build, pytest and browser regression on task9 are unverified until the user tests.

## TASK-018 (task10) — cross-feature smoke testing
- Added `backend/tests/test_integration_smoke.py` covering the existing health → interest quiz → recommendations → catalogue details journey, plus safe errors and filters.
- Added `TASK_018_REVIEW.md` with browser validation steps and team handoff. `task10` is based on `task9` and preserves previous backend test corrections.
- The TASK-010 math analysis contract is still not integrated into this task series, so **full all-member end-to-end verification remains incomplete**. Actual local pytest/build/browser test results remain pending.

## TASK-019 — README & setup (task11)
- Replaced stale Streamlit-only README with current React/Vite + FastAPI two-terminal Windows and macOS/Linux instructions, exact UI/API routes, environment variables, tests, architecture, known limitations, legacy prototype note and troubleshooting.
- Branch task11 based on task10. Review details in TASK_019_REVIEW.md. No application code, runtime dependencies, database or shared branches changed. Local verification still pending.

## TASK-020 — Member 1 demo planning and final review (task12)
- `task12` extends `task11` and adds HACKATHON_DEMO_SCRIPT.md with a five-minute walkthrough and realistic judge Q&A.
- Added TASK_020_REVIEW.md with full test gates, team signoffs, browser walkthrough, and final integration PR/merge review.
- This is documentary delivery only: no source-code or dependency changes, no claims that member 2/3 features have been integrated, and no claims that local tests are already green. Readiness is pending real verification on task12 and shared integration branch.

## TASK-008 — Member 2 career roadmaps (task13)
- Branch `task13` extends `task12` and adds `GET /api/v1/careers/{career_id}/roadmap`, Pydantic models, deterministic four-stage illustrative roadmaps for all twelve catalogue careers, React career-profile timeline, responsive CSS and dedicated API tests.
- Existing career detail response shape remains unchanged; typed frontend fetch calls the new child endpoint. Safe 404, loading/retry and disclaimers included. Contract appended to .ai/API_CONTRACTS.md. See TASK_008_REVIEW.md.
- GitHub commits complete. Build, pytest, browser acceptance and shared team integration remain unverified; no merge to main/integration.

## TASK-013 — Member 2 Discovery Lab (task14)
- Added six illustrative activities, typed GET /api/v1/discovery-activities with interest filter, React /discovery-lab page and temporary reflection state. See TASK_013_REVIEW.md.
- Four backend tests added; local execution and browser build unverified. No database, aptitude diagnosis or score; no shared merge.
