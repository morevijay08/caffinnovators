# AI DEVELOPMENT RULES

## AI coding model
- Gemma 4 is the preferred coding assistant for this repository whenever available.
- Give the model the required `.ai/` instructions, member role, assigned task, allowed files, dependencies, and acceptance criteria before asking it to edit.
- If Gemma 4 is not available in the current environment, disclose that; do not claim another model is Gemma 4.
- Gemma 4 is for development assistance only. It must not become an app dependency or call an external model at runtime unless the user explicitly approves a separate integration task.
- Never provide secrets or private student data to an AI model.

## Before coding
- Read required control, product, stack, state, roadmap, team workflow, member assignment and task documents.
- Inspect current branch, repository tree, dependencies and existing code.
- Confirm the assigned member, single active task, owned files, dependencies and acceptance criteria.
- Write a short implementation plan before editing.

## Task control and collaboration
1. Follow `.ai/TEAM_WORKFLOW.md` and `.ai/roadmap/MEMBER_TASK_ASSIGNMENTS.md`.
2. Parallel work is allowed only for independent tasks whose dependencies and interfaces are agreed.
3. One task per feature branch and one owner per file; do not make overlapping edits to shared files.
4. Do not implement a task before its dependencies are merged into `integration`.
5. Do not implement future tasks early or mark work DONE without relevant testing and acceptance-criteria verification.
6. If requirements change, update state/roadmap explicitly.
7. Never push directly to `main` or `integration`; use a pull request.
8. Never force-push shared branches or resolve a conflict by blindly selecting one side.

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
Add/update tests for meaningful logic, run relevant tests/app checks, report exact checks truthfully, and update current state/progress/changelog. Each pull request must state scope, changed files, tests run, and known limitations.

## Stop conditions
Stop on destructive changes, conflicting requirements, stack changes, paid/external-service requirements or unsupported official claims that materially affect the product.
