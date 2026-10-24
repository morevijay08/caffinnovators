# TASK-006 — Career Catalogue and Career Explorer Review

Branch: `task5` based on `task4`, preserving TASK-002 through TASK-005.

## Implemented
- 12 fictional career summaries with unique, stable IDs, clusters, summaries, interest tags and skill tags. All marked `illustrative=true`.
- Interest tags align with TASK-005 scoring categories, including `problem_solving` and `helping_people`.
- FastAPI GET `/api/v1/careers`: optional case-insensitive `search` and `cluster` filters; returns `careers`, `clusters`, `total`.
- FastAPI GET `/api/v1/careers/{career_id}`: career summary detail; returns 404 for unknown ID.
- Pydantic schemas, catalogue services, tests for records, filtering, empty results, detail and bad query.
- React Career Explorer page at `/careers` with searchable, filterable cards, loading/error/empty states.
- Illustrative career profile page at `/careers/<career-id>` with interests and skills. TASK-008 later adds roadmaps.
- Header nav link to career explorer. No database or new packages.

## Local testing on Windows
From repository root:
```powershell
git status
git fetch origin
git switch --track origin/task5
```
If local task5 exists, use `git switch task5`. Save/commit work before switching.

Backend terminal:
```powershell
cd C:\Users\Admin\Desktop\caffinnovators\backend
python -m pip install -r requirements.txt
python -m pytest -q
python -m uvicorn app.main:app --reload --port 8000
```
Use `http://localhost:8000/docs`, `http://localhost:8000/api/v1/careers`, and `http://localhost:8000/api/v1/careers/software-developer`.

Frontend terminal:
```powershell
cd C:\Users\Admin\Desktop\caffinnovators\frontend
npm install
npm run build
npm run dev
```
Visit `http://localhost:5173/careers`.

## Acceptance checks
- [ ] Landing and onboarding + interest assessment still work.
- [ ] 12 illustrative careers appear when no filters are selected.
- [ ] Search `robots` matches Robotics Technician, ignoring case.
- [ ] Creative cluster filter returns creative careers only.
- [ ] Combined filters can return a friendly empty state; clear resets them.
- [ ] Selecting a card opens its detail with interests, skills and demo disclaimer.
- [ ] Unknown career ID returns 404 in API and informative UI.
- [ ] With backend stopped, UI shows a usable error/retry message.
- [ ] API tests pass and production React build passes.

## Boundaries
No salary, admission, formal eligibility or tuition claims. Not a recommendation engine: TASK-007 matches TASK-005 signals to this catalogue. No year-by-year roadmap; TASK-008 owns that. No persistent profiles. Do not mark DONE until local test evidence and review.

## Verification status
Source committed to GitHub and structure inspected; automated build and test commands have not run in this assistant environment.
