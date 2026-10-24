# AI DEVELOPMENT RULES

## AI coding model
- Gemma 4 is the preferred coding assistant for this repository whenever available.
- Give the model the required `.ai/` instructions, member role, assigned task, allowed files, dependencies, API contracts, and acceptance criteria before asking it to edit.
- If Gemma 4 is not available in the current environment, disclose that; do not claim another model is Gemma 4.
- Gemma 4 has two separate roles: optional development coding assistant and approved student-facing runtime model for TASK-014. Runtime integration must use the backend Gemma adapter and documented API contract.
- Never provide secrets or private student data to an AI model.

## Before coding
- Read required control, product, stack, architecture, API contract, state, roadmap, team workflow, member assignment and task documents.
- Inspect current branch, repository tree, dependencies and existing code.
- Confirm assigned member, one active task, owned files, dependencies, API request/response schemas and acceptance criteria.
- Write a short implementation plan before editing.

## Task control and collaboration
1. Follow `.ai/TEAM_WORKFLOW.md` and `.ai/roadmap/MEMBER_TASK_ASSIGNMENTS.md`.
2. Parallel work is allowed only for independent tasks whose dependencies and API interfaces are agreed.
3. One task per feature branch and one owner per file; do not make overlapping edits to shared files.
4. Do not implement a task before its dependencies and required API contracts are merged into `integration`.
5. Do not implement future tasks early or mark work DONE without relevant testing and acceptance-criteria verification.
6. If requirements change, update state/roadmap explicitly.
7. Never push directly to `main` or `integration`; use a pull request.
8. Never force-push shared branches or resolve a conflict by blindly selecting one side.

## Code and dependencies
- Follow `.ai/TECH_STACK.md`; no unapproved packages or technology substitutions.
- Keep React components focused and accessible; use TypeScript types instead of spreading untyped data.
- Keep Python domain logic pure/testable where practical; keep FastAPI route handlers thin.
- Validate API requests/responses with Pydantic and keep TypeScript API types aligned with `.ai/API_CONTRACTS.md`.
- Use a single frontend API client and configured API base URL.
- No database. The approved chatbot may call local Ollama from FastAPI. Never call the model from React. Hosted inference is allowed only if explicitly chosen, with credentials held server-side in untracked environment variables.
- Preserve responsive design and reduced-motion/accessibility support.

## Student privacy and safety
- Fixtures use fictional data.
- Never use sensitive characteristics to restrict career recommendations.
- Do not shame students or present a short quiz as a diagnosis.
- Explain recommendation evidence and uncertainty.
- Label sample data, estimates and simulations clearly. Career Assistant answers are AI-generated guidance, not official advice; do not present generated claims about live scholarships, fees, salaries, eligibility or admissions as verified.

## Verification
Add/update tests for meaningful logic, run relevant tests/build/API checks, report exact commands and outcomes, and update current state/progress/changelog. Each PR must state scope, changed files, tests run, and known limitations.

## Stop conditions
Stop on destructive changes, conflicting requirements, unapproved stack changes, paid/external-service requirements, missing API contracts, or unsupported official claims that materially affect the product.
