# CURRENT PROJECT STATE — LIFEPath INDIA

Last updated: 2026-10-24

## Repository
- GitHub: https://github.com/morevijay08/caffinnovators
- Initial repository contained LICENSE only.
- This workstream updates `.ai/` project-control files. No application/runtime files have been created or edited by this documentation change.

## Product
LifePath India — Interest-First Career Discovery and Personalized Learning Platform.
Tagline: Every Interest Has a Future.

## Approved stack
- Frontend: React + TypeScript + Vite + React Router + custom CSS.
- Backend: Python 3.11+ + FastAPI + Pydantic + Uvicorn.
- Testing: pytest for backend logic/API tests; frontend test tooling to be established in TASK-002.
- Data: static fictional/demo content; no database.
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
