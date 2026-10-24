# LIFEPath INDIA — AI MASTER DEVELOPMENT INSTRUCTIONS

You are an implementation agent for LifePath India, a student career-discovery platform. Gemma 4 is the preferred AI coding assistant for this repository when available in the user's chosen environment.

## Required reading before every task
1. `.ai/AI_RULES.md`
2. `.ai/PROJECT_CONTEXT.md`
3. `.ai/TECH_STACK.md`
4. `.ai/ARCHITECTURE.md`
5. `.ai/CURRENT_STATE.md`
6. `.ai/DECISIONS.md`
7. `.ai/TEAM_WORKFLOW.md`
8. `.ai/roadmap/MASTER_ROADMAP.md`
9. `.ai/roadmap/MEMBER_TASK_ASSIGNMENTS.md`
10. The active task in `.ai/tasks/`
11. Relevant product requirements and data notes.

## Preferred AI coding model
- Use Gemma 4 as the preferred model for coding, code explanation, planning, debugging, review, and test-writing whenever the environment provides access to it.
- Before editing, provide Gemma 4 with this repository's required instructions, the assigned member role, the single task, allowed file paths, dependencies, and acceptance criteria.
- If Gemma 4 is unavailable in the current tool/editor, do not pretend it was used. Tell the user and request permission before switching to another coding model if model choice is mandatory.
- The model is a development assistant, not a runtime dependency. Do not add Gemma 4, Ollama, Google AI Studio, an API key, or any LLM SDK to the app unless a separate task explicitly approves in-product AI integration.
- Never send secrets or private student data to a model.

## Required loop
READ → INSPECT → PLAN → IMPLEMENT ONE ASSIGNED TASK → TEST → VERIFY ACCEPTANCE CRITERIA → UPDATE STATE/LOGS → STOP.

## Team and scope control
- Follow `.ai/TEAM_WORKFLOW.md` and `.ai/roadmap/MEMBER_TASK_ASSIGNMENTS.md`.
- Work only on the current member's assigned task and owned files.
- Multiple members may work in parallel only on independent tasks after shared contracts and dependencies are ready.
- Never edit another member's owned files without explicit coordination.
- Do not implement a task before its dependencies are merged into the shared integration branch.
- Do not invent requirements, data sources, tools, routes, services, or technology choices.
- Do not introduce unapproved technologies, packages, APIs, external services, databases, or AI models.
- Do not rewrite architecture without explicit approval.
- Do not claim tests or verification unless they actually ran and passed.
- If blocked or a contract is missing, explain the blocker and stop rather than silently expanding scope.

## Product guardrails
- Interest and exploration are central; marks are not a verdict about potential.
- Never diagnose a student or declare a career unsuitable from one short quiz.
- Explain multiple recommendations and offer next steps.
- Clearly label simulated assessments/assistant responses and illustrative fees.
- Never invent institutions, official links, live scholarships, eligibility rules, fees, salaries, or admission outcomes.
- Use fictional demo student data and do not collect sensitive information.
- Use inclusive, non-shaming language and preserve the student's agency and ability to change paths.

## Cost discipline
No paid APIs, secrets, database, hosted AI model, or network-required runtime for the MVP. Any real AI model inside the student-facing application requires a separate approved task.

## Completion gate
Run relevant checks, inspect changes, verify each acceptance criterion, update `.ai/CURRENT_STATE.md`, `.ai/logs/PROGRESS.md`, and `.ai/logs/CHANGELOG.md`, record decisions if needed, and stop after the assigned task.
