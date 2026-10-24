# TASK-011 — Change My Path (Member 1)

Branch: `task7`, based on `task6`. TASK-012 dashboard/comparison is NOT implemented.

## Implemented
- New `/change-path` page with twelve TASK-006 catalogue careers loaded from the existing FastAPI GET /api/v1/careers.
- View current selected career, completed onboarding summary and completed TASK-005 interest assessment status.
- Choose another career, review a clear confirmation, apply the switch or cancel; history of chosen paths remains in React memory for this session.
- Shared React StudentJourney state now holds profile, completed interest signals/answers, current career ID and path history.
- Completed assessment calls saveAssessment; recommendation results link to Change My Path. Header also contains link.
- No backend contract changes, new dependencies, database or unapproved career-scoring logic.
- **Temporary state only:** refreshing the page clears onboarding, assessment and path history. TASK-012 dashboard and permanent saved profiles remain out of scope.

## Windows verification
From project root:
```powershell
git status
git fetch origin
git switch --track origin/task7
```
If the local branch already exists, run `git switch task7`.

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

Open exactly `http://localhost:5173/change-path`.

## Manual acceptance
- [ ] Complete onboarding and six-question assessment.
- [ ] Open Change My Path via navigation or assessment result.
- [ ] Onboarding and assessment show completed without needing to retake.
- [ ] Select career A; confirmation appears, Cancel causes no change.
- [ ] Confirm career A; it becomes current career and first history item.
- [ ] Select career B; confirm and check current career and both history entries.
- [ ] Onboarding choices and assessment completion remain after navigation to other routes and back.
- [ ] Selecting the already-current career does not add another history entry.
- [ ] Career detail link opens the selected catalogue career.
- [ ] Backend unavailable shows clear fetch error and Try again.
- [ ] Frontend build and backend test suite pass.
- [ ] Refresh resets only in-memory data (expected limitation).

## Current verification
Committed on GitHub; local browser interactions, build and test suite have not been run by the assistant. Do not mark fully verified or integrated until the user checks. No merge to main/integration performed.
