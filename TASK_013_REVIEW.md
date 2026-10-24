# TASK-013 — Interest Discovery Lab (Member 2)

Branch `task14` extends `task13`.

## Delivered
- Six illustrative hands-on activities aligned with existing TASK-005 interest categories (technology/design, environment/science, writing/arts, helping/business, mathematics/problem solving, sports/helping).
- Backend GET `/api/v1/discovery-activities` with optional case-insensitive `interest` filter; Pydantic response and four tests.
- React page `/discovery-lab` with interest filter, activity steps, reflection prompt, client-only saved reflections, error/retry and responsive styles. No grade, talent test, AI, account or database.
- All data are fictional/illustrative. Session-only reflections disappear on browser refresh.

## Test locally (Windows)
```powershell
cd C:\Users\Admin\Desktop\caffinnovators
git status
git fetch origin
git switch --track origin/task14
```
Use `git switch task14` if it already exists locally.

Backend terminal:
```powershell
cd C:\Users\Admin\Desktop\caffinnovators\backend
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

Visit `http://localhost:5173/discovery-lab` and `http://localhost:8000/docs`.

## Checks
- [ ] Six activity cards visible for All interests.
- [ ] SCIENCE interest yields Nature detective and relevant tasks only.
- [ ] Activities show materials, numbered steps and reflective question.
- [ ] Empty reflection cannot be saved; non-empty can be saved and shown.
- [ ] Reflection remains while navigating pages but is cleared by refreshing the browser.
- [ ] Network/server error displays an actionable Try again.
- [ ] Responsive view, keyboard operation and links work.
- [ ] Backend pytest and frontend npm run build pass; record actual results.

**Verification status:** GitHub implementation committed; no local test/build outcomes observed. No merge into main/integration. TASK-014 is separate.
