# TASK-009 — Timed Math Readiness Assessment

Status: IN PROGRESS on `feature/TASK-009-math-readiness`. This branch implements the independent readiness domain module and router; integration into the shared FastAPI app waits for TASK-002's app entry point.

## Owner
Member 3 — readiness backend and tests.

## Implemented in this branch
- Static fictional practice question bank with 12 questions across arithmetic, fractions/decimals, algebra, geometry, ratios/proportions and data interpretation.
- Public question response contains only IDs, prompts, topic tags and options. Correct answers and explanations remain server-side.
- Pydantic request/response schemas.
- Deterministic server-side scoring and per-topic totals/percentages.
- FastAPI router:
  - `GET /api/v1/math-assessment`
  - `POST /api/v1/math-assessment/submit`
- Unit tests for public answer-key exclusion, full score, wrong/unanswered answers, invalid option IDs, unknown question IDs and duplicate submissions.

## Timing behavior for MVP
The assessment declares a 600-second time limit. `elapsed_seconds` is client-reported and is used only to flag whether the reported time exceeded the limit; it is not tamper-proof server timing. A session-backed server timer can be agreed later if the product requires stronger enforcement. Scoring always happens on the server and unanswered questions count as not correct.

## API behavior
- Submit stable `question_id` and `option_id` pairs; the server never trusts a client-submitted score.
- Unknown question IDs, duplicate answers for one question and invalid option IDs return a validation error from the route.
- Results contain total/answered/correct counts, percentage, topic breakdown, time-limit flag, supportive encouragement and a non-diagnostic disclaimer.
- No database, external API, LLM, or personal student data is required.

## Acceptance checklist
- [x] Question bank and stable IDs exist.
- [x] Public assessment does not expose answer keys or explanations.
- [x] Scoring is deterministic and server-side.
- [x] Topic-level results are returned.
- [x] Invalid/unknown/duplicate submissions are rejected.
- [x] Unit tests pass in an isolated local test copy (6 passed).
- [ ] Run tests against the actual GitHub branch checkout when network/checkout is available.
- [ ] Wire router into `backend/app/main.py` after TASK-002 creates the shared FastAPI entry point.
- [ ] Run FastAPI endpoint smoke tests after integration.
- [ ] Review the timing/anti-tampering behavior with the team before claiming secure server-enforced timing.

## Files
- `backend/app/data/math_questions.py`
- `backend/app/schemas/math_readiness.py`
- `backend/app/services/math_readiness.py`
- `backend/app/api/math_assessment.py`
- `backend/tests/test_math_readiness.py`

Do not mark TASK-009 DONE until the router is wired into the shared FastAPI app and API smoke tests pass.
