# THREE-MEMBER TEAM WORKFLOW — LIFEPath INDIA

## Purpose
Let three members build independent features in parallel while reducing merge conflicts. This document governs branch use, ownership, API contracts, reviews and integration.

## Roles at a glance
- **Member 1 — React frontend and integration:** app shell, design system, navigation, onboarding, dashboard, path switching, frontend API client, release coordination.
- **Member 2 — Career domain and backend:** interest assessment, career data, recommendations, career details/roadmaps, discovery activities and Gemma 4-powered Career Assistant API (TASK-014).
- **Member 3 — Readiness backend and tests:** timed math assessment, topic analysis, improvement/retest, fictional affordability demo data, API/service tests and test coordination.

See `.ai/roadmap/MEMBER_TASK_ASSIGNMENTS.md` for task IDs, dependencies and ownership.

## Before parallel coding
1. Member 1 coordinates TASK-002 to create the minimal React + TypeScript/Vite frontend and FastAPI backend skeleton.
2. Agree and document API contracts in `.ai/API_CONTRACTS.md` before parallel feature implementation.
3. Agree request/response schemas, error format, API base URL, local ports/CORS policy, temporary state assumptions and shared design tokens.
4. Member 2 owns career/interest API schema and service contracts; Member 3 owns readiness API schema and service contracts; Member 1 owns frontend client/types and integration.
5. If a dependency or interface is missing, do not guess. Ask the team to agree first.

## Branch model
- `main`: stable demo-ready code only.
- `integration`: shared integration branch; create it from `main` when the team starts implementation.
- Optional member branches: `member-1-frontend`, `member-2-career-api`, `member-3-readiness-api`.
- Use short-lived feature branches from latest `integration`, e.g. `feature/TASK-007-career-recommendations`.
- Never commit directly to `main` or `integration`.
- Open a pull request from a feature branch to `integration`; promote to `main` only after build, API checks and end-to-end smoke test pass.

## File ownership
- Member 1 owns `frontend/`, React pages/components, styles/design tokens, routing, frontend API client/types and frontend integration.
- Member 2 owns career/interest domain services and data under `backend/app/services/` and `backend/app/data/`, plus related schemas/routes assigned to career APIs.
- Member 3 owns readiness/performance services, math assessment data, readiness schemas/routes, SQLite persistence for anonymous assessment attempts, database configuration/models/repository, and related backend tests.
- For this approved SQLite change, Member 3 is the sole task owner for all database code, database schema/evolution, persistence endpoints, database documentation, and database-specific tests. Other members must coordinate before touching these files.
- Member 3 coordinates test coverage; every feature owner writes tests for their own logic.
- `.ai/API_CONTRACTS.md`, backend entry point/CORS, dependency files, shared frontend types/API client, `.ai/CURRENT_STATE.md` and logs are shared-sensitive; coordinate edits and assign one editor at a time.
- Do not have two members edit the same file in parallel. Agree changes to a contract before modifying both API and TypeScript types.

## Gemma 4 workflow
At the beginning of each coding session, use Gemma 4 when available and provide:
1. Required `.ai/` instruction files and API contracts.
2. Member number/role and assigned task ID.
3. Dependencies, acceptance criteria and allowed file paths.
4. Relevant request/response schema.
5. Instruction to inspect first, plan, implement only the task, run relevant checks, and show a diff summary.
Review all changes. If Gemma 4 is unavailable, disclose it; do not mislabel another model. The running Career Assistant is expected to use Gemma 4 at runtime through the backend adapter. Keep this separate from the development coding assistant.

## Standard feature workflow
1. Sync latest `integration`.
2. Create one task branch.
3. Inspect files and write a short plan.
4. Implement only assigned task and owned paths.
5. Run relevant frontend tests/build or backend tests/API checks.
6. Review diff/status and stage explicit paths.
7. Push branch and open PR into `integration`.
8. PR includes task ID, scope, files, tests/results, UI screenshots where applicable, API contract changes and known limitations.
9. Teammate reviews and owner addresses feedback.
10. Merge only when dependencies, tests and interfaces are satisfied.

## API integration rules
- API route handlers validate input and call service functions; they must not duplicate domain logic.
- Frontend components call the shared typed API client, not raw hardcoded URLs scattered across files.
- Keep Pydantic schemas and TypeScript types aligned with `.ai/API_CONTRACTS.md`.
- Configure local CORS for the actual frontend origin only.
- Use a consistent error format and handle loading, empty and failed requests in the UI.
- Do not add authentication or databases beyond the approved SQLite persistence for anonymous math-assessment attempts. Gemma 4 inference for TASK-014 is explicitly approved; use local Ollama by default and keep any hosted provider credentials server-side.

## Conflict prevention and resolution
- One owner per file per task; keep PRs small.
- Avoid broad formatting changes and unrelated refactors.
- Never force-push shared branches or blindly choose ours/theirs.
- If conflict occurs, affected owners agree on intended behavior; one resolver applies the combined change and runs tests.
- If a shared contract changes, notify all members and update the contract in a dedicated PR.

## Definition of ready to merge
- Acceptance criteria met and relevant checks actually run.
- No secrets, local environments, cache files or unrelated changes.
- No unapproved dependency or architecture changes.
- API contract and types agree.
- UI has useful loading/error/empty states and is checked at desktop and narrow widths where possible.

## Definition of integrated
A task is integrated only after its PR is merged to `integration` and the combined frontend/backend is checked. A branch push alone does not mean the feature is integrated or complete.


## Gemma 4 runtime integration
- Member 2 owns TASK-014's system prompt, model adapter/service and assistant route; Member 1 owns the React chat UI and typed API client; Member 3 coordinates timeout, unavailable-model and malformed-response tests.
- Local default: FastAPI calls Ollama at the configured backend URL; do not expose the Ollama endpoint to the browser.
- Do not make career matching or math scoring dependent on generated chatbot output. If the model is unavailable, show a clear recoverable error rather than pretending a rule-based answer came from Gemma 4.
- Confirm model tag and local hardware/runtime before the final demo; hosted inference is an explicit fallback decision, not a hidden substitution.
