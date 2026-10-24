# TASK-014 — Gemma 4 Career Assistant (Runtime)

Status: NOT STARTED. This specification is not evidence that the chatbot exists.

## Owner and collaborators
- **Member 2 — backend owner:** prompt, FastAPI route, Gemma adapter, schemas and backend tests.
- **Member 1 — frontend owner:** React chat interface, typed API client, loading/error states and integration.
- **Member 3 — test coordinator:** unavailable-model, timeout, malformed-output and regression tests.

## Goal
Provide a student-friendly career exploration chatbot that uses **Gemma 4 at runtime**. It must not be a hard-coded or rule-based response falsely presented as model-generated.

## Dependencies
- TASK-002 runnable React + TypeScript/Vite and FastAPI skeleton.
- Agreed API conventions from `.ai/API_CONTRACTS.md`.
- Career catalogue/recommendation/roadmap contracts from TASK-006/007/008.
- Ollama installed and a Gemma 4 model available on the implementation machine, or a separately approved hosted Gemma inference configuration.

## Runtime architecture
React chat UI → shared typed API client → `POST /api/v1/career-assistant` → FastAPI route/schema → Gemma service/adapter → local Ollama → configured Gemma 4 model → bounded, user-safe response.

Default configuration:
- `OLLAMA_BASE_URL=http://localhost:11434`
- `GEMMA_MODEL=gemma4:e2b`

Treat these as configurable initial defaults. Confirm the exact installed Ollama model tag and actual hardware/runtime before final demo. Keep model inference on the backend. Do not put Ollama URLs, provider credentials or model keys into browser-exposed `VITE_*` variables.

## Functional requirements
1. Accept a trimmed user message with a documented maximum length (target 1–2000 characters).
2. Optionally accept a small, bounded recent conversation history containing only user/assistant messages. The client cannot supply or override the system prompt.
3. Call the configured Gemma 4 model through the backend adapter.
4. Return an answer, configured model identifier and a short AI-guidance disclaimer, matching the API contract.
5. Keep latency bounded with a timeout and return a useful, non-sensitive error when the runtime is unavailable, times out, or returns an invalid/empty response.
6. Do not silently fall back to canned text while claiming it came from Gemma 4.
7. Do not use the LLM to calculate interest scores, math results, career match scores or eligibility.
8. Encourage exploration and multiple possibilities; never describe a student's future as fixed or shame students for marks.
9. Do not invent official admissions rules, live scholarships, exact fees, salary guarantees or job guarantees. Direct users to verified sources only when the application actually has them.
10. Avoid collecting names, addresses, school names, marks or other sensitive personal information. Do not log full chat contents by default.

## Hosted provider fallback
Local Ollama is the default. If local inference is impractical, the team may explicitly choose a hosted Gemma provider after checking availability, cost/quota, privacy and connectivity. Keep secrets only in an untracked backend environment file. Document setup requirements without committing keys. Do not silently swap to another model.

## Acceptance criteria
- [ ] API contract and Pydantic/TypeScript types match.
- [ ] A request reaches an actual Gemma 4 model and returns its generated response.
- [ ] Frontend communicates only with FastAPI, never directly with Ollama/provider.
- [ ] Loading, unavailable-model, timeout and error UI states are handled.
- [ ] Backend tests cover success, validation, unavailable runtime, timeout and malformed/empty output using a mocked adapter; a separate manual smoke test confirms real Gemma 4 inference.
- [ ] Model/configuration can be changed without editing source code.
- [ ] No credentials or private student data are committed or unnecessarily logged.
- [ ] Documentation and logs reflect only checks actually run.

## Scope exclusions
No RAG, embeddings, vector database, external web search, agent tools, fine-tuning, persistent chat storage or LLM-based scoring for the hackathon MVP unless separately approved.

## Required handoff
Update `.ai/CURRENT_STATE.md`, `.ai/logs/PROGRESS.md` and `.ai/logs/CHANGELOG.md` with truthful implementation/test results when this task is completed.
