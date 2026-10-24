# AI DEVELOPMENT RULES

## Before coding
- Read required control, product, stack, state, roadmap and task documents.
- Inspect current branch, repository tree, dependencies and existing code.
- Confirm the single active task and its acceptance criteria.
- Write a short implementation plan before editing.

## Task control
1. Exactly one active task.
2. Follow `.ai/roadmap/MASTER_ROADMAP.md` order.
3. Do not implement future tasks early.
4. Code existence is not proof of completion.
5. Do not mark DONE without relevant testing and acceptance-criteria verification.
6. If requirements change, update state/roadmap explicitly.

## Code and dependencies
- No unapproved packages or technology substitutions.
- Keep Python modules focused and testable.
- Use `st.session_state` for prototype state; no database in MVP.
- Separate assessment logic from presentation and demo data.
- Validate user inputs; handle empty/error states.
- No API keys or runtime network requirements.
- Preserve responsiveness and accessibility; respect reduced-motion settings where practical.

## Student privacy and safety
- Fixtures must use fictional data.
- Never use sensitive characteristics to restrict career recommendations.
- Do not shame students or present a short quiz as a diagnosis.
- Explain recommendation evidence and uncertainty.
- Label sample data, estimates and simulation clearly.

## Verification
Add/update tests for meaningful logic, run relevant tests/app checks, report exact checks truthfully, and update current state/progress/changelog.

## Stop conditions
Stop on destructive changes, conflicting requirements, stack changes, paid/external-service requirements or unsupported official claims that materially affect the product.
