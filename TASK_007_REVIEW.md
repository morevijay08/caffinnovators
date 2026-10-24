# TASK-007 — Explainable Career Recommendations (Member 2)

Branch: `task6`, based on `task5`. The separate older `feature/member-2-career-discovery` branch was NOT merged.

## What exists
- Deterministic Python service scoring submitted TASK-005 question/option IDs server-side, then matching its interest signals to TASK-006 career interest tags.
- Stable career IDs, normalized heuristic score 0–100, explanations, matching interest tags, next exploration steps and a prominent limitations disclaimer.
- POST `/api/v1/recommendations`: JSON `{"answers":[{"question_id":"q1","option_id":"a"}, ...],"limit":5}`. Limit 1–12, default 5; all six stable questions must be answered exactly once. Returns `recommendations`, `assessment_signals`, `disclaimer`.
- Frontend displays a “See career suggestions” action after TASK-005 assessment results; shows ranked options linking to actual TASK-006 career profiles. API failure has retry state.
- Backend tests for sorted recommendations, limit, repeatability, invalid input, and consistency with career catalogue.
- No external LLM, paid service, database or new dependency. No fake guarantee/aptitude claim.

## Local testing — Windows
From repo root (save or commit any local changes first):
```powershell
git fetch origin
git switch --track origin/task6
```
If task6 exists locally, run `git switch task6`.

Backend terminal:
```powershell
cd C:\Users\Admin\Desktop\caffinnovators\backend
python -m pip install -r requirements.txt
python -m pytest -q
python -m uvicorn app.main:app --reload --port 8000
```

Frontend terminal:
```powershell
cd C:\Users\Admin\Desktop\caffinnovators\frontend
npm install
npm run build
npm run dev
```
Open exactly `http://localhost:5173/interest-assessment`. Complete all six questions and click **See career suggestions** after your signals appear.
You can also test API requests through `http://localhost:8000/docs` under POST /api/v1/recommendations.

## Acceptance checklist
- [ ] Onboarding → assessment continues working.
- [ ] Six questions submit and produce interest signals.
- [ ] Clicking 'See career suggestions' displays five explained career options.
- [ ] Every career link opens a valid TASK-006 detail page.
- [ ] Different answer patterns produce different interest signals / rankings.
- [ ] API rejects unanswered/duplicate/invalid options with 422.
- [ ] API rejects limit outside 1–12 with 422.
- [ ] Scoring results stable for repeated identical submissions.
- [ ] Stopping backend produces a clear error rather than false recommendations.
- [ ] `python -m pytest -q` and `npm run build` pass.

## Important scope / handoff
- Percentage is **heuristic signal overlap**, not statistical probability or fitness for a career.
- Results exist in React component state and disappear on reload. TASK-011 path switching needs a coordinated shared-state extension; that is NOT implemented here.
- TASK-008 detailed roadmaps are future work.
- These changes are on a feature task branch and are not merged into `integration`.
- GitHub commits verified. Actual terminal tests and browser behavior require the user's local verification.
