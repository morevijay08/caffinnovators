# CHANGELOG — LIFEPath INDIA

## 2026-10-24 — Project control baseline
- Added LifePath-specific agent instructions, project context, architecture, coding standards, stack lock, decisions, current state and known issues.
- Added ordered roadmap, phased notes, task template and task definitions.
- Preserved the existing LICENSE.
- Re-inspected the GitHub tree and key control files.
- No runtime implementation was included in this documentation-only milestone.

## 2026-10-24 — Gemma 4 and team collaboration plan
- Updated AI_MASTER_PROMPT.md and AI_RULES.md to prefer Gemma 4 for development assistance when available.
- Updated TECH_STACK.md to state that Gemma 4 is not a student-facing runtime dependency.
- Added TEAM_WORKFLOW.md with branch strategy, ownership boundaries, PR checks and conflict-resolution rules.
- Added MEMBER_TASK_ASSIGNMENTS.md mapping all roadmap tasks to the three member roles and identifying dependencies.
- Updated MASTER_ROADMAP.md and CURRENT_STATE.md for dependency-aware parallel delivery.
- No application/runtime code, Gemma API integration, package installation or app tests were added.

## 2026-10-24 — Approved switch to React + TypeScript and FastAPI
- Recorded explicit user approval for React + TypeScript + Vite frontend and Python FastAPI backend in ADR-007; marked the previous Streamlit-only ADR-002 as superseded.
- Updated TECH_STACK.md, ARCHITECTURE.md, PROJECT_CONTEXT.md, AI_MASTER_PROMPT.md, AI_RULES.md, CURRENT_STATE.md, TEAM_WORKFLOW.md, MASTER_ROADMAP.md, MEMBER_TASK_ASSIGNMENTS.md and TASK_002.md.
- Added API_CONTRACTS.md to define the initial health endpoint, API conventions, planned endpoint inventory, shared data shapes and contract ownership.
- Kept the MVP database-free and independent of paid APIs, secrets and runtime LLM services.
- Documentation-only update: no runtime code was created, installed, launched or tested.


## 2026-10-24 — Gemma 4 approved as student-facing runtime model
- Superseded the earlier simulated/rule-based Career Assistant decision for TASK-014.
- Approved Gemma 4 runtime inference behind FastAPI, using local Ollama by default and configurable model/base URL; hosted inference remains an explicit fallback decision.
- Updated stack, architecture, AI instructions, project context, decisions, current state, team workflow, roadmap, member assignments and API contracts.
- Added a detailed TASK-014 specification for request/response shape, safe prompt behavior, runtime configuration, failure handling and member ownership.
- Documentation-only update; no runtime integration or tests are claimed.


## 2026-10-24 — Member 1 task branch implementation and state reconciliation
- Branch `task1`: React/Vite frontend, typed health API client, FastAPI /health scaffold and smoke tests.
- Branch `task2`: landing page design system, header/footer and responsive navigation.
- Branch `task3`: 3-step onboarding, typed temporary React context, required-field validation, review/edit/clear UI, onboarding route and landing CTA wiring.
- Correct onboarding URL is `http://localhost:5173/onboarding`; malformed URL containing literal Markdown `**` displayed catch-all 404 and was corrected.
- Refreshed `.ai/CURRENT_STATE.md` and `.ai/KNOWN_ISSUES.md` to supersede obsolete Streamlit and simulated-assistant descriptions; previous historical entries remain preserved.
- No new application changes in this documentation-only reconciliation; full build and tests remain to be recorded by a developer.

## 2026-10-25 — TASK-005 interest assessment feature branch
- `task4` extends `task3` with an illustrative six-question interest assessment.
- Adds FastAPI GET/POST assessment API, deterministic scoring and unit/API tests; adds typed React assessment view and navigation.
- No new third-party dependencies, database or Gemma runtime use. Test evidence and integration merge pending.

## TASK-006 — task5
- Career catalogue API, static fictional dataset, React Career Explorer and illustrative detail route.
- No new dependencies, external services, database, recommendations or roadmap implementation. Tests pending local execution.

## 2026-10-25 — TASK-007 career recommendations
- Added `backend/app/services/career_recommendations.py`, recommendation API/schema/tests and typed React suggestions component/client.
- Reused TASK-005 answers and TASK-006 career IDs; no additional third-party packages.
- Local test verification and shared integration remain pending.

## TASK-011 — Member 1 (task7)
- Added Change My Path React route, selection/confirmation UI, shared current career and path history state, and assessment-progress preservation.
- Session-only; no additional dependencies or backend endpoints. Verification pending.

## TASK-012 on task8
- Added DashboardPage.tsx and dashboard.css, React route and header navigation for session-based summary and comparison of up to three careers.
- No new packages or fabricated readiness metrics; remaining acceptance depends on TASK-010 and local verification.

## TASK-016 (task9)
- Added FeedbackState component and plain-CSS styles for consistent recoverable loading/error/empty UI.
- Updated career search, interest assessment, recommendations and onboarding copy. Backend test corrections from parent branch are retained.
- No new packages; tests not executed in connector environment.

## TASK-018 (task10)
- New backend/tests/test_integration_smoke.py exercises integrated TASK-002/005/006/007 APIs without changing feature logic.
- Added TASK_018_REVIEW.md and tracked remaining missing all-member TASK-010 integration.

## TASK-019 (task11)
- Updated README.md and created TASK_019_REVIEW.md. Documentation only; no functional features or package updates.

## TASK-020 (task12)
- Added HACKATHON_DEMO_SCRIPT.md and TASK_020_REVIEW.md; updated .ai project tracking.
- No application runtime code changed; final integration/release gates have not been completed.

## TASK-008 (task13)
- New backend roadmap service/schema/route/test and frontend roadmap typing, API fetch, detail-page timeline and styles.
- Roadmap data is illustrative; no new dependencies or changes to recommendation logic.

## TASK-013 on task14
- Added Discovery Lab dataset, API, schema, backend tests, React page/client/types and styles; registered navigation. No packages added.
