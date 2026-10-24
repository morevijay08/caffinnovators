# TASK-020 — Final repository verification and demo readiness

Branch: `task12` based on `task11`. TASK-020 scope is team coordination, review and a truthful hackathon demo. The primary output is `HACKATHON_DEMO_SCRIPT.md`; this branch does not integrate unmerged teammate features.

## Repository verification gates

- [ ] Git working tree clean on `task12` (except intentionally local ignored artifacts).
- [ ] Review `.ai/AI_RULES.md`, `.ai/TECH_STACK.md`, `.ai/API_CONTRACTS.md`, `.ai/TEAM_WORKFLOW.md` and other members' handoff details.
- [ ] Backend: `python -m pytest -q` from `backend/`. Write the *actual* count below.
- [ ] Frontend: `npm run build` from `frontend/`. Write actual result below.
- [ ] Backend: `python -m uvicorn app.main:app --reload --port 8000`. Verify GET `/health` and `/docs`.
- [ ] Frontend: `npm run dev` from `frontend/` and load localhost:5173.
- [ ] Browser: home → onboarding → timed interest assessment → five career suggestions → career profile.
- [ ] Browser: Change My Path switch/confirmation/history preserves onboarding + assessment in app navigation.
- [ ] Browser: dashboard current career and three-career comparison; selection cap works.
- [ ] Browser: loading, no-results and backend-off error/retry behavior; narrow viewport and keyboard basics.
- [ ] Verify fictional/illustrative labels, scoring disclaimers, no sensitive student data stored, no secrets tracked.
- [ ] Member 2 reviews career/interest content and documents TASK-008/013/014 status.
- [ ] Member 3 reviews readiness/math/affordability test status and shares approved schemas for integration.
- [ ] Confirm PRs and shared `integration` state with teammates; do not assume pushing task12 merges it.
- [ ] Run the five-minute demo script and time the speaking transitions.
- [ ] Confirm the complete roadmap MVP scope actually exists on the final combined branch before promising it to judges.

## Exact Windows commands

```powershell
cd C:\Users\Admin\Desktop\caffinnovators
git status
git fetch origin
git switch --track origin/task12
```

Use `git switch task12` if it already exists locally; save uncommitted work before switching.

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

## Verification record — fill with real terminal results

- Date/time:
- Git commit:
- Pytest result:
- React production build result:
- Browser walkthrough:
- Member 2 sign-off:
- Member 3 sign-off:
- Known remaining bugs:
- Shared integration PR/merge status:

**At creation:** GitHub documentation commits completed. This assistant has not executed tests or browser walkthrough on the user's machine. Do not mark fully verified or merged. Member 3 maths/readiness, Member 2 roadmap/Gemma and other unmerged branches still require separate review.
