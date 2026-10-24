# APPROVED PRODUCT AND ARCHITECTURE DECISIONS

## ADR-001 — Control system before product implementation
Status: APPROVED. Create project-specific agent rules and product/stack constraints before runtime code.

## ADR-002 — Streamlit monolith for hackathon
Status: APPROVED. Use Python + Streamlit with modular domain logic and static demo content. Rejected for MVP: React/TypeScript + FastAPI + database, due to integration overhead and the supplied brief's explicit stack.

## ADR-003 — No real AI dependency in first demo
Status: APPROVED. Use deterministic rule-based scoring, matching, topic feedback and a simulated assistant. Label simulation in the UI.

## ADR-004 — Interest-first and supportive recommendations
Status: APPROVED. Use interest/activity preferences and stated goals. Marks cannot be the sole gate. Explain multiple matches and never declare fixed destiny.

## ADR-005 — Source transparency
Status: APPROVED. Demo fees, scholarship listings and unverified pathway details are labelled illustrative/demo. Data format supports source URLs and last-verified date.

## ADR-006 — Session-only demo state
Status: APPROVED. Use Streamlit session state without database persistence in the hackathon MVP.
