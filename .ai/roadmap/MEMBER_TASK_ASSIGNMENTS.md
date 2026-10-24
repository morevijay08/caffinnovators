# MEMBER TASK ASSIGNMENTS — LIFEPath INDIA

This mapping allocates the existing roadmap; it does not mark tasks complete or authorize implementation. TASK-002 is the first runtime task and must be explicitly started by the user. Dependencies must be merged into `integration` before dependent tasks begin.

## Member 1 — UI, navigation and integration
**Role:** Streamlit shell, design system, navigation, onboarding, student dashboard, path changes and release coordination.

| Task | Work | Dependency / handoff |
|---|---|---|
| TASK-002 | Streamlit skeleton, app entry point, folders, navigation shell and basic setup files | First runtime task; merge to `integration` before others start app features |
| TASK-003 | Design system, landing page, reusable UI patterns and navigation | Depends on TASK-002; publish shared design tokens |
| TASK-004 | Student onboarding and session-state structure | Depends on TASK-002/003; agree state keys with Members 2 and 3 |
| TASK-011 | Change My Path while preserving progress | Depends on TASK-004/007; coordinate state contract with Member 2 |
| TASK-012 | Dashboard and comparison of up to three careers | Depends on TASK-004/007/010/011; consumes career and assessment result schemas |
| TASK-016 | Feedback page, navigation and empty/error states | Depends on TASK-003/004 and integrated feature pages |
| TASK-018 | Coordinate end-to-end smoke test and integration fixes | Each feature owner fixes defects in their own module |
| TASK-019 | Coordinate README, setup instructions and limitations | Gather accurate feature notes from Members 2 and 3 |
| TASK-020 | Coordinate demo script and final repository verification | All three verify their own feature journeys |

## Member 2 — Interest discovery and career engine
**Role:** Interest assessment, career data, recommendations, career details, roadmaps and rule-based career guidance.

| Task | Work | Dependency / handoff |
|---|---|---|
| TASK-005 | Timed interest assessment, reflection and explainable scoring | Depends on TASK-002/004; agree question/result schema with Member 3 |
| TASK-006 | Fictional career catalogue and Career Explorer data/query logic | Depends on TASK-002/003; provide stable career record schema |
| TASK-007 | Explainable multi-career recommendation engine | Depends on TASK-005/006; expose a documented function interface |
| TASK-008 | Career detail and illustrative year-by-year roadmap | Depends on TASK-006/007; clearly label illustrative content |
| TASK-013 | Interest Discovery Lab activities and reflection | Depends on TASK-005/006 |
| TASK-014 | Transparent rule-based Career Assistant | Depends on TASK-006/007/008; no LLM/runtime API required |

## Member 3 — Readiness assessments and learning analytics
**Role:** Timed maths quiz, topic-level results, improvement/retest logic, fictional affordability demo and test coordination.

| Task | Work | Dependency / handoff |
|---|---|---|
| TASK-009 | Timed Math Readiness Assessment with topic tags | Depends on TASK-002/003; agree question/result schema with Member 2 and state keys with Member 1 |
| TASK-010 | Topic analysis, improvement plan, progress checklist and retest | Depends on TASK-009; publish a documented result schema for the dashboard |
| TASK-015 | Fictional scholarship/affordability demo page | Depends on TASK-002 and agreed fictional-data schema; do not imply real-time eligibility or official funding |
| TASK-017 | Coordinate unit-test coverage across the app | Feature owners write tests for their own logic; Member 3 checks coverage gaps and runs the combined suite |

## Shared responsibility
- Each member writes and runs tests for the logic they implement.
- Member 1 coordinates integration and shared UI contracts.
- Member 2 owns career/interest domain contracts.
- Member 3 owns readiness/question/scoring contracts and test-suite coordination.
- All members review product safety, fictional-data labels, accessibility and student-friendly wording.
- Do not mark a task DONE until its own acceptance criteria and relevant tests are verified.

## Parallel execution order
1. **Gate 1:** Member 1 completes TASK-002; merge to `integration`.
2. **Gate 2:** Agree shared schemas/contracts and merge TASK-003/004 foundations.
3. **Parallel wave A:** Member 2 can work on TASK-005/006 as their dependencies allow; Member 3 can work on TASK-009 once the shell/design contract is ready; Member 1 prepares TASK-011/012 scaffolding only when dependencies are available.
4. **Parallel wave B:** Member 2 completes TASK-007/008; Member 3 completes TASK-010/015; Member 1 integrates TASK-011/012.
5. **Parallel wave C:** Member 2 completes TASK-013/014; Member 1 completes TASK-016; Member 3 coordinates TASK-017 while feature owners maintain their tests.
6. **Release:** All members support TASK-018; Member 1 coordinates TASK-019/020; merge stable work to `main` only after end-to-end checks.

If an assigned task is blocked by an unmet dependency, work on another already-authorized independent task or ask the coordinator; do not build a private incompatible version of the missing dependency.
