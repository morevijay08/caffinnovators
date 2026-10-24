# KNOWN ISSUES AND OPEN RISKS — LifePath India

Reviewed: 2026-10-24. Applies to `task3` unless otherwise stated.

## KI-001 — Historical assumption that no runtime exists
Status: RESOLVED for Member 1 task branches.
Runtime React/FastAPI scaffold exists on `task1`, landing page on `task2`, onboarding on `task3`. No claim that every task is merged into `integration` or `main`.

## KI-002 — Career facts need verification
Status: OPEN.
Exact eligibility, fees, salaries, scholarships and institutional facts must be verified or identified as illustrative. Do not invent official information.

## KI-003 — Old Streamlit-only architecture instructions
Status: SUPERSEDED.
The approved stack is React + TypeScript + Vite frontend and FastAPI backend. Root Streamlit prototype files are legacy, not authorization to revive that stack. Read `.ai/TECH_STACK.md`.

## KI-004 — Session-only state
Status: ACCEPTED FOR MVP.
Onboarding state is held in React memory; full browser reload loses answers. No account/database persistence is implemented. Dashboard/path switching must share state without overstating persistence.

## KI-005 — Old simulated-assistant assumption
Status: SUPERSEDED.
TASK-014 requires real Gemma 4 runtime inference behind FastAPI, default local Ollama; it is a separate future task and is not implemented on `task3`.

## KI-006 — Task branch verification and integration
Status: OPEN.
TASK-002, 003 and 004 source files exist in successive branches. User confirmed local Vite startup and successful access to the corrected onboarding URL. Exact frontend build, backend test suite and complete onboarding interaction test results are not logged; do not mark fully verified or merged until checks are recorded.

## KI-007 — Accidental malformed onboarding URL
Status: RESOLVED by corrected URL; NOT a proven application bug.
A link/opened URL containing literal `**` after `/onboarding` hit the catch-all 404 page. Correct URL: `http://localhost:5173/onboarding`. Do not pass Markdown formatting characters into a URL.
