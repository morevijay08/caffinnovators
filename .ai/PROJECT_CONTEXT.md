# LIFEPath INDIA — COMPLETE PROJECT BRIEF & AI HANDOFF

> **Purpose:** A portable source of context for new teammates and AI coding assistants. Read this file first, then follow the detailed control files and the one active task. Keep this brief aligned with those documents.

## 1. Project identity
- **Product:** LifePath India
- **Tagline:** *Every Interest Has a Future.*
- **Purpose:** Help students explore careers through interests, curiosity, preferred activities, goals, and learnable skills—not marks alone.
- **Users:** Students in Classes 8–12, diploma students, and college students exploring future directions in India.
- **Repository:** https://github.com/morevijay08/caffinnovators
- **Documentation:** `.ai/`

## 2. Problem and principles
Students may be pushed toward a narrow set of careers because of marks, social expectations, or limited information. Some already have a goal but need a roadmap; others need activities to discover what interests them.

1. Interest first; marks are context, not destiny.
2. Show multiple plausible careers and explain why they match.
3. Skills can improve; a short assessment is not a diagnosis or permanent verdict.
4. Students can change direction without losing recorded progress.
5. Use inclusive, supportive language and minimal data collection.
6. Label illustrative data, AI-generated assistant guidance and demo scholarships.
7. Never fabricate official links, institutions, live scholarships, eligibility rules, fees, salaries, admission criteria, or job guarantees.

## 3. Core student journeys
A. Knows interests → onboarding → interest assessment → explained career suggestions → career detail/roadmap → compare/save.
B. Unsure → Interest Discovery Lab → activities/reflection → refined career exploration.
C. Has a goal → career details/pathway → readiness quiz → learning plan.
D. Has subject difficulty → timed diagnostic → topic feedback → practice plan → retest.
E. Changes goal → preserve completed progress → compare old/new paths → new roadmap.

## 4. MVP features
1. Premium, accessible landing page and navigation.
2. Lightweight onboarding.
3. Timed interest assessment with explainable scoring.
4. Searchable career explorer with representative demo content.
5. Multiple explainable career recommendations.
6. Career detail and illustrative year-by-year roadmap.
7. Timed Math Readiness Assessment with topic tags.
8. Topic analysis, supportive improvement plan and retest.
9. Change My Path while preserving completed progress.
10. Dashboard and comparison of up to three careers.
11. Interest Discovery Lab.
12. Gemma 4-powered Career Assistant behind FastAPI, with safe prompt instructions, bounded context and recoverable errors.
13. Fictional scholarship/affordability demo, clearly labelled.
14. Feedback, empty states and useful error handling.

### MVP definition of done
A judge can complete onboarding and an interest assessment, see multiple explained career options, open a roadmap, take a timed math test, receive topic feedback and an improvement plan, and change career choice without losing completed progress. The frontend and backend run locally using the documented commands. No database is required. The Career Assistant uses Gemma 4 at runtime through local Ollama by default; hosted inference is optional only if the team explicitly selects it.

## 5. Approved architecture
**React + TypeScript frontend, Python FastAPI backend, static demo data, no database.** This replaces the earlier Streamlit-only architecture by explicit user approval on 2026-10-24.

### Frontend
- React + TypeScript, built and served in development with Vite.
- React Router for pages.
- Custom CSS/design tokens for a polished, responsive and accessible UI.
- A typed Fetch API client calls the backend; components should not hardcode API URLs.

### Backend
- Python 3.11+ with FastAPI, Pydantic and Uvicorn.
- Thin API route handlers call deterministic, testable Python services.
- Static fictional data; no database or durable personal profile storage.

### Intended repository layout
- `frontend/`: React application, pages, components, API client, types and styles.
- `backend/app/main.py`: FastAPI entry point.
- `backend/app/api/`: route handlers.
- `backend/app/schemas/`: Pydantic request/response models.
- `backend/app/services/`: interest scoring, career matching, readiness analysis and learning-plan logic.
- `backend/app/data/`: fictional careers, activities, quiz questions and scholarship demo data.
- `backend/tests/`: backend tests.
- `.ai/API_CONTRACTS.md`: API contracts that frontend and backend must follow.

Inspect the repository before assuming these paths exist; avoid duplicate structures.

### Explicit non-goals for the MVP
No Next.js, second frontend framework, Tailwind/Bootstrap/component framework, database, authentication, analytics SDK, paid API, required external service, hosted/local LLM, LangChain/LangGraph, vector database, embeddings or RAG. Do not add packages without a demonstrated need and approval.

### Gemma 4
Gemma 4 is the preferred **development-time** coding assistant when available. It is not part of the running application and must not be added as a runtime dependency.

## 6. Team roles
- **Member 1 — Frontend/UI and integration:** React app shell, design system, navigation, onboarding, dashboard, path changes, frontend API client, release coordination.
- **Member 2 — Career domain/backend:** interest assessment service, career catalogue, recommendation logic, career detail/roadmaps, discovery activities and rule-based assistant API.
- **Member 3 — Readiness backend and tests:** maths assessment API/service, topic analysis, improvement/retest logic, fictional affordability demo data, test coordination.

See `.ai/TEAM_WORKFLOW.md` and `.ai/roadmap/MEMBER_TASK_ASSIGNMENTS.md` for exact ownership and dependencies.

## 7. How AI coding assistants must work
1. Inspect the current branch, repository tree and existing code.
2. Read `.ai/AI_RULES.md`, `.ai/AI_MASTER_PROMPT.md`, `.ai/TECH_STACK.md`, `.ai/ARCHITECTURE.md`, `.ai/API_CONTRACTS.md`, `.ai/CURRENT_STATE.md`, `.ai/DECISIONS.md`, `.ai/TEAM_WORKFLOW.md`, the roadmap, member assignments and the active task file.
3. Confirm member role, one task ID, allowed files, dependencies and acceptance criteria.
4. Check that the relevant API contract and prerequisites are merged before parallel work.
5. State a brief plan before editing.
6. Implement only the assigned task and owned files; do not build the entire app in one pass.
7. Add relevant tests, run checks when possible, and report actual results only.
8. Review changes for privacy, accessibility, inclusive language, demo labels and dependency compliance.
9. Update state/progress/changelog with verified facts; coordinate shared-file edits.
10. Summarize changed files, test results, limitations and the next ready task.

If a required file is missing or an interface is unclear, report the blocker instead of inventing a private incompatible contract.

## 8. Current documented status
- TASK-001 — project definition/control documentation: recorded as done.
- TASK-002 — initial React + TypeScript/Vite frontend and FastAPI backend skeleton: next runtime task, assigned to Member 1 as integration lead with Member 2/3 consulted on the API contract.
- The repository's runtime implementation status must be checked directly; this brief does not claim the application has been implemented or tested.

## 9. Source-of-truth documents
- [AI master instructions](AI_MASTER_PROMPT.md)
- [AI rules](AI_RULES.md)
- [Approved tech stack](TECH_STACK.md)
- [Architecture](ARCHITECTURE.md)
- [API contracts](API_CONTRACTS.md)
- [Current state](CURRENT_STATE.md)
- [Decisions](DECISIONS.md)
- [Three-member workflow](TEAM_WORKFLOW.md)
- [Master roadmap](roadmap/MASTER_ROADMAP.md)
- [Member task assignments](roadmap/MEMBER_TASK_ASSIGNMENTS.md)
- [Task files and template](tasks/)
- [Progress log](logs/PROGRESS.md)
- [Changelog](logs/CHANGELOG.md)


## User-approved Gemma 4 runtime chatbot
The Career Assistant must use Gemma 4 at runtime; it is not a simulated/rule-based chatbot and not merely a coding-assistant preference. Default request flow: React chat UI → FastAPI `POST /api/v1/career-assistant` → local Ollama → configurable Gemma 4 model. Initial configuration defaults: `OLLAMA_BASE_URL=http://localhost:11434`, `GEMMA_MODEL=gemma4:e2b`; verify the installed tag before implementation. The browser never calls Ollama directly. Hosted inference is an explicit fallback decision. Interest scoring, career recommendation ranking and math assessment scoring remain deterministic Python services. See ADR-008 and `.ai/tasks/TASK_014_GEMMA_CAREER_ASSISTANT.md`.
