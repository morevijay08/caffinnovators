# THREE-MEMBER TEAM WORKFLOW — LIFEPath INDIA

## Purpose
Let three members build independent features in parallel while reducing merge conflicts. This document governs branch use, ownership, interfaces, reviews and integration.

## Roles at a glance
- **Member 1 — UI and integration:** application shell, shared design system, navigation, onboarding, dashboard, path switching, feedback, final integration and demo readiness.
- **Member 2 — Interest and career engine:** interest assessment logic, career catalogue, recommendations, career details/roadmaps, discovery activities and rule-based career guidance.
- **Member 3 — Readiness and learning analytics:** timed math assessment, topic analysis, improvement/retest, fictional affordability demo, test coordination and scoring/analytics verification.

See `.ai/roadmap/MEMBER_TASK_ASSIGNMENTS.md` for task IDs, dependencies and ownership.

## Before parallel coding
1. Member 1 completes TASK-002 (the minimal Streamlit skeleton) and merges it into `integration`.
2. Agree and document the shared interface contracts before feature branches are created:
   - session-state keys and their default values;
   - career and question data schemas;
   - recommendation function input/output;
   - assessment scoring and result schema;
   - navigation/page entry conventions;
   - shared design tokens.
3. Each member reads the AI instructions and only their task file(s).
4. If a dependency is not merged or a contract is unclear, do not guess. Ask the team to agree first.

## Branch model
- `main`: stable demo-ready code only.
- `integration`: shared integration branch; create it from `main` when the team starts implementation.
- `member-1-ui`, `member-2-careers`, `member-3-assessments`: optional personal branches for each member's ongoing work.
- Use short-lived feature branches from the latest `integration`, e.g. `feature/TASK-007-career-recommendations`.
- Never commit directly to `main` or `integration`.
- Open a pull request from a feature branch to `integration`. After merge, sync the member branch and create a fresh feature branch for the next task.
- Promote `integration` to `main` only after the app starts and the end-to-end smoke test passes.

## File ownership
- Member 1 owns `app.py`, `pages/`, `components/`, shared CSS/design tokens, navigation and shared session-state integration.
- Member 2 owns career and interest modules under `services/` and career data under `data/`, except files explicitly assigned to another member.
- Member 3 owns readiness/performance modules under `services/`, assessment question data under `data/`, and test coordination.
- Test files follow the feature owner: Member 2 owns career/interest logic tests; Member 3 owns readiness/performance tests. Each owner adds tests alongside their feature.
- `requirements.txt`, shared contracts, `app.py` integration points, `.ai/CURRENT_STATE.md`, `.ai/logs/PROGRESS.md`, and `.ai/logs/CHANGELOG.md` are shared-sensitive files. Coordinate edits; only one person edits each shared file at a time.
- Do not create duplicate versions of a shared module or rename another member's file without agreement.

## Gemma 4 coding workflow
At the beginning of each coding session, use Gemma 4 when available and provide:
1. Required `.ai/` instruction files.
2. Member number/role and assigned task ID.
3. Task dependencies and acceptance criteria.
4. Explicit allowed file paths.
5. The relevant shared interface contract.
6. The instruction to inspect first and propose a plan before editing.

Prompt Gemma 4 to avoid touching files owned by other members, to show a diff summary, and to run only relevant tests. Review all changes before committing. If Gemma 4 is unavailable, disclose it; do not mislabel another model. The app itself must not require Gemma 4 unless a separate product-integration task is approved.

## Standard feature workflow
1. Sync from latest `integration`.
2. Create one task branch.
3. Inspect files and write a short plan.
4. Implement only the assigned task and owned paths.
5. Run relevant tests and the available app check.
6. Review `git diff` and `git status`; stage explicit paths.
7. Push branch and open a pull request into `integration`.
8. PR description must include task ID, scope, files changed, tests run/results, screenshots for UI changes, and known limitations.
9. Another teammate reviews the change; owner addresses feedback.
10. Merge only when dependencies, tests and interface contract are satisfied.

## Conflict prevention and resolution
- One owner per file per task. Do not have two branches edit the same file in parallel.
- Keep pull requests small and focused.
- Avoid broad formatting changes and unrelated refactors.
- Never force-push shared branches or blindly choose "ours"/"theirs".
- If a conflict happens, both affected owners agree on intended behaviour; one designated resolver applies the combined change, runs tests, and documents the resolution.
- If a shared contract must change, notify all members first and update its documentation in a dedicated PR.

## Shared-file coordination
The team should nominate Member 1 as the integration coordinator. For a shared-file change, Member 1 opens a small coordination task and announces the owner before edits start. Only one member edits the shared file at a time. Every member updates the state/progress log for their own completed task, but log edits must be coordinated to avoid simultaneous changes.

## Definition of ready to merge
- Task acceptance criteria are met.
- Relevant tests ran; exact results are stated.
- No secrets, local environments, cache files or unrelated changes are committed.
- No unapproved dependency or architecture change was introduced.
- The feature respects the agreed interfaces and has useful empty/error states.
- UI changes are checked at a practical desktop and narrow width where possible.

## Definition of integrated
A task is integrated only after its PR is merged to `integration` and the combined app is checked. A branch push alone does not mean the feature is integrated or complete.
