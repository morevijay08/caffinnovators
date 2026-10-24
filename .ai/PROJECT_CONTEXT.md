# LIFEPath INDIA — COMPLETE PROJECT BRIEF & AI HANDOFF

> **Purpose of this file:** This is the project's portable source of context. A new teammate or any AI coding assistant should be able to read this file first, understand what we are building and why, identify the approved implementation approach, and then continue work without inventing a different product. Keep it consistent with the more detailed control files linked below.

## 1. Project identity

- **Product:** LifePath India
- **Tagline:** *Every Interest Has a Future.*
- **Type:** Hackathon MVP for student career discovery, career exploration, and learning-readiness guidance.
- **Primary context:** Indian education and career pathways.
- **Intended users:** Students in Classes 8–12, diploma students, and college students who are exploring possible futures.
- **Main idea:** Help students explore careers through their interests, curiosity, preferred activities, goals, and learnable skills—not through marks alone.
- **Repository:** https://github.com/morevijay08/caffinnovators
- **Current documentation home:** `.ai/`

## 2. The problem we are solving

Students may feel pressured to choose a career because of marks, family or social expectations, or limited knowledge of available options. Some students already have a career goal but do not know the steps to pursue it. Others do not yet know what they enjoy or what careers connect to their interests. Students may also struggle in a school subject and need a constructive way to identify topics to practise.

LifePath India should help both groups:
1. **Students who have some direction:** make their goal more concrete with career information, a staged roadmap, and learning next steps.
2. **Students who are unsure:** try interest-discovery activities, reflect on what they enjoyed, and explore several plausible options without being forced to choose one immediately.

The app is a supportive exploration tool, not an authority that decides a student's future.

## 3. Product principles and non-negotiable guardrails

1. **Interest first, not marks first.** Marks may provide context for a learning plan but must not decide a student's worth or permanently exclude a career.
2. **Exploration before commitment.** Show multiple reasonable career options and let students compare them.
3. **Explain recommendations.** State which answers, interests, activities, or preferences contributed to a match. Do not present a score as scientific certainty.
4. **Ability can grow.** A weak quiz result means “topics to practise next,” not “you cannot do this career.”
5. **Student agency.** Students can revisit answers, explore alternatives, and change their path.
6. **Preserve progress.** Changing a selected career must not erase completed assessments, achievements, or learning progress.
7. **Inclusive language.** Never shame, diagnose, stereotype, or describe a student's future as fixed.
8. **Be honest about evidence.** Mark sample careers, roadmaps, costs, questions, assistant responses, and scholarship cards as illustrative or simulated wherever they are not verified real-world data.
9. **Protect privacy.** Use fictional demo data. Do not ask for unnecessary sensitive personal details or claim to save data permanently.
10. **No fabricated authority.** Do not invent official links, institutions, live scholarship availability, admission criteria, eligibility, exact fees, salary outcomes, or job guarantees.

## 4. Core user journeys

### Journey A — “I know what I like”
Landing page → lightweight onboarding → timed interest assessment → explained multi-career recommendations → open career details → compare/save options → see roadmap and next steps.

### Journey B — “I don't know what I like yet”
Landing page → onboarding → Interest Discovery Lab → short activities and reflection → identify themes the student enjoyed → explore several career options → optionally take the interest assessment.

### Journey C — “I already have a goal”
Career Explorer or recommendation → career detail → staged illustrative roadmap → readiness assessment where useful → actionable learning plan.

### Journey D — “Maths is difficult for me”
Timed Math Readiness Assessment → results grouped by topic → supportive explanation of strengths and practice areas → manageable improvement checklist → retest → compare progress over time within the current session.

### Journey E — “I want to change my career choice”
Change My Path → show alternative career options → choose a new path → preserve completed assessments, achievements, and progress → update the active roadmap and dashboard.

## 5. MVP features and expected behaviour

The following describes the intended product. It is **not a claim that these runtime features have already been implemented**.

1. **Landing page:** clear product promise, welcoming visual hierarchy, and obvious actions to discover interests or explore careers.
2. **Onboarding:** lightweight, student-friendly setup with only the information needed to personalize the demo.
3. **Timed Interest Assessment:** multiple questions about preferred activities, curiosity, and work styles; visible timer/progress; result and explanation retained in session state.
4. **Career Explorer:** searchable/filterable career catalogue with several representative career clusters and clear career summaries.
5. **Recommendation engine:** ranks multiple plausible careers using transparent, understandable rules tied to assessment responses; explains why each option appeared.
6. **Career detail:** what the career involves, relevant interests/skills, possible learning steps, and a staged year-by-year example roadmap. Label unverified content as illustrative.
7. **Timed Math Readiness Assessment:** timed questions tagged by topic, a clear progress indicator, and a fair completion/results state.
8. **Learning analysis:** topic-level results, supportive strengths/practice areas, actionable practice checklist, and retest flow. Do not label a student incapable.
9. **Change My Path:** change the active career without erasing previous results or achievements.
10. **Dashboard and comparison:** summarize available assessment progress, current exploration, next actions, and compare up to three career options where data is available.
11. **Interest Discovery Lab:** simple activities and reflection prompts for students who are unsure of their interests.
12. **Career Assistant:** a transparent, rule-based demo helper that uses the approved local content and clearly states that responses are simulated/rule-based; no LLM service is required.
13. **Scholarship/affordability demo:** fictional sample cards only, with prominent demo labels; never imply real eligibility or live funding availability.
14. **Feedback and empty/error states:** useful messages for first-time users, missing results, incomplete assessments, and invalid or interrupted flows.

### MVP definition of done

A judge should be able to start at the landing page, complete onboarding and the interest assessment, review multiple explained career options, open a roadmap, take the timed math assessment, receive topic-level feedback and an improvement plan, and change the selected career without losing completed progress. The app should start with `streamlit run app.py`, use no secrets or API key, and not require a database or external AI service.

## 6. Approved technology and architecture

**Approved runtime stack (do not change without explicit user approval):**
- Python 3.11+ compatible with the chosen environment.
- Streamlit for the app, pages/navigation, widgets, forms, and session state.
- Pandas for structured data where useful.
- Plotly for interactive result/progress visualizations where useful.
- Custom CSS embedded through Streamlit for the visual system and lightweight transitions.
- Python standard library for timing, scoring, and utilities.
- pytest for pure-logic tests as a development/test dependency.

**Architecture direction:**
- A single Streamlit application with `app.py` as the entry point.
- `pages/` for feature pages when appropriate.
- `components/` for reusable UI pieces.
- `services/` for assessment scoring, recommendation logic, and other pure/domain logic.
- `data/` for clearly labelled fictional/demo career and assessment content.
- `tests/` for automated logic tests.
- Streamlit `st.session_state` for temporary session interactions.
- Keep domain/scoring logic testable separately from UI rendering wherever practical.

These are intended conventions; inspect the repository before assuming folders or files already exist. Do not create parallel or duplicate structures if the repository has since established a different agreed structure.

**Not approved for the MVP:** React, Next.js, Vite, TypeScript, Node.js, FastAPI/Flask/Django, a second web server, Tailwind/Bootstrap/shadcn, LangChain/LangGraph, vector databases, embeddings/RAG, database services, auth/analytics SDKs, paid APIs, or any package without a demonstrated need and explicit approval.

### Gemma 4 development workflow

Gemma 4 is the preferred coding assistant when available in the team's chosen environment. It may help with repository understanding, task planning, coding, review, debugging, and drafting tests. It is a **development-time assistant only**; the application does not require Gemma 4, a model download, Ollama, an API key, or an LLM SDK. Never claim to have used Gemma 4 if it was unavailable, and never assume an AI tool can access the repository or execute commands unless that capability is actually provided.

## 7. Data, scoring, and result expectations

- Keep the first version local and demo-friendly; no external service should be required for the core journey.
- Use fictional or representative sample data and visibly label it as such.
- Interest matching should be explainable: for example, show which response themes relate to a suggested career and what the student can explore next.
- Prefer several recommendations over a single definitive verdict.
- Make assessment timers and completion rules visible and consistent; handle unanswered questions and early exits intentionally.
- Math questions should have topic tags so results can be grouped by topic.
- Improvement plans should turn results into small, achievable practice actions.
- Changing paths should update the active path without deleting historical session progress.
- Use only fields that are needed for the demo; do not collect real student identifiers or sensitive information.
- Session state is temporary. Do not promise that it survives a new session, browser reset, or server restart.
- Any future real-world data should include trustworthy source URLs and a last-verified date. Until verified, keep the information explicitly illustrative.

## 8. Visual and interaction direction

Aim for a polished, modern, colourful, student-friendly product rather than a plain school form. Use a consistent design system, clear hierarchy, accessible contrast, readable typography, responsive layouts, friendly cards, visible progress, helpful empty states, and restrained transitions/hover feedback. Keep interactions understandable on a laptop and at narrow/mobile-like widths. Do not let animation or decoration obstruct assessment questions, timers, or accessibility. Avoid shame-oriented red error states for learning performance; use constructive language and explain the next action.

## 9. Team roles and ownership

There are three members. See `.ai/TEAM_WORKFLOW.md` and `.ai/roadmap/MEMBER_TASK_ASSIGNMENTS.md` for the authoritative task table and branch procedure.

- **Member 1 — UI/navigation/integration:** app shell, design system, onboarding, dashboard, Change My Path, feedback/empty states, integration, README and demo readiness.
- **Member 2 — interest/career engine:** interest assessment, career data/explorer, explainable recommendations, career detail/roadmaps, discovery activities, rule-based Career Assistant.
- **Member 3 — readiness/learning analytics:** timed math assessment, topic analysis, improvement/retest, fictional affordability demo, and test-suite coordination.

### Collaboration rules
- `main` is for stable, demo-ready work.
- Use `integration` for team integration; create it from `main` when implementation begins.
- Use focused feature branches and pull requests into `integration`; do not commit directly to shared branches.
- Member 1 completes TASK-002 and merges the app skeleton into `integration` before other members build app features.
- Agree shared contracts before parallel implementation: session-state keys, career/question schemas, scoring outputs, navigation conventions, and design tokens.
- One owner per file at a time. Coordinate shared-sensitive files and avoid simultaneous edits to `app.py`, shared contracts, requirements, and project-state logs.
- Do not begin dependent work before dependencies are merged.
- Each feature owner writes and runs tests for their logic. A pushed branch is not the same as integrated/complete work.

## 10. How any AI coding assistant should work on this repository

When given this file, the AI should understand the product; it should **not** immediately implement the entire application.

1. Inspect the current repository and Git branch before planning changes. Do not assume planned files already exist.
2. Read `.ai/AI_RULES.md`, `.ai/AI_MASTER_PROMPT.md`, `.ai/TECH_STACK.md`, `.ai/ARCHITECTURE.md`, `.ai/CURRENT_STATE.md`, `.ai/DECISIONS.md`, `.ai/TEAM_WORKFLOW.md`, `.ai/roadmap/MASTER_ROADMAP.md`, `.ai/roadmap/MEMBER_TASK_ASSIGNMENTS.md`, and the active task file when those files exist.
3. Identify the user's assigned member role and **one explicit task ID**. If the user has not authorized implementation or no task is specified, summarize understanding and ask which task to start; do not silently start building.
4. Check task dependencies and whether they are integrated. If a dependency or shared interface is missing, report the blocker and request agreement rather than inventing an incompatible contract.
5. State a short implementation plan, the exact files allowed to change, and how acceptance will be checked.
6. Implement only the assigned task and its owned files. Do not rewrite unrelated modules, architecture, stack, or product scope.
7. Add or update relevant tests. Run checks only when the environment supports them, and report the actual commands and outcomes. Never fabricate test results.
8. Review the diff for scope, privacy, inclusive language, demo-data labels, and dependency compliance.
9. Update `.ai/CURRENT_STATE.md`, `.ai/logs/PROGRESS.md`, and `.ai/logs/CHANGELOG.md` with verified facts only; coordinate edits to avoid conflicts.
10. Summarize changed files, tests/results, remaining limitations, and the next dependency-ready task. Stop at the task boundary.

If a request conflicts with this brief or a more specific approved project decision, explain the conflict and ask for clarification. Do not treat sample ideas in this document as permission to add unapproved technologies or features.

## 11. Current documented status

- Product scope, stack direction, AI workflow, team roles, and a 20-task roadmap are documented in `.ai/`.
- TASK-001 (project definition and control documentation) is recorded as done.
- TASK-002 (Streamlit skeleton and app shell) is the first runtime task and is assigned to Member 1.
- Runtime implementation is not claimed complete by this document. Verify the live repository and `.ai/CURRENT_STATE.md` before stating the current implementation status.
- No tests, launch checks, or feature behaviour should be described as passing unless someone has actually run and recorded them.

## 12. Source-of-truth documents

This file gives the complete high-level handoff. Detailed operational rules and task-level acceptance criteria live in these files:

- [AI master instructions](AI_MASTER_PROMPT.md)
- [AI rules](AI_RULES.md)
- [Approved tech stack](TECH_STACK.md)
- [Architecture](ARCHITECTURE.md)
- [Current state](CURRENT_STATE.md)
- [Decisions](DECISIONS.md)
- [Three-member workflow](TEAM_WORKFLOW.md)
- [Master roadmap: all task IDs and order](roadmap/MASTER_ROADMAP.md)
- [Member task assignments and dependencies](roadmap/MEMBER_TASK_ASSIGNMENTS.md)
- [Task files and template](tasks/)
- [Progress log](logs/PROGRESS.md)
- [Changelog](logs/CHANGELOG.md)

**Instruction for future contributors:** Treat this brief as the starting context, detailed project-control files as the execution rules, and the active task file as the scope of the work you are currently authorized to do.
