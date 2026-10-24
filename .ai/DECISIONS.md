# APPROVED PRODUCT AND ARCHITECTURE DECISIONS

## ADR-001 — Control system before product implementation
Status: APPROVED. Create project-specific agent rules and product/stack constraints before runtime code.

## ADR-002 — Streamlit monolith for hackathon
Status: SUPERSEDED on 2026-10-24 by ADR-007. The original Streamlit-only decision reflected the initial brief and is no longer the approved architecture.

## ADR-003 — No real AI dependency in first demo
Status: APPROVED. Use deterministic rule-based scoring, matching, topic feedback and a simulated assistant. Label simulation in the UI.

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
