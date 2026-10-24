# TASK-016 — Feedback, loading, empty and error states (Member 1)

Branch: `task9`, based on `fix/task8-backend-tests`, so it retains the previously corrected backend test expectations.

## Scope delivered
- Reusable `FeedbackState` React component with accessible `role=status/alert`, aria-live, loading, error and empty styles, optional retry/primary action, responsive CSS and reduced-motion support.
- Career Explorer: shared loading, unavailable API / retry and no-match / clear filters states.
- Interest Assessment: shared loading and unavailable question state with live retry (no page refresh required); approachable disclaimer.
- Career Recommendations: consistent recoverable API error and empty-recommendations guidance.
- Onboarding summary text updated to reflect that interest assessments and career suggestions now exist.
- Existing dashboard, career details and path-selection states retained; no changes to Python scoring, FastAPI API shapes, new packages or persistence.
- API health tests fixed on the parent branch remain in this new branch.

## Windows commands
From repository root:
```powershell
git status
git fetch origin
git switch --track origin/task9
```
If `task9` exists locally, use `git switch task9`.

Terminal A:
```powershell
cd C:\Users\Admin\Desktop\caffinnovators\backend
python -m pytest -q
python -m uvicorn app.main:app --reload --port 8000
```
Terminal B:
```powershell
cd C:\Users\Admin\Desktop\caffinnovators\frontend
npm install
npm run build
npm run dev
```

Open exactly `http://localhost:5173/careers` and `http://localhost:5173/interest-assessment`.

## Review checklist
- [ ] Career Explorer loads 12 careers normally.
- [ ] Search `zzzz-no-match` to trigger empty state, then Clear filters.
- [ ] Stop FastAPI and reload Career Explorer; error message and retry button appear. Restart FastAPI and click Try again.
- [ ] With backend stopped reload Interest Assessment, confirm error feedback. Start FastAPI and Try again *without refreshing*.
- [ ] Complete six questions, show interest signals with supportive text and see recommended careers.
- [ ] Stop FastAPI before requesting recommendations; error/retry appears. Start it, retry successfully.
- [ ] Navigate to Dashboard/Change My Path and verify earlier behavior was not disrupted.
- [ ] Check narrow viewport and keyboard Tab focus.
- [ ] `npm run build` succeeds and backend `python -m pytest -q` passes (expect 18 backend tests if no other branches changed).
- [ ] Git status remains clean aside from user changes.

## Scope limits
- No persistent student state; page refresh clears profile, assessment and selected path.
- Task does not implement Member 3 readiness API or TASK-014 Gemma Career Assistant.
- API/build/browser checks have **not been run by this assistant**. Record real output before marking TASK-016 done or merging into shared integration branch.
