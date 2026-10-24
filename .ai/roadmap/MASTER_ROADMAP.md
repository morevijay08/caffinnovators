# MASTER ROADMAP — LIFEPath INDIA

Tasks follow dependency order. Independent work may run in parallel only after required frontend/backend foundations and API contracts are merged. See `.ai/roadmap/MEMBER_TASK_ASSIGNMENTS.md`. Mark DONE only after acceptance criteria are verified.

## Phase 0 — Product contract, skeleton and core discovery
- [x] TASK-001 — Define product and create AI/project-control documentation.
- [ ] TASK-002 — Initialize React + TypeScript/Vite frontend and FastAPI backend skeleton; establish local run commands and API contract baseline. **Owner: Member 1 coordinates; Members 2/3 review service/API boundaries; integration prerequisite.**
- [ ] TASK-003 — React design system, responsive landing page and routing. **Owner: Member 1; depends on TASK-002.**
- [ ] TASK-004 — Student onboarding and temporary client state. **Owner: Member 1; depends on TASK-002/003 and state/API contract.**
- [ ] TASK-005 — Timed interest assessment and explainable scoring service/API. **Owner: Member 2; depends on TASK-002/004 and assessment contract.**

## Phase 1 — Parallel feature work after contracts are merged
- [ ] TASK-006 — Fictional career catalogue and Career Explorer. **Owner: Member 2; depends on TASK-002/003 and career data/API contract.**
- [ ] TASK-007 — Explainable multi-career recommendation service/API. **Owner: Member 2; depends on TASK-005/006.**
- [ ] TASK-008 — Career detail and illustrative year-by-year roadmap via API. **Owner: Member 2; depends on TASK-006/007.**
- [ ] TASK-009 — Timed Math Readiness Assessment and topic-tagged questions via API. **Owner: Member 3; depends on TASK-002 and assessment contract.**
- [ ] TASK-010 — Topic analysis, supportive improvement plan, checklist and retest service/API. **Owner: Member 3; depends on TASK-009.**
- [ ] TASK-011 — Change My Path while preserving completed client-side progress. **Owner: Member 1; depends on TASK-004/007 and shared state contract.**
- [ ] TASK-012 — Dashboard and comparison of up to three careers. **Owner: Member 1; depends on TASK-004/007/010/011 and API contracts.**

## Phase 2 — Secondary demo modules
- [ ] TASK-013 — Interest Discovery Lab activities and reflection. **Owner: Member 2; depends on TASK-005/006.**
- [ ] TASK-014 — Gemma 4-powered Career Assistant API/UI. **Owner: Member 2; depends on TASK-002/006/007/008 and Gemma runtime configuration; default path is FastAPI → Ollama → Gemma 4. Member 1 owns chat UI; Member 3 coordinates failure-path tests.**
- [ ] TASK-015 — Fictional scholarship/affordability demo using static data. **Owner: Member 3; depends on TASK-002 and demo-data contract.**
- [ ] TASK-016 — Feedback, loading, empty and error states. **Owner: Member 1; depends on TASK-003/004 and feature integration.**

## Phase 3 — Verification and demo readiness
- [ ] TASK-017 — Coordinate frontend/backend tests and API contract coverage. **Coordinator: Member 3; every feature owner tests their own logic.**
- [ ] TASK-018 — End-to-end smoke test and integration fixes. **Coordinator: Member 1; all members fix issues in owned modules.**
- [ ] TASK-019 — README, two-process local setup, API configuration and limitations. **Coordinator: Member 1; all contribute accurate notes.**
- [ ] TASK-020 — Hackathon demo script and final repository verification. **Coordinator: Member 1; all members verify their feature journeys.**

## MVP definition of done
A judge can complete onboarding and interest assessment, review multiple explained career options, open a roadmap, take a timed math test, receive topic-level feedback and an improvement plan, and change career path without losing completed progress. The React frontend and FastAPI backend run locally using documented commands. No database is required. The Career Assistant uses Gemma 4 at runtime through local Ollama by default; a hosted provider is optional only if explicitly selected.

## Scope rule
This roadmap is a delivery plan, not permission to implement everything in one pass. Work only on assigned tasks whose dependencies and API contracts are integrated. Gemma 4 runtime use for TASK-014 is explicitly approved; do not add other models/providers or use the LLM for deterministic scoring without approval.
