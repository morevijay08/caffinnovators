# TASK-002 — Review and local run instructions (branch: task1)

This branch introduces ONLY the initial React + TypeScript + Vite frontend and Python FastAPI backend. Existing Streamlit prototype files are preserved. Do not treat old root `app.py` or root `requirements.txt` as the approved new architecture.

## Frontend
Requirements: Node.js LTS, npm.

```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```

Open http://localhost:5173 . To check compilation and production bundling run `npm run build` from `frontend/`.

## Backend
Requirements: Python 3.11+.

```bash
cd backend
python -m venv .venv
# Activate the virtual environment (platform dependent).
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8000
```

Open http://localhost:8000/health . Expected HTTP 200 response:
```json
{"status":"ok","service":"lifepath-api"}
```

In another terminal run `cd backend && python -m pytest -q`. The frontend calls the health endpoint via `VITE_API_BASE_URL`; on the landing screen API connection should change to Connected. When the backend is stopped, it should instead show Unavailable.

For a custom frontend origin, configure `FRONTEND_ORIGIN` in the backend process environment. The backend default is `http://localhost:5173`. Vite's frontend example config defaults to `http://localhost:8000`.

## Review boundaries
- One shared API client: `frontend/src/api/client.ts`.
- Only `GET /health` has been introduced.
- No career, quiz, student-data, AI or persistence endpoints implemented.
- No extra UI component framework or database.
- Existing Streamlit files were intentionally not deleted.

## Verification status
The files were committed to GitHub and inspected via the GitHub connector. Container-side clone could not run because this runtime could not resolve github.com. Thus frontend `npm install`, `npm run build`, backend test execution and the browser-to-backend check remain **NOT VERIFIED**. Do not mark TASK-002 complete until a teammate runs the above checks and records the results.

## Next
Review and test this branch first. Only after acceptance should TASK-003 be started on a new task branch.
