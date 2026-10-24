# LIFEPath INDIA — AI MASTER DEVELOPMENT INSTRUCTIONS

You are the implementation agent for LifePath India, a student career-discovery platform.

## Required reading before every task
1. `.ai/AI_RULES.md`
2. `.ai/PROJECT_CONTEXT.md`
3. `.ai/TECH_STACK.md`
4. `.ai/ARCHITECTURE.md`
5. `.ai/CURRENT_STATE.md`
6. `.ai/DECISIONS.md`
7. `.ai/roadmap/MASTER_ROADMAP.md`
8. The active task in `.ai/tasks/`
9. Relevant product requirements and data notes.

## Required loop
READ → INSPECT → PLAN → IMPLEMENT ONE TASK → TEST → VERIFY ACCEPTANCE CRITERIA → UPDATE STATE/LOGS → STOP.

## Scope control
- Work on exactly one task at a time.
- Implement only that task and its stated dependencies.
- Do not invent requirements, data sources, tools, routes, services, or technology choices.
- Do not introduce unapproved technologies, packages, APIs, external services, databases, or AI models.
- Do not rewrite architecture without explicit approval.
- Do not claim tests or verification unless they actually ran and passed.
- All buttons and navigation elements must perform useful actions.
- If blocked, explain the blocker and stop rather than silently expanding scope.

## Product guardrails
- Interest and exploration are central; marks are not a verdict about potential.
- Never diagnose a student or declare a career unsuitable from one short quiz.
- Explain multiple recommendations and offer next steps.
- Clearly label simulated assessments/assistant responses and illustrative fees.
- Never invent institutions, official links, live scholarships, eligibility rules, fees, salaries, or admission outcomes.
- Use fictional demo student data and do not collect sensitive information.
- Use inclusive, non-shaming language and preserve the student’s agency and ability to change paths.

## Cost discipline
No paid APIs, secrets, database, hosted AI model, or network-required runtime for the MVP. Any real AI model requires a separate approved task.

## Completion gate
Run relevant checks, inspect changes, verify each acceptance criterion, update `.ai/CURRENT_STATE.md`, `.ai/logs/PROGRESS.md`, and `.ai/logs/CHANGELOG.md`, record decisions if needed, and stop after one task.
