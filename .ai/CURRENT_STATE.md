# CURRENT PROJECT STATE — LIFEPath INDIA

Last updated: 2026-10-25

## Repository
- GitHub: https://github.com/morevijay08/caffinnovators
- The `integration` branch contains the shared application scaffold and math readiness API.
- The Member 3 TASK-009A feature branch adds SQLite persistence for anonymous math-assessment attempts. Verify combined behavior before marking it complete.

## Product
LifePath India — Interest-First Career Discovery and Personalized Learning Platform.

Tagline: Every Interest Has a Future.

## Approved stack
- Frontend: React + TypeScript + Vite + React Router + custom CSS.
- Backend: Python 3.11+ + FastAPI + Pydantic + Uvicorn.
- Testing: pytest for backend logic and API tests.
- Assessment data: static, fictional practice questions.
- Persistence: SQLite for anonymous math-assessment result summaries only.
- No student accounts or durable student profiles are introduced by TASK-009A.
- See `.ai/TECH_STACK.md` and `.ai/ARCHITECTURE.md`.

## Development AI assistant
- Gemma 4 is the preferred coding assistant when available.
- Gemma 4 is approved as the student-facing runtime model for the Career Assistant (TASK-014).
- Default runtime path: FastAPI → local Ollama → configurable Gemma 4 model (`GEMMA_MODEL`, initial default `gemma4:e2b`).
- A hosted API key is not required for the default local setup.

## Team and coordination
- Three workstreams are defined in `.ai/TEAM_WORKFLOW.md`.
- Task ownership and dependencies are defined in `.ai/roadmap/MEMBER_TASK_ASSIGNMENTS.md`.
- Frontend/backend interfaces are defined in `.ai/API_CONTRACTS.md`.
- Work must be integrated through pull requests. Do not commit directly to `main` or `integration`.

## Current phase
Phase 0 — Product contract, shared application foundation, and feature implementation.

## Current task
TASK-009 — Timed Math Readiness Assessment.

- The assessment question bank, schemas, deterministic scoring service, and API router are implemented on `integration`.
- TASK-009A adds persistence for anonymous assessment results using SQLAlchemy and SQLite.
- Planned storage includes the server-calculated score summary, topic breakdown, elapsed time, assessment version, and server timestamp.
- Do not store student names or answer-by-answer submissions in this task.
- The database file must remain local and gitignored. `DATABASE_URL` may override the default SQLite location.
- The proposed retrieval endpoint is `GET /api/v1/math-assessment/attempts/{attempt_id}`. An opaque UUID is not authentication.

## Verification status
- The shared math readiness API was tested on `integration`; eight backend tests passed in the reported run.
- The API health check and math assessment GET/POST endpoints were smoke-tested locally.
- SQLite persistence and retrieval must be verified with the combined backend test suite and a restart-persistence smoke test before TASK-009A is marked complete.
- Client-reported elapsed time is informational and is not tamper-proof server-enforced timing.
- Do not claim any test or runtime verification that has not actually been performed.

## Next steps
1. Resolve conflicts while preserving the current `integration` application and the TASK-009A persistence feature.
2. Install dependencies from `backend/requirements.txt` and run `python -m pytest -v` from `backend/`.
3. Verify submission returns an `attempt_id` and retrieval returns the saved result.
4. Confirm the saved attempt survives a server restart.
5. Update task documentation only after the corresponding checks pass.

## Completion standard
A task is complete only when its acceptance criteria are satisfied and relevant validation evidence exists. Documentation alone does not prove application functionality.

## Approved runtime AI change (2026-10-24)
- TASK-014 requires a real Gemma 4-backed Career Assistant behind FastAPI.
- Local Ollama is the default inference path, with `OLLAMA_BASE_URL=http://localhost:11434` and `GEMMA_MODEL=gemma4:e2b` as initial defaults.
- Deterministic career matching and math assessment scoring remain separate from LLM inference.
- Do not claim unverified runtime integration.

## Approved SQLite architecture change (2026-10-24)
- SQLite is approved for anonymous math-assessment attempt summaries.
- SQLAlchemy is the ORM; SQLite is the only approved database for this task.
- The attempt UUID provides lookup, not authentication.
- Keep the database file out of Git.
- Mark persistence verified only after tests and restart-persistence checks pass.
