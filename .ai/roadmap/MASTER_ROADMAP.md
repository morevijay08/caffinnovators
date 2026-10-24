# MASTER ROADMAP — LIFEPath INDIA

Tasks follow dependency order, but independent tasks may run in parallel when the shared skeleton and interfaces are ready. Use `.ai/roadmap/MEMBER_TASK_ASSIGNMENTS.md` for owners and dependencies. Mark DONE only after acceptance criteria are verified.

## Phase 0 — Product contract, skeleton and core discovery
- [x] TASK-001 — Inspect reference, lock product/stack and create .ai control files.
- [ ] TASK-002 — Initialize Streamlit skeleton and application shell. **Owner: Member 1; integration prerequisite.**
- [ ] TASK-003 — Design system, responsive landing page and navigation. **Owner: Member 1; depends on TASK-002.**
- [ ] TASK-004 — Student onboarding and session state. **Owner: Member 1; depends on TASK-002/003 and shared state contract.**
- [ ] TASK-005 — Timed interest assessment with reflection and explainable scoring. **Owner: Member 2; depends on TASK-002/004 and assessment contract.**

## Phase 1 — Parallel feature work after contracts are merged
- [ ] TASK-006 — Fictional career catalogue and Career Explorer. **Owner: Member 2; depends on TASK-002/003 and career data contract.**
- [ ] TASK-007 — Explainable multi-career recommendation engine. **Owner: Member 2; depends on TASK-005/006.**
- [ ] TASK-008 — Detailed career page and illustrative year-by-year roadmap with transparent cost labels. **Owner: Member 2; depends on TASK-006/007.**
- [ ] TASK-009 — Timed Math Readiness Assessment with topic tags. **Owner: Member 3; depends on TASK-002/003 and assessment contract.**
- [ ] TASK-010 — Topic analysis, supportive improvement plan, progress checklist and retest. **Owner: Member 3; depends on TASK-009.**
- [ ] TASK-011 — Change My Path while preserving achievements and progress. **Owner: Member 1; depends on TASK-004/007 and shared state contract.**
- [ ] TASK-012 — Student dashboard and comparison of up to three careers. **Owner: Member 1; depends on TASK-004/007/010/011.**

## Phase 2 — Secondary demo modules
- [ ] TASK-013 — Interest Discovery Lab activities and reflection. **Owner: Member 2; depends on TASK-005/006.**
- [ ] TASK-014 — Transparent rule-based Career Assistant. **Owner: Member 2; depends on TASK-006/007/008.**
- [ ] TASK-015 — Fictional scholarship/affordability demo page. **Owner: Member 3; depends on agreed fictional-data schema and TASK-002.**
- [ ] TASK-016 — Feedback page and navigation/empty states. **Owner: Member 1; depends on TASK-003/004 and feature integration.**

## Phase 3 — Verification and demo readiness
- [ ] TASK-017 — Unit-test coordination for assessment, recommendations, improvement plan and path changes. **Coordinator: Member 3; each feature owner writes tests for their own logic.**
- [ ] TASK-018 — End-to-end manual smoke test and bug fixes. **Coordinator: Member 1; all members fix issues in their owned modules.**
- [ ] TASK-019 — README, setup instructions and accurate limitations. **Coordinator: Member 1; all members contribute accurate setup/feature notes.**
- [ ] TASK-020 — Hackathon demo script and final repository verification. **Coordinator: Member 1; all members verify their feature paths.**

## MVP definition of done
A judge can start at the landing page, complete onboarding and an interest assessment, review explained multiple career options, open a roadmap, take a timed math test, receive topic-level feedback and an improvement plan, then change career path without losing completed progress. The app runs with `streamlit run app.py` and requires no secret/API key or database.

## Scope rule
This roadmap is a delivery plan, not permission to implement everything in one pass. Members work only on assigned tasks whose dependencies are merged into `integration`. Do not introduce a student-facing AI model without explicit approval.
