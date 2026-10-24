# Full-stack audit and student persistence — review branch

Branch: `feature/student-auth-persistence-ollama-integration` (based on `main`). **No merge to main has been performed.**

## Implemented
- Restored Member 2's missing Gemma Career Assistant backend/frontend files from `fix/task15-ollama-timeout`. Registered `POST /api/v1/career-assistant`, React route `/career-assistant` and navigation. Its Ollama adapter uses bounded output, timeout and graceful errors. Live Gemma/Ollama still needs local verification.
- Pseudonymous username/password student accounts using PBKDF2-SHA256 with random salt (310k iterations), opaque random 7-day session tokens hashed in SQLite, HttpOnly SameSite=Lax cookies; configurable `COOKIE_SECURE=1` for HTTPS.
- Added `POST /api/v1/auth/register`, `POST /api/v1/auth/login`, `GET /api/v1/auth/me`, `POST /api/v1/auth/logout`, `GET /api/v1/journey`, `PATCH /api/v1/journey`.
- Added SQLite tables for students, sessions and per-student journeys alongside existing math-attempt table. DB creates tables during app startup. Passwords are never returned or stored as plaintext.
- Persisted account-owned onboarding profile, selected interests/favourite subjects, completed interest-assessment signals/answers, selected career, path history, Discovery Lab reflections, latest math result, career comparison selection, and bounded Gemma chat history.
- Added a sign-in/registration route, gated student pages, save-error notice and sign-out navigation; updated outdated transient-state UI copy.
- Added backend auth/isolation/invalid-input/origin tests; existing math tests still need to be run.
- CORS now allows only configured frontend origin, credentialed requests and required PATCH method.

## Known caveats / NOT completed
- **Not a verified exhaustive bug-free audit.** GitHub connector changes cannot run user's local npm build, pytest, browser UI, SQLite migrations or Ollama model. Verify all commands and flows below.
- Built for local hackathon development only: no password reset, brute-force rate limiting, multi-device revocation, database encryption, deployment hardening, or guardian/age consent handling. Never deploy student data to the public internet until these have been addressed.
- Existing anonymous `/api/v1/math-assessment/attempts/{uuid}` can still retrieve a result by an unguessable UUID. The new account saves a *copy of the latest math result*, but the legacy endpoint and table need separate privacy/ownership migration before production use.
- Current in-progress unsent forms, timers, filter selections and quiz drafts remain transient. Persisting every keystroke is not appropriate. Completed progress, latest math result and saved reflections are persisted.
- Save actions update UI optimistically then send changes to SQLite in order; if a network write fails, a visible warning appears and the action should be repeated. A retry queue/durable offline sync is future work.
- No automatic import of profiles created before authentication (previously nothing was persisted).
- Ollama is **not bundled** and a verified installed Gemma 4 model is still required. The model is server-side; the app cannot supply a reply when the runtime is missing.

## On Windows — test this branch safely
```powershell
cd C:\Users\Admin\Desktop\caffinnovators
git status
git fetch origin
git switch --track origin/feature/student-auth-persistence-ollama-integration
```
If it already exists locally, use `git switch feature/student-auth-persistence-ollama-integration`. Save ongoing changes and resolve any active merge before switching. **Do not overwrite a working main checkout.**

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

Open `http://localhost:5173/auth` and create a pseudonymous test account.

## Acceptance checklist
- [ ] Registration returns 201 and sets HttpOnly cookie; duplicate username rejected.
- [ ] Login rejects wrong password; logout removes access.
- [ ] Complete onboarding, interest quiz, Change Path, comparison, Discovery Lab reflection and math assessment; refresh and verify each completed item is restored.
- [ ] Sign out and register a second student; no account A data should appear for student B.
- [ ] Browser API requests to `PATCH /api/v1/journey` work from localhost:5173 without CORS errors.
- [ ] User's new math score appears on dashboard and matches submitted result.
- [ ] Open Career Assistant; if Ollama is absent, friendly 503; if running verified Gemma, real chat response and restored chat after refresh.
- [ ] Confirm existing /careers, /assessment, /scholarships API/UI still function.
- [ ] `python -m pytest -q` and `npm run build` pass; record actual observed results.
- [ ] Review database privacy, schema, account recovery and rate limiting before any public deployment.

**Status:** Implementation pushed to separate review branch. Tests and local environment not verified here. No main or integration merge.
