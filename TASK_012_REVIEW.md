# TASK-012 — Student Dashboard and Career Comparison (Member 1)

Branch: `task8` from `task7` — React + TypeScript, FastAPI catalogue and shared StudentJourney state.

## Delivered in TASK-012
- New `/dashboard` route, linked in site navigation.
- Cards summarizing onboarding, completed interest assessment and selected career path.
- View up to six interest signals when the interest assessment was completed.
- Fetch real illustrative TASK-006 catalogue through typed frontend client.
- Select and compare up to **three** careers side by side: summary, interest tags and skills, with career-profile links.
- Clear empty/loading/error states and backend retry for the catalogue.
- Support session-only React state; no database, no fabricated readiness scores, no additional dependencies.

## Scope dependency
TASK-010 math topic analysis/improvement data is not integrated into `task7` or `task8`; this dashboard shows an explicit integration-pending notice rather than fake readiness results. That portion of the roadmap is **not complete** until Member 3's endpoint and schema are agreed and integrated. TASK-012 is a working partial feature, pending this dependency and local tests.

## Windows review
From repository root:
```powershell
git status
git fetch origin
git switch --track origin/task8
```
If local `task8` exists, use `git switch task8`; save uncommitted changes before switching.

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
Open exactly `http://localhost:5173/dashboard`.

## Acceptance checks
- [ ] New route loads from navigation.
- [ ] Empty onboarding / interest / selected-path cards show useful next actions.
- [ ] Complete onboarding, then interest quiz; return to dashboard and see session progress and interest signals.
- [ ] Select a career on Change My Path; dashboard reflects correct career.
- [ ] Compare one, two then three careers; the fourth choice is disabled until one is unchecked.
- [ ] Compare cards show correct summary, interest tags, skills and profile links.
- [ ] Simulate unavailable backend; error and retry appear.
- [ ] Refresh clears the session-only state (expected behavior).
- [ ] Backend pytest and frontend production build pass.

## Verification
Branch files committed. The assistant has not executed the npm build, backend pytest or manual browser checks in the user's local environment. **Do not mark TASK-012 DONE** until testing and readiness-API integration are reviewed.
