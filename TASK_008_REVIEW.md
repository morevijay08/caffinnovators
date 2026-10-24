# TASK-008 — Career Detail and Illustrative Year-by-Year Roadmaps

**Member 2 task**, implemented on `task13` based on `task12`.

## Implemented
- Added `GET /api/v1/careers/{career_id}/roadmap` to the existing career router.
- The endpoint returns a Pydantic-validated `CareerRoadmap` containing career ID/title, illustrative flag, duration, four numbered stages (focus, two activities, milestone) and a student-friendly disclaimer.
- Added distinct project examples for all 12 existing career IDs in a pure deterministic Python roadmap service. No fabricated admission criteria, official qualifications, fees, salaries, job guarantees or fixed timelines.
- Added typed React API client and a responsive year-by-year roadmap timeline to existing career detail pages, with loading/error and retry affordances.
- Added `backend/tests/test_roadmaps.py` (12-career coverage, unknown-ID 404, deterministic content).
- No database, authentication, additional packages, Gemma runtime or changes to Member 3 code.

## Review on Windows
```powershell
cd C:\Users\Admin\Desktop\caffinnovators
git status
git fetch origin
git switch --track origin/task13
```
Use `git switch task13` if the branch already exists locally; save uncommitted edits before switching.

**Backend terminal**
```powershell
cd C:\Users\Admin\Desktop\caffinnovators\backend
python -m pytest -q
python -m uvicorn app.main:app --reload --port 8000
```

**Frontend terminal**
```powershell
cd C:\Users\Admin\Desktop\caffinnovators\frontend
npm install
npm run build
npm run dev
```

Open `http://localhost:5173/careers/software-developer`, `http://localhost:5173/careers/robotics-technician` and `http://localhost:5173/careers/sports-coach`.

## Acceptance checks
- [ ] Every career profile shows four numbered illustrative learning stages.
- [ ] Example milestones differ meaningfully between software, robotics and sports.
- [ ] Text makes clear this is not an official four-year requirement.
- [ ] Each stage has a focus, activities and sample milestone.
- [ ] Layout works on mobile widths.
- [ ] API docs show `GET /api/v1/careers/{career_id}/roadmap`.
- [ ] Unknown career roadmap returns HTTP 404 and a safe message.
- [ ] Temporarily stop FastAPI: career detail displays error; restart and retry.
- [ ] Existing Explorer/search/recommendation links still open careers.
- [ ] Run `npm run build` and `python -m pytest -q`; record actual results.

## Verification status
Files committed on GitHub. Automated/build/browser checks have not been executed on user's machine; **do not mark verified or merge** until the user checks. Other Member 2 tasks (TASK-013 and TASK-014) remain separate tasks.
