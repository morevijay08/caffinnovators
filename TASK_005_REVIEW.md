# TASK-005 — Interest Assessment Review (Member 2)

Branch: `task4`, based on `task3`. TASK-007's previous incompatible branch was NOT merged.

## What was implemented
- Six fictional interest-reflection questions with stable IDs and three choices each.
- FastAPI GET `/api/v1/interest-assessment` returns questions without scoring tags or hidden signals.
- FastAPI POST `/api/v1/interest-assessment/submit` validates exactly one answer per question, calculates deterministic normalized interest scores, returns explainable signals and a disclaimer.
- React `/interest-assessment` page: question navigation, choice validation, six-minute visual timer, results, retry and graceful API-error state.
- Onboarding completion links to assessment. Student identity/marks are not sent.
- API tests cover questions, deterministic scoring and invalid/missing/duplicate answers.
- No recommendations, career catalogue, model inference, database, auth or persistence.
- Timer is **client-side UX only**. Server does not certify elapsed time; do not claim anti-cheat or server-enforced timing.

## Test locally — from repository root (Windows)
```powershell
git status
git fetch origin
git switch --track origin/task4
```
If a local `task4` branch already exists, use `git switch task4`. Never discard uncommitted work.

### Backend terminal
```powershell
cd backend
python -m pip install -r requirements.txt
python -m pytest -q
python -m uvicorn app.main:app --reload --port 8000
```
Visit `http://localhost:8000/docs`. Test GET `/api/v1/interest-assessment` and inspect POST via Swagger.

### Frontend terminal (new terminal at root)
```powershell
cd frontend
npm install
npm run build
npm run dev
```
Visit **http://localhost:5173/interest-assessment** or complete onboarding and click **Start interest assessment**.

### Browser acceptance
- [ ] Questions load from FastAPI (backend running).
- [ ] Six different prompts; no solution/score shown before submission.
- [ ] Next button requires an answer; Previous preserves choices.
- [ ] The countdown is shown and the expiry screen offers restart (speed up via local dev-only inspection if needed).
- [ ] Answer all six and submit; interest signals and disclaimer appear.
- [ ] Try again clears the previous answers.
- [ ] Stop FastAPI/reload to confirm a visible recovery message.
- [ ] API POST with an omitted, duplicate, or unknown option gets HTTP 422.
- [ ] Frontend build and backend pytest pass.

## Known limitations
- Interest questions are a reflective exercise, not a validated psychometric test.
- Scores are heuristic; no career probabilities or fixed-ability verdicts.
- Answers/results are not persisted across refresh. TASK-007 integration will require coordination on the response fields.
- Local build and browser/API tests have **not been executed by this assistant**. They require your verification.

## Handoff
Do not start TASK-007 until TASK-006 career catalogue and shared matching tags have been integrated. Do not merge directly to `main`.
