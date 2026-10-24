# LifePath India — Every Interest Has a Future

Current Development

This repository contains the LifePath India application, including the Streamlit frontend and FastAPI backend.

**Interest-first career exploration for students.** This repository contains a React + TypeScript frontend and a Python FastAPI backend with illustrative career content and deterministic, explainable interest matching. Built as a hackathon MVP.


> **Working application:** run the `frontend/` and `backend/` directories. Root-level `app.py` and Streamlit files are a **legacy prototype** retained for reference; they are not the current frontend.

## Requirements

- Node.js LTS with npm
- Python **3.11 or newer** (3.11+); the team has also run the backend using Python 3.13
- Git and two terminals
- No account, database, API key, paid service, or Ollama installation is required for the currently implemented core flow.

## Local setup — Windows PowerShell

Clone the repository if necessary:

```powershell
git clone https://github.com/morevijay08/caffinnovators.git
cd caffinnovators
git fetch origin
git switch --track origin/task11
```

If you already have the repository, open its root folder and run `git fetch origin`, then `git switch --track origin/task11`. If `task11` already exists locally, run `git switch task11`. Check `git status` and save local changes before changing branches.

**Terminal 1 — API:**

```powershell
cd C:\Users\Admin\Desktop\caffinnovators\backend
python -m pip install -r requirements.txt
python -m pytest -q
python -m uvicorn app.main:app --reload --port 8000
```

Keep it running. Confirm [http://localhost:8000/health](http://localhost:8000/health) and [http://localhost:8000/docs](http://localhost:8000/docs).

**Terminal 2 — React UI:**

```powershell
cd C:\Users\Admin\Desktop\caffinnovators\frontend
npm install
npm run build
npm run dev
```

Open [http://localhost:5173/](http://localhost:5173/). Run the commands from the indicated folders: **do not `cd frontend` again if your terminal is already inside `frontend`**.

Alternatively, use `python -m venv .venv` under `backend/` and activate the environment before installing the backend requirements.

### macOS / Linux

From the repository root, use separate terminals:

```bash
cd backend
python3 -m pip install -r requirements.txt
python3 -m pytest -q
python3 -m uvicorn app.main:app --reload --port 8000
```

```bash
cd frontend
npm install
npm run build
npm run dev
```

## Environment configuration

The frontend defaults to backend `http://localhost:8000`. To override, define `VITE_API_BASE_URL` in a local, untracked `frontend/.env.local` (for example `VITE_API_BASE_URL=http://localhost:8000`) and restart Vite.

The backend CORS policy defaults to frontend origin `http://localhost:5173`. If Vite uses another origin, set `FRONTEND_ORIGIN` before starting Uvicorn, e.g.:

```powershell
$env:FRONTEND_ORIGIN="http://localhost:5174"
python -m uvicorn app.main:app --reload --port 8000
```

Do not add secrets to frontend environment variables; Vite exposes `VITE_*` variables to browsers.

## Features available on branch `task11`

| Feature | UI route | Notes |
|---|---|---|
| Landing and navigation | `/` | Responsive React landing |
| Student onboarding | `/onboarding` | Stage, interests and goal; temporary React state |
| Timed interest activity | `/interest-assessment` | Six illustrative questions and server-computed signals |
| Explained recommendations | On assessment results | Server-calculated career overlap with explanations; five default options |
| Career Explorer | `/careers` | Search/filter 12 fictional/illustrative careers |
| Career profiles | `/careers/:careerId` | Summary, interests and skills |
| Change My Path | `/change-path` | Confirm switches and retain progress while navigating |
| Dashboard | `/dashboard` | Onboarding/assessment/path summary; compare up to 3 careers |
| Feedback states | Throughout | Loading, empty, errors and retry affordances |

**Suggested demo journey:** Home → onboarding → interest assessment → interest signals → “See career suggestions” → career profile → “Change My Path” → dashboard → compare three career profiles.

## API reference

FastAPI serves API docs at `http://localhost:8000/docs`. Currently registered endpoints on this task-series branch:

| Method | Path | Purpose |
|---|---|---|
| GET | `/health` | Service health |
| GET | `/api/v1/interest-assessment` | Get public question choices and duration |
| POST | `/api/v1/interest-assessment/submit` | Validate and score six answers |
| GET | `/api/v1/careers` | List careers; optional `search` and `cluster` query parameters |
| GET | `/api/v1/careers/{career_id}` | Retrieve a profile; unknown IDs return 404 |
| POST | `/api/v1/recommendations` | Validate original answers and rank catalogue careers; `limit` 1–12 |

Example POST body for **recommendations** (first retrieve the question/option IDs from the GET assessment endpoint):

```json
{
  "answers": [
    {"question_id": "q1", "option_id": "a"},
    {"question_id": "q2", "option_id": "a"},
    {"question_id": "q3", "option_id": "a"},
    {"question_id": "q4", "option_id": "a"},
    {"question_id": "q5", "option_id": "a"},
    {"question_id": "q6", "option_id": "a"}
  ],
  "limit": 5
}
```

Option IDs must actually belong to their corresponding question. Recommendation scores measure heuristic overlap of selected interest signals with career tags; they are **not probabilities, diagnoses, eligibility evaluations, or career guarantees**. The backend rejects invalid answers with HTTP 422.

## Quality checks

Run backend tests from `backend/`:

```powershell
python -m pytest -q
```

Run frontend TypeScript verification and production bundle build from `frontend/`:

```powershell
npm run build
```

The backend includes endpoint and cross-feature integration smoke tests in `backend/tests/`. `TASK_018_REVIEW.md` provides a human browser walkthrough. The last previously reported fixed-branch run passed 18 tests; TASK-018 subsequently added 3 integration tests. **Do not claim 21/21 or frontend build success without running the commands on the current branch.** A Starlette/httpx compatibility deprecation warning may occur while tests otherwise pass.

## Architecture at a glance

```text
frontend/                    React + TypeScript / Vite / React Router
  src/pages/                Onboarding, assessment, careers, change path, dashboard
  src/components/           Layout, recommendations, feedback
  src/state/                Session-only StudentJourney React Context
  src/api/                  Typed Fetch API clients
backend/                     Python FastAPI / Pydantic / pytest
  app/main.py               Routers, CORS and health check
  app/api/                  HTTP endpoints
  app/schemas/              API models
  app/services/             Deterministic scoring and career matching
  app/data/                 Illustrative careers and interest questions
  tests/                    API/domain/integration smoke tests
.ai/                         Team workflow, API contracts and task history
TASK_*_REVIEW.md             Per-task review/checklists
app.py, pages/, ...          Legacy Streamlit prototype (not active UI)
```

## Honest limitations and roadmap gaps

- **No database, sign-in or persistent storage.** Onboarding answers, assessment progress, career path and comparison selections live in React memory and disappear on a full browser refresh. No student records are written to the backend.
- **Demo content only.** Career profiles, interest categories and matching are illustrative. No real tuition, scholarship, admission or job outcome claims.
- **No completed roadmaps** on this branch; detailed year-by-year career pathways belong to TASK-008.
- **Math readiness** TASK-009/TASK-010 work from other members is not integrated into this task-series branch; the dashboard states that readiness results are pending. Other team branches may contain separate work but are not automatically included.
- Interest assessment timer is client-side only; there is no server-enforced timeout.
- No TASK-013 discovery lab, TASK-014 Gemma runtime chatbot or TASK-015 affordability module on this branch. Gemma 4 via FastAPI → Ollama is the approved *future* TASK-014 integration, **not currently running** in this application.
- `integration` and `main` can differ from the task-series branches. Do not merge unrelated feature branches blindly; use reviewed PRs and respect the `.ai/TEAM_WORKFLOW.md` contract.

## Troubleshooting

| Problem | What to check |
|---|---|
| `ModuleNotFoundError: app` | Run Uvicorn and pytest **from `backend/`** |
| Browser says API is unavailable | Start backend on port 8000; check `/health`; verify `VITE_API_BASE_URL` |
| CORS error | Make `FRONTEND_ORIGIN` match the actual Vite page origin |
| `cd frontend` cannot find folder | Check `pwd`; you may already be inside `frontend/` |
| Port already used | Stop old server or coordinate port and environment variables |
| Progress disappeared | Expected after full browser refresh: React state is temporary |
| Tests fail on old `ROBOTS`/404 assertions | Fetch the latest reviewed task branch; corrections were introduced on `fix/task8-backend-tests` and carried forward |
| Deprecation warning involving Starlette/httpx | Usually non-blocking if all pytest tests pass; review dependency compatibility separately |

## Team and project process

TASK-019 documentation was authored on `task11` based on `task10`. The source of truth for task scope, ownership, contracts and integration is under `.ai/`. Members 1/2/3 should review feature acceptance and PRs before shared-branch merges. Refer to `TASK_019_REVIEW.md` for this documentation's checklist.

**Every Interest Has a Future.** Career direction is exploratory, not predetermined.


## TASK-008 — Illustrative career roadmaps on `task13`
The current Member 2 task branch `task13` adds `GET /api/v1/careers/{career_id}/roadmap`. All twelve existing career profiles now have four illustrative year-labelled stages, activities and examples of portfolio milestones. The route uses the same catalogue IDs and is shown on `/careers/:careerId`. These stages are not official education or admission requirements. For local testing use `TASK_008_REVIEW.md`. This branch updates the earlier README limitation that roadmaps were not yet implemented; other pending math, affordability and Gemma modules remain unintegrated.
