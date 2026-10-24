# CHANGELOG — LIFEPath INDIA

## 2026-10-24 — Project control baseline
- Added LifePath-specific agent instructions, project context, architecture, coding standards, stack lock, decisions, current state and known issues.
- Added ordered roadmap, phased notes, task template and task definitions.
- Preserved the existing LICENSE.
- Re-inspected the GitHub tree and key control files.
- No runtime implementation was included in this documentation-only milestone.

## 2026-10-24 — Gemma 4 and team collaboration plan
- Updated AI_MASTER_PROMPT.md and AI_RULES.md to prefer Gemma 4 for development assistance when available.
- Updated TECH_STACK.md to state that Gemma 4 is not a student-facing runtime dependency.
- Added TEAM_WORKFLOW.md with branch strategy, ownership boundaries, PR checks and conflict-resolution rules.
- Added MEMBER_TASK_ASSIGNMENTS.md mapping all roadmap tasks to the three member roles and identifying dependencies.
- Updated MASTER_ROADMAP.md and CURRENT_STATE.md for dependency-aware parallel delivery.
- No application/runtime code, Gemma API integration, package installation or app tests were added.

## 2026-10-24 — Approved switch to React + TypeScript and FastAPI
- Recorded explicit user approval for React + TypeScript + Vite frontend and Python FastAPI backend in ADR-007; marked the previous Streamlit-only ADR-002 as superseded.
- Updated TECH_STACK.md, ARCHITECTURE.md, PROJECT_CONTEXT.md, AI_MASTER_PROMPT.md, AI_RULES.md, CURRENT_STATE.md, TEAM_WORKFLOW.md, MASTER_ROADMAP.md, MEMBER_TASK_ASSIGNMENTS.md and TASK_002.md.
- Added API_CONTRACTS.md to define the initial health endpoint, API conventions, planned endpoint inventory, shared data shapes and contract ownership.
- Kept the MVP database-free and independent of paid APIs, secrets and runtime LLM services.
- Documentation-only update: no runtime code was created, installed, launched or tested.
