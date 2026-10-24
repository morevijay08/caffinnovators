# TASK-009 — Timed Math Readiness Assessment

**Status:** Core math readiness API implemented on `integration`. SQLite persistence is being added in `feature/TASK-009-sqlite-persistence` under TASK-009A. Combined persistence verification is pending.

## Owner
Member 3 — readiness backend and tests.

## Implemented functionality
- Static fictional practice question bank with 12 questions across arithmetic, fractions/decimals, algebra, geometry, ratios/proportions and data interpretation.
- Public question response contains only IDs, prompts, topic tags and options. Correct answers and explanations remain server-side.
- Pydantic request/response schemas.
- Deterministic server-side scoring and per-topic totals/percentages.
- FastAPI router:
  - `GET /api/v1/math-assessment`
  - `POST /api/v1/math-assessment/submit`
- Unit tests cover public answer-key exclusion, full score, wrong or unanswered answers, invalid option IDs, unknown question IDs and duplicate submissions.

## Timing behavior for MVP
The assessment declares a 600-second time limit. `elapsed_seconds` is client-reported and is used only to flag whether the reported time exceeded the limit; it is not tamper-proof server timing. A session-backed server timer can be considered later if stronger enforcement is required. Scoring always happens on the server, and unanswered questions count as incorrect.

## API behavior
- Submit stable `question_id` and `option_id` pairs; the server never trusts a client-submitted score.
- Unknown question IDs, duplicate answers for one question and invalid option IDs return a validation error from the route.
- Results contain total, answered and correct counts; percentage; topic breakdown; time-limit flag; supportive encouragement; and a non-diagnostic disclaimer.
- The scoring service is deterministic and does not use an LLM.
- TASK-009A adds SQLite persistence of non-identifying result summaries only. Student accounts and answer-by-answer storage are outside this task's scope.
- Planned retrieval endpoint: `GET /api/v1/math-assessment/attempts/{attempt_id}`.
- The attempt UUID supports lookup; it is not authentication.

## Acceptance checklist
- [x] Question bank and stable IDs exist.
- [x] Public assessment does not expose answer keys or explanations.
- [x] Scoring is deterministic and server-side.
- [x] Topic-level results are returned.
- [x] Invalid, unknown and duplicate submissions are rejected.
- [x] Original feature-branch unit tests were reported as passing (6 tests); rerun the combined suite after conflict resolution.
- [x] Math assessment router is registered in the shared FastAPI application on `integration`.
- [ ] Run the combined backend test suite after integrating SQLite persistence.
- [ ] Verify POST submission saves a result and returns an `attempt_id`.
- [ ] Verify GET attempt retrieval returns the saved result and a missing ID returns 404.
- [ ] Verify saved attempts survive a server restart.
- [ ] Run combined API smoke tests on the resolved branch.
- [ ] Review timing limitations with the team before claiming secure server-enforced timing.

## Relevant files
- `backend/app/data/math_questions.py`
- `backend/app/schemas/math_readiness.py`
- `backend/app/services/math_readiness.py`
- `backend/app/api/math_assessment.py`
- `backend/app/db.py`
- `backend/app/models/assessment_attempt.py`
- `backend/app/services/assessment_persistence.py`
- `backend/tests/test_math_readiness.py`
- `backend/tests/test_assessment_persistence.py`

## Completion rule
Do not mark TASK-009 and TASK-009A fully complete until the shared API works, the combined tests pass, and persistence/retrieval—including restart persistence—has been verified.
