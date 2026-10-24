# TASK-018 — Integration smoke testing (Member 1)

Branch: `task10` based on `task9`. This is a verification task, not a new feature. No changes to Member 2/3 domain logic or unmerged branches.

## Added
- `backend/tests/test_integration_smoke.py`: integration tests using FastAPI's in-process TestClient.
- Exercises health, career catalogue, six-question interest submission, deterministic recommendations, and individual career details as one coherent flow.
- Checks that recommendation career IDs exist in the actual catalogue, explanations/next steps are present, and scores are ordered.
- Covers missing answers (422), unknown career (404), and cluster filtering.
- No new runtime packages or backend endpoints.

## Known integration gaps
- TASK-010 readiness analysis is not integrated on the task branch; dashboard honestly reports pending integration. This is not a full all-member end-to-end pass.
- TASK-008 roadmap, TASK-013 discovery lab, TASK-014 Gemma, TASK-015 affordability are separate tasks and not required to fabricate for this branch.
- Frontend does not have an automated browser E2E runner. Browser steps below must be completed manually.
- Tests executed through GitHub edits **have not been run in the user's environment**. Do not mark TASK-018 DONE until verifying output and coordinating remaining integration.

## Run on Windows
At repository root:
```powershell
git status
git fetch origin
git switch --track origin/task10
```
If already created locally, `git switch task10`. Save local edits before switching.

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
Visit `http://localhost:5173/`.

## Browser smoke checklist
- [ ] Home loads, navigation works, no console crashes.
- [ ] Complete onboarding including form validation.
- [ ] Go to /interest-assessment; answer six questions, submit; interest signals display.
- [ ] Request five career suggestions; each explanation appears and links to a valid career profile.
- [ ] /careers displays twelve illustrative careers; search and cluster filter work; empty search supports reset.
- [ ] /change-path: select path, cancel first, then confirm; switch again; progress survives in-app navigation.
- [ ] /dashboard: onboarding and assessment progress and current career display.
- [ ] /dashboard: compare up to three careers; fourth selection is disabled.
- [ ] Turn backend off: Career Explorer and Interest Assessment show recoverable error states.
- [ ] Start backend again: retry succeeds.
- [ ] Refresh page: in-memory progress resets as documented.
- [ ] Frontend `npm run build` succeeds.
- [ ] Full backend pytest passes, including `test_integration_smoke.py`.

## Coordination before final approval
Review integration branch independently; task-series features do not automatically appear in `integration`. Member 3 must supply approved TASK-010 schemas and progress before the dashboard's readiness area can be connected. Resolve conflicts through PR review, never blindly merge unrelated branches.
