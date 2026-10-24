# CURRENT PROJECT STATE — LIFEPath INDIA

Last updated: 2026-10-24

## Repository
- GitHub: https://github.com/morevijay08/caffinnovators
- Initial repository contained LICENSE only.
- The Member 3 TASK-009A branch updates `.ai/` project-control files and introduces SQLite persistence code/tests. Runtime behavior remains unverified until local tests and smoke checks pass.

## Product
LifePath India — Interest-First Career Discovery and Personalized Learning Platform.
Tagline: Every Interest Has a Future.

## Approved stack
- Frontend: React + TypeScript + Vite + React Router + custom CSS.
- Backend: Python 3.11+ + FastAPI + Pydantic + Uvicorn.
- Testing: pytest for backend logic/API tests; frontend test tooling to be established in TASK-002.
- Data: static fictional/demo content plus SQLite persistence for anonymous math-assessment attempt results only (approved 2026-10-24; implementation pending verification).
- No student accounts or durable student profiles.
- See `.ai/TECH_STACK.md` and `.ai/ARCHITECTURE.md`.

## Development AI assistant
- Gemma 4 is the preferred coding assistant whenever available in the team's chosen environment.
- Gemma 4 is explicitly approved as the student-facing runtime model for the Career Assistant (TASK-014), separate from its optional use as a coding assistant. Default runtime path: FastAPI → local Ollama → configurable Gemma 4 model (`GEMMA_MODEL`, initial default `gemma4:e2b`). A hosted API key is not required for the default local setup.

## Team
- Three workstreams are defined in `.ai/TEAM_WORKFLOW.md`.
- Task ownership and dependencies are defined in `.ai/roadmap/MEMBER_TASK_ASSIGNMENTS.md`.
- Frontend/backend interface shapes are defined in `.ai/API_CONTRACTS.md`.
- Parallel implementation starts after TASK-002 establishes the skeleton and shared API contracts are agreed and merged into `integration`.

## Current phase
Phase 0 — Product contract and AI control system.

## Current task
TASK-001 — DONE. Project definition/control documentation is recorded as done. This change updates architecture decisions in response to the user's explicit approval to switch to React + TypeScript.

## Next milestone
TASK-002 — Initialize React + TypeScript/Vite frontend and FastAPI backend skeleton, configure local development, and establish API contract baseline. Member 1 coordinates; Members 2 and 3 review backend/service boundaries. Runtime implementation must be explicitly started by the user.

## Verification
- Existing stack, architecture, roadmap, assignment and task files were fetched and reviewed before updating.
- Documentation and task planning are being updated to reflect the user's approved architecture choice.
- No runtime code, package installation, app launch or tests are claimed as part of this documentation update.

## Completion standard
A task is complete only when its acceptance criteria are checked and relevant validation evidence exists. Creating documentation alone does not prove application functionality.


## Approved runtime AI change (2026-10-24)
- The user explicitly requires Gemma 4 to power the student-facing chatbot at runtime.
- TASK-014 is a real model integration behind FastAPI; local Ollama is the default. Initial configurable defaults are `OLLAMA_BASE_URL=http://localhost:11434` and `GEMMA_MODEL=gemma4:e2b`.
- Hosted inference is optional only by explicit team decision. Deterministic career matching and assessment scoring are unchanged.
- Documentation is updated/planned; no runtime model call or chatbot implementation is claimed yet.


## Approved SQLite architecture change (2026-10-24)
- User approved SQLite for anonymous math-assessment attempts; database integration and `.ai/` contract updates are assigned to Member 3.
- Planned storage: server-calculated score summary, topic breakdown snapshot, elapsed seconds, assessment version and server timestamp. Do not persist student names or answer-by-answer submissions in this task.
- SQLAlchemy is the ORM; SQLite is the only approved database for this scope. Database file is local and must be gitignored; `DATABASE_URL` may override the default.
- Proposed endpoint: `GET /api/v1/math-assessment/attempts/{attempt_id}` to retrieve a saved attempt by opaque UUID. UUID is not authentication.
- Status: branch created; implementation and tests are in progress. Do not claim the database is verified until tests and restart-persistence smoke test pass.
