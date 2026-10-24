# TASK-009A — SQLite Persistence for Anonymous Math Attempts

Status: IN PROGRESS on `feature/TASK-009-sqlite-persistence`. Implementation is present on this branch; local dependency installation and test execution still need verification.

## Owner
**Member 3 — sole owner for this database workstream.** All database setup, SQLAlchemy models, SQLite schema evolution, persistence/repository code, save/retrieve API, database-related `.ai/` documentation and database tests are assigned to Member 3. Member 1 may consume the agreed API contract but should coordinate before changing persistence files.

## Goal
Persist non-identifying, server-calculated math assessment result snapshots in SQLite. No login, student profiles, names, school details, marks, or answer-by-answer storage.

## Implementation
- SQLAlchemy 2.x with SQLite.
- `DATABASE_URL` can override the default local database path under `backend/data/lifepath.db`.
- Database file patterns are gitignored.
- `assessment_attempts` stores UUID, assessment version, counts, percentage, reported elapsed time, timeout flag, topic-breakdown JSON, encouragement/disclaimer and server timestamp.
- `POST /api/v1/math-assessment/submit` persists the calculated result and adds `attempt_id` to the response.
- `GET /api/v1/math-assessment/attempts/{attempt_id}` retrieves a saved result; unknown IDs return 404.
- The attempt UUID is an opaque reference, not authentication. No identity or per-student access control is implied.
- The question bank and correct answer keys remain server-side in Python. Individual submitted answers are not stored.

## Files changed
- `backend/requirements.txt`
- `backend/.gitignore`
- `backend/app/db.py`
- `backend/app/models/assessment_attempt.py`
- `backend/app/services/assessment_persistence.py`
- `backend/app/schemas/math_readiness.py`
- `backend/app/api/math_assessment.py`
- `backend/app/main.py`
- `backend/tests/test_assessment_persistence.py`
- `.ai/TECH_STACK.md`
- `.ai/ARCHITECTURE.md`
- `.ai/CURRENT_STATE.md`
- `.ai/TEAM_WORKFLOW.md`
- `.ai/API_CONTRACTS.md`
- `.ai/roadmap/MEMBER_TASK_ASSIGNMENTS.md`

## Acceptance checklist
- [ ] Install backend dependencies including SQLAlchemy.
- [ ] Run all backend tests from `backend/`.
- [ ] Confirm valid POST returns an attempt UUID and writes exactly one row.
- [ ] Confirm GET by UUID returns the same result.
- [ ] Confirm unknown UUID returns 404.
- [ ] Confirm invalid, duplicate and unknown-question submissions do not create rows.
- [ ] Confirm data remains after a session/application restart using the same SQLite file.
- [ ] Inspect git status and verify no local database file is staged.
- [ ] Verify health, assessment GET and submission endpoints remain functional.

## Known limitations
- `elapsed_seconds` is client-reported and is not a tamper-proof timer.
- This is anonymous result persistence, not authentication or student history.
- SQLite is appropriate for this hackathon/local prototype. Production multi-instance deployment would need an explicit storage/deployment decision.
- `create_all` initializes the current schema but is not a migration system; schema changes must be coordinated and documented.

## Branch/PR workflow
Never commit directly to `main` or `integration`. This branch is based on the existing TASK-009 API-integration feature branch while prerequisite scaffold/assessment PRs are pending; retarget/rebase against latest `integration` after those dependencies are merged. Open a reviewed PR to `integration`; do not claim the task is integrated until merged and combined checks pass.
