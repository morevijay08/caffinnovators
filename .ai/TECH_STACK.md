# APPROVED TECH STACK — LIFEPath INDIA

Status: **APPROVED FOR HACKATHON MVP — React + TypeScript frontend with Python FastAPI backend.** This supersedes the earlier Streamlit-only decision. Do not change the stack again without explicit user approval.

## Frontend
- Node.js LTS and npm for frontend tooling and package scripts.
- React with TypeScript for the browser UI and reusable components.
- Vite for development server and production build.
- React Router for client-side page navigation.
- Plain CSS/CSS modules and shared design tokens for styling; no Tailwind, Bootstrap, or component framework unless separately approved.
- Browser Fetch API for calls to the Python backend.
- Use accessible semantic HTML, responsive layouts, keyboard focus states, and reduced-motion support.
- Avoid adding UI, chart, icon, state-management, or animation packages without a demonstrated need and explicit approval.

## Backend
- Python 3.11+.
- FastAPI for the JSON API.
- Pydantic models for request/response validation and shared API shapes.
- Uvicorn as the local ASGI development server.
- Python standard library for deterministic scoring, timers/business rules, and utilities.
- Pandas only where structured data processing provides value.
- No database for the MVP; use fictional/static demo data and explicitly documented in-memory/session behaviour.

## Testing
- pytest for Python services and API tests.
- Frontend test tooling must be chosen and documented when the frontend scaffold is created; prefer the smallest compatible setup that can test critical components and interactions.
- Verify frontend production build and backend startup/API health.
- Git/GitHub for version control and pull requests.

## Development AI assistant
- Preferred coding assistant: Gemma 4, when available through the team's chosen editor or model interface.
- Use it for repository understanding, planning, coding, code review, debugging, and test drafting.
- Separately, Gemma 4 is an approved student-facing runtime model for TASK-014. The default inference path is FastAPI → local Ollama → configurable Gemma 4 model (initial `GEMMA_MODEL=gemma4:e2b`, `OLLAMA_BASE_URL=http://localhost:11434`; verify the installed tag). Keep inference behind FastAPI; React must never call the model directly. Hosted inference is only an explicit fallback and any credentials stay server-side and untracked.
- Do not assume the model can access GitHub, local files, terminals, or execute tests unless the chosen tool explicitly provides those capabilities.

## Explicitly not approved for MVP
- Next.js or a second frontend framework.
- Tailwind, Bootstrap, shadcn/ui or another styling/component framework.
- LangChain, LangGraph, vector DB, embeddings or RAG.
- Unapproved AI providers or paid APIs. Gemma 4 runtime inference for TASK-014 is explicitly approved; follow `.ai/ARCHITECTURE.md` and `.ai/API_CONTRACTS.md`.
- PostgreSQL, MongoDB, Supabase, Firebase, Redis, or any other database.
- Authentication, analytics SDKs, paid APIs, or required external services.
- Any package added without demonstrated need and explicit approval.

## Repository direction
- `frontend/`: React + TypeScript + Vite app.
- `backend/`: FastAPI application and Python services.
- `backend/app/main.py`: API entry point.
- `backend/app/api/`: route handlers.
- `backend/app/schemas/`: Pydantic request/response models.
- `backend/app/services/`: deterministic career matching, interest scoring, math analysis, and learning-plan logic.
- `backend/app/data/`: fictional/static demo content.
- `backend/tests/`: backend tests.
- `frontend/src/`: pages, components, API client, types, styles.
- `frontend/` tests follow the frontend tooling decision made during TASK-002.
- Inspect the actual repository before creating files; do not duplicate existing structures.

## State and data
- Demo content is local and fictional/illustrative unless verified.
- No durable user profile storage or database in the MVP.
- Do not claim browser or in-memory progress survives refresh, a new session, or a server restart unless implemented and verified.
- API contracts are documented in `.ai/API_CONTRACTS.md`; keep TypeScript types and Pydantic schemas aligned.

## Local development and deployment
- Frontend and backend run as two local processes during development.
- Document exact commands, ports, environment variables, and CORS configuration in the README when TASK-002 implements the scaffold.
- No secrets or external API keys should be required for the MVP.

## Future integrations
Verified career-data imports, real scholarships, persistence, authentication, and production deployment require separate decisions. The Gemma 4-powered student-facing Career Assistant is explicitly approved.


## Approved runtime AI — Career Assistant only
- Runtime model: Gemma 4, called by the FastAPI backend for TASK-014.
- Default local serving option: Ollama; initial defaults `OLLAMA_BASE_URL=http://localhost:11434` and `GEMMA_MODEL=gemma4:e2b`. Validate the exact tag and available hardware during implementation.
- Keep model inference server-side. Never expose provider keys or call model endpoints from React.
- Hosted Gemma inference is an optional fallback only after an explicit team decision. All other application logic remains deterministic; no RAG, embeddings or vector database.
