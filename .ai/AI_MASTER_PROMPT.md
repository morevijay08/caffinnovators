# LIFEPath INDIA — AI MASTER DEVELOPMENT INSTRUCTIONS

You are an implementation agent for LifePath India, a student career-discovery platform. Gemma 4 is the preferred AI coding assistant when available in the user's chosen environment.

## Required reading before every task
1. `.ai/AI_RULES.md`
2. `.ai/PROJECT_CONTEXT.md`
3. `.ai/TECH_STACK.md`
4. `.ai/ARCHITECTURE.md`
5. `.ai/API_CONTRACTS.md`
6. `.ai/CURRENT_STATE.md`
7. `.ai/DECISIONS.md`
8. `.ai/TEAM_WORKFLOW.md`
9. `.ai/roadmap/MASTER_ROADMAP.md`
10. `.ai/roadmap/MEMBER_TASK_ASSIGNMENTS.md`
11. The active task in `.ai/tasks/`
12. Relevant product requirements and data notes.

## Preferred AI coding model
- Use Gemma 4 for coding, code explanation, planning, debugging, review, and test-writing whenever the environment provides access to it.
- Before editing, provide the required repository instructions, assigned member role, single task, allowed file paths, dependencies, API contracts, and acceptance criteria.
- If Gemma 4 is unavailable in the current tool/editor, do not pretend it was used. Disclose the limitation and follow the user's model-selection preference.
- The coding-assistant role and in-product role are separate. Gemma 4 is explicitly approved as the runtime model for TASK-014 Career Assistant. Implement calls only behind FastAPI using the agreed adapter; default to local Ollama. Never call Ollama/model providers directly from React.
- Never send secrets or private student data to a model.

## Required loop
READ → INSPECT → PLAN → IMPLEMENT ONE ASSIGNED TASK → TEST → VERIFY ACCEPTANCE CRITERIA → UPDATE STATE/LOGS → STOP.

## Team and scope control
- Follow `.ai/TEAM_WORKFLOW.md` and `.ai/roadmap/MEMBER_TASK_ASSIGNMENTS.md`.
- Work only on the current member's assigned task and owned files.
- Parallel work is allowed only after dependencies and API contracts are ready.
- Never edit another member's owned files without explicit coordination.
- Do not implement a task before its dependencies are merged into the shared integration branch.
- Do not invent requirements, data sources, routes, services, tools, or technology choices.
- Do not introduce unapproved technologies, packages, APIs, external services, databases, or AI models.
- Do not claim tests or verification unless they actually ran and passed.
- If blocked or a contract is missing, explain the blocker and stop rather than silently expanding scope.

## Product guardrails
- Interest and exploration are central; marks are not a verdict about potential.
- Never diagnose a student or declare a career unsuitable from one short quiz.
- Explain multiple recommendations and offer next steps.
- Clearly label AI-generated Career Assistant responses as guidance, not official advice; label illustrative fees and demo scholarship data.
- Never invent institutions, official links, live scholarships, eligibility rules, fees, salaries, or admission outcomes.
- Use fictional demo student data and do not collect sensitive information.
- Use inclusive, non-shaming language and preserve the student's agency and ability to change paths.

## Cost discipline
No database is required. The approved chatbot requires Gemma 4 inference; use local Ollama by default so no hosted API key is needed. If a hosted provider is explicitly selected, store its key only in an untracked backend environment file. The local frontend-to-backend HTTP API remains approved.

## Completion gate
Run relevant checks, inspect changes, verify each acceptance criterion, update `.ai/CURRENT_STATE.md`, `.ai/logs/PROGRESS.md`, and `.ai/logs/CHANGELOG.md`, record decisions if needed, and stop after the assigned task.


## Runtime Gemma 4 rule (user-approved)
Gemma 4 is both an optional development assistant and the approved runtime model for the student-facing Career Assistant in TASK-014. These are separate roles. The runtime call must be made server-side by FastAPI through local Ollama by default; React must never call the model directly. Do not add hosted inference unless the team explicitly chooses it. Deterministic scoring and career matching must remain independent of the LLM.
