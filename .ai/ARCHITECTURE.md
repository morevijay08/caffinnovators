# ARCHITECTURE — LIFEPath INDIA

## Principle
A React + TypeScript browser frontend communicates with a Python FastAPI backend over a documented JSON API. The MVP uses deterministic Python domain services and static fictional/demo data. No database or external AI service is required.

## Request flow
Student browser → React page/component → typed frontend API client → FastAPI route → Pydantic validation → pure Python domain service → static demo data/in-memory request state → JSON response → React UI.

## Repository structure
- `frontend/`: React + TypeScript + Vite app.
- `frontend/src/app/`: app shell and route configuration where useful.
- `frontend/src/pages/`: landing, onboarding, interest discovery, career explorer/detail, assessments, learning plan, dashboard, path change and affordability demo.
- `frontend/src/components/`: reusable cards, navigation, progress indicators, explanation panels, forms and accessible UI elements.
- `frontend/src/api/`: typed fetch client and API functions.
- `frontend/src/types/`: shared frontend request/response types aligned with API contracts.
- `frontend/src/styles/`: global CSS, tokens and component styles.
- `backend/app/main.py`: FastAPI app and CORS setup.
- `backend/app/api/`: route handlers; keep routes thin.
- `backend/app/schemas/`: Pydantic request/response models.
- `backend/app/services/`: pure, testable interest scoring, career matching, readiness analysis and learning-plan logic.
- `backend/app/data/`: fictional catalogue, activities, math questions and demo scholarship cards.
- `backend/tests/`: backend and API tests.
- `.ai/`: project instructions, contracts, decisions, task files, roadmap and logs.

Inspect the repository before creating folders; these are intended conventions, not proof that files already exist.

## API boundary
- Use JSON over HTTP between frontend and backend.
- Keep API contracts in `.ai/API_CONTRACTS.md`; route handlers, Pydantic schemas and TypeScript types must agree.
- Use a single configured API base URL; never hardcode different URLs in components.
- Configure CORS only for the local frontend origin needed in development; do not use wildcard origins with credentials.
- Return useful, consistent error responses; validate requests at the API boundary.
- Keep career/scoring logic in services, not in React components or route handlers.
- No secret, API key, database, or external network service is required.

## State and privacy
- The frontend may keep temporary UI state in React state/context; use only as much shared state as required.
- Assessment results and selected career may be kept in browser memory for the demo, with limitations stated clearly. Do not claim refresh-safe or durable persistence unless implemented and verified.
- Backend must not pretend to provide user accounts or durable profiles.
- Use fictional demo data and avoid unnecessary personal/sensitive information.

## UI direction
Palette: navy #14213D, teal #20C997, amber #FFBF69, background #F7F9FC, white cards, primary text #182230, secondary #64748B. Use a cohesive responsive design system, clear hierarchy, accessible contrast, focus states, reduced-motion support, and no required remote fonts/images/CDNs. Prioritize usable assessment interactions and clear feedback over decorative animation.

## Trust boundary
Rule-based recommendations are heuristics and must explain matching signals. Short diagnostics are not definitive measures of ability. Fees, scholarships and route details are illustrative unless verified. The career assistant is rule-based/simulated; no LLM runtime is required.
