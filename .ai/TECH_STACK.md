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
- This is a developer workflow preference, not an application dependency. No Gemma runtime, model download, hosted inference, API key, Ollama service, or LLM SDK is required.
- Do not assume the model can access GitHub, local files, terminals, or execute tests unless the chosen tool explicitly provides those capabilities.

## Explicitly not approved for MVP
- Next.js or a second frontend framework.
- Tailwind, Bootstrap, shadcn/ui or another styling/component framework.
- LangChain, LangGraph, vector DB, embeddings or RAG.
- Student-facing hosted/local LLM, paid AI APIs or required external services.
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
A student-facing AI assistant, verified career-data imports, real scholarships, persistence, authentication, and production deployment require separate decisions; do not add them by default.
