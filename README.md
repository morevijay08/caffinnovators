# LifePath India

**Every Interest Has a Future.** An interest-first Streamlit prototype for career exploration.

## TASK-002: Streamlit skeleton

This branch currently implements **only the navigation and application scaffold**. The Home view and all other pages are placeholders; assessments, recommendation services, learning roadmaps, dashboards, and onboarding are not functional yet. There is no authentication, database, or student-facing AI runtime.

## Run locally

Requires Python 3.11+.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

On macOS/Linux, activate with `source .venv/bin/activate`. Streamlit usually serves at http://localhost:8501.

## Tests

```powershell
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

## Structure

- `app.py`: application entry point and registered navigation
- `pages/`: temporary page placeholders awaiting their respective tasks
- `components/`: session defaults and reusable placeholder UI
- `services/`: pure domain logic to be added by feature owners
- `data/`: fictional catalogue and question content to be added
- `assets/`: optional local assets
- `tests/`: smoke tests for structure

Session state is temporary and resets when a user session ends; it is **not** a stored profile. No credentials or paid APIs are needed to launch the shell.
