# APPROVED PRODUCT AND ARCHITECTURE DECISIONS

## ADR-001 — Control system before product implementation
Status: APPROVED. Create project-specific agent rules and product/stack constraints before runtime code.

## ADR-002 — Streamlit monolith for hackathon
Status: SUPERSEDED on 2026-10-24 by ADR-007. The original Streamlit-only decision reflected the initial brief and is no longer the approved architecture.

## ADR-003 — Deterministic core logic; no AI dependency for scoring
Status: APPROVED for interest scoring, career matching, math scoring and topic feedback. These remain deterministic and testable. The earlier simulated Career Assistant portion is superseded by ADR-008.

## ADR-004 — Interest-first and supportive recommendations
Status: APPROVED. Use interest/activity preferences and stated goals. Marks cannot be the sole gate. Explain multiple matches and never declare fixed destiny.

## ADR-005 — Source transparency
Status: APPROVED. Demo fees, scholarship listings and unverified pathway details are labelled illustrative/demo. Data format supports source URLs and last-verified date.

## ADR-006 — Session-only demo state
Status: APPROVED WITH UPDATED IMPLEMENTATION DETAIL. No database or durable student profile storage. The React client may hold temporary UI/session state and the FastAPI backend may use in-memory data for a demo; do not promise persistence across refreshes or restarts.

## ADR-007 — React + TypeScript frontend with FastAPI backend
Status: APPROVED by explicit user instruction on 2026-10-24.
- Frontend: React + TypeScript + Vite, React Router and custom CSS.
- Backend: Python 3.11+, FastAPI, Pydantic and Uvicorn.
- Communication: typed frontend Fetch API client and documented JSON API contracts.
- Data: static fictional/demo content; no database, authentication, paid API or required external service.
- Rationale: user chose Option B to gain more control over a polished, interactive frontend while keeping Python for domain logic.
- Delivery guardrail: implement incrementally; do not rewrite the entire app in one task. TASK-002 creates the minimal runnable skeleton and API contract baseline.


## ADR-008 — Gemma 4 powers the student-facing Career Assistant
Status: APPROVED by explicit user instruction on 2026-10-24.
- Gemma 4 must be used at runtime for the student-facing Career Assistant; it is not only a development coding assistant.
- Default hackathon inference path: FastAPI backend → local Ollama service → Gemma 4 model. Default model name is configurable (`GEMMA_MODEL`, initial value `gemma4:e2b`); confirm the available Ollama tag on the implementation machine.
- React calls only `POST /api/v1/career-assistant`; it must never call Ollama or a hosted model provider directly.
- Keep model URL, timeout, model name and any hosted provider credentials in backend configuration. Never commit secrets.
- Hosted Gemma inference may be selected only after checking access, quota, cost and connectivity; it is not required for the default local path.
- Deterministic assessment scoring and career recommendation services remain authoritative and do not delegate scoring to the LLM.
- The assistant must not present generated content as official or verified; no guarantees about jobs, admissions, salaries, fees or scholarships.
- TASK-014 owns this implementation and tests.
