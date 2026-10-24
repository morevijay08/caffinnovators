# TASK-017 — Test coverage and API contract checks (Member 3)

## Scope
Add regression checks for the math readiness API and coordinate the combined test pass. Tests must verify externally observable contracts, safe validation errors, score/topic consistency, and anonymous attempt retrieval. This task does not claim the entire app has passed end-to-end testing.

## Added in this task branch
- `backend/tests/test_math_assessment_contract.py`
  - Public assessment response exposes options but not correct-answer keys or explanations.
  - Submission returns a valid attempt ID and internally consistent totals/topic breakdown.
  - Saved attempt can be retrieved by its ID with the same result.
  - Unknown question IDs, duplicate answers, invalid options, and invalid elapsed time are rejected with HTTP 422.
  - Unknown valid UUID attempt IDs return HTTP 404.

## Verification status
- **Not completed yet.** The assistant has not run pytest or the frontend build against this branch.
- The user asked to defer manual functional testing until a consolidated pass.
- Do not mark TASK-017 done based on authored tests alone.

## Run on Windows PowerShell
From the repository root, check for local changes before switching branches:
```powershell
git status
git fetch origin
git switch --track origin/feature/TASK-017-test-coverage-api-contracts
```
If the branch already exists locally, use `git switch feature/TASK-017-test-coverage-api-contracts`.

Backend:
```powershell
cd D:\Hackday\caffinnovators\backend
python -m pip install -r requirements.txt
python -m pytest -q
```

Frontend contract/type check:
```powershell
cd D:\Hackday\caffinnovators\frontend
npm install
npm run build
```

## Consolidated review checklist
- [ ] Backend pytest suite passes; record the actual test count.
- [ ] Frontend TypeScript/Vite production build passes.
- [ ] OpenAPI docs at `http://localhost:8000/docs` show current registered routes.
- [ ] Math assessment GET omits answer keys and explanations.
- [ ] Invalid math submissions return structured 422 responses.
- [ ] A submitted attempt can be fetched again by attempt ID.
- [ ] Career/interest integration smoke tests still pass.
- [ ] Manually walk the student journey and scholarship estimator before release.
- [ ] Confirm the feature branches being promoted are intentionally integrated; do not assume task-series branches automatically appear on main.

## Known limitations
- Browser E2E automation is not configured in `frontend/package.json`; UI checks remain manual.
- These tests use the app's configured database for persistence checks. CI should configure an isolated test database if it runs tests against a shared persistent environment.
- Test files authored remotely have not been executed in the user's local environment.
