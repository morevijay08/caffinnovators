# MEMBER TASK ASSIGNMENTS — LIFEPath INDIA

This mapping allocates roadmap tasks; it does not mark them complete or authorize implementation beyond the task the user starts. TASK-002 is the first runtime task. Dependencies and API contracts must be merged into `integration` before dependent work begins.

## Member 1 — React frontend, design and integration
**Role:** React/TypeScript shell, design system, navigation, onboarding, dashboard, path changes, frontend API client and release coordination.

| Task | Work | Dependency / handoff |
|---|---|---|
| TASK-002 | Coordinate React + TypeScript/Vite frontend and FastAPI backend skeleton, scripts, CORS baseline and API contract | First runtime task; consult Members 2/3 on API boundary; merge to `integration` |
| TASK-003 | Design system, landing page, reusable components and React Router navigation | Depends on TASK-002; publish design tokens |
| TASK-004 | Onboarding and temporary client state | Depends on TASK-002/003; agree state keys and API expectations |
| TASK-011 | Change My Path while preserving completed progress | Depends on TASK-004/007; coordinate with Member 2 and state contract |
| TASK-012 | Dashboard and comparison of up to three careers | Depends on TASK-004/007/010/011; consumes typed API response data |
| TASK-016 | Feedback, loading, empty and error states | Depends on TASK-003/004 and feature integration |
| TASK-018 | Coordinate end-to-end testing across frontend and backend | Each feature owner fixes defects in their own module |
| TASK-019 | Coordinate README, frontend/backend setup commands and limitations | Gather accurate notes from Members 2 and 3 |
| TASK-020 | Coordinate demo script and final verification | All three verify their own journeys |

## Member 2 — Career domain and backend APIs
**Role:** Interest assessment, career data, recommendations, career detail/roadmaps, discovery activities and rule-based career guidance.

| Task | Work | Dependency / handoff |
|---|---|---|
| TASK-005 | Interest assessment scoring service and FastAPI route; reflection/results contract | Depends on TASK-002/004; align request/response schema |
| TASK-006 | Fictional career catalogue and Career Explorer API/data query | Depends on TASK-002/003; publish career record schema |
| TASK-007 | Explainable multi-career recommendation service/API | Depends on TASK-005/006; expose documented function and API interface |
| TASK-008 | Career detail and illustrative year-by-year roadmap API | Depends on TASK-006/007; label illustrative content |
| TASK-013 | Interest Discovery Lab activities and reflection data/logic | Depends on TASK-005/006 |
| TASK-014 | Rule-based Career Assistant service/API and integration notes | Depends on TASK-006/007/008; no LLM/runtime API required |

## Member 3 — Readiness backend and testing
**Role:** Timed maths quiz, topic-level analysis, improvement/retest, fictional affordability demo data, readiness API and test coordination.

| Task | Work | Dependency / handoff |
|---|---|---|
| TASK-009 | Timed Math Readiness Assessment service/API with topic tags | Depends on TASK-002 and agreed assessment contract |
| TASK-010 | Topic analysis, improvement plan, checklist and retest service/API | Depends on TASK-009; publish result schema for frontend dashboard |
| TASK-015 | Fictional scholarship/affordability demo content and API/data integration as needed | Depends on TASK-002 and agreed fictional-data schema; no real-time eligibility claims |
| TASK-017 | Coordinate frontend/backend test coverage and API contract checks | Feature owners write tests for their own logic; Member 3 checks coverage gaps and runs combined suites |

## Shared responsibilities
- Each member writes and runs tests for their own logic.
- Member 1 coordinates frontend and cross-stack integration.
- Member 2 owns career/interest service contracts and data schemas.
- Member 3 owns readiness service contracts, scoring and test-suite coordination.
- All members review student safety, fictional-data labels, accessibility, and API/UI error states.
- Do not mark a task DONE until acceptance criteria and relevant tests are verified.

## Parallel execution order
1. **Gate 1:** TASK-002 establishes a runnable frontend/backend skeleton and API contract baseline; merge to `integration`.
2. **Gate 2:** Agree shared schemas, API errors, local ports/CORS, temporary state and frontend type conventions; merge TASK-003/004 foundations.
3. **Wave A:** Member 2 works on TASK-005/006 as dependencies allow; Member 3 starts TASK-009 after API/schema agreement; Member 1 builds frontend features only against agreed contracts.
4. **Wave B:** Member 2 completes TASK-007/008; Member 3 completes TASK-010/015; Member 1 integrates TASK-011/012.
5. **Wave C:** Member 2 completes TASK-013/014; Member 1 completes TASK-016; Member 3 coordinates TASK-017.
6. **Release:** All members support TASK-018; Member 1 coordinates TASK-019/020. Promote stable work to `main` only after builds, API checks and end-to-end tests.

If a dependency or API contract is missing, work on another authorized independent task or ask the coordinator; do not invent an incompatible interface.
