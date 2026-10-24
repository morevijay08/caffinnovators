# API CONTRACTS — LIFEPath INDIA

Status: Initial contract baseline approved for implementation planning. Endpoint definitions below are planned contracts, not proof that routes already exist. Update this file in a dedicated, coordinated change whenever the API changes.

## 1. Conventions

- Local development: frontend and backend run as separate processes.
- Backend base path: `/api/v1`.
- Health check: `GET /health` (outside the versioned feature prefix so tooling can check service health).
- Requests and responses use JSON with UTF-8.
- Use Pydantic models for Python request/response validation and matching TypeScript types in `frontend/src/types/`.
- Frontend components call the shared client under `frontend/src/api/`; do not scatter raw `fetch()` calls or hardcoded base URLs throughout components.
- Configure the API base URL through one frontend environment setting (for Vite, a `VITE_API_BASE_URL` variable). Provide a safe local default only if the team agrees it is useful.
- Backend local CORS should allow only the configured local frontend origin, not all origins with credentials.
- No authentication, database, external APIs, API keys, or persistent student profiles in the MVP.
- All content that is not verified real-world information must be marked illustrative/demo.
- Use consistent HTTP status codes and an error response with a human-readable detail. Do not leak stack traces or secrets.

## 2. Health contract — required for TASK-002

### Request
`GET /health`

### Success response — HTTP 200
```json
{
  "status": "ok",
  "service": "lifepath-api"
}
```

### Frontend behaviour
The minimal React shell should be able to call the health endpoint using the shared API client and show a small connected/unavailable status or equivalent developer-friendly indication. Do not block the entire UI indefinitely if the backend is unavailable.

## 3. Shared data shapes

These are initial planning shapes. Refine them with the owning member before implementing each feature; keep Python and TypeScript representations aligned.

### Career summary
```json
{
  "id": "career-example",
  "title": "Example Career",
  "cluster": "technology",
  "summary": "Illustrative description of the work.",
  "interest_tags": ["problem-solving", "building"],
  "skill_tags": ["logical-thinking", "communication"],
  "illustrative": true
}
```

### Interest assessment submission/result
- Submission contains selected answers using stable question IDs and option IDs; do not trust client-submitted scores.
- The backend computes deterministic scoring and returns multiple matches with explanations.
- A planned result should include an assessment/result ID suitable for temporary client-side reference, completion timestamp if available, and a list of interest signals/recommendations.
- Do not collect sensitive student data.

### Recommendation item
A recommendation should include a career ID, a numeric match score or rank (document the scale), a short explanation of matching signals, and suggested exploration steps. The score is heuristic, not a scientific probability or guarantee.

### Math assessment result
- Questions have stable IDs, topic tags and answer options.
- The client may manage the visible timer, but the server must calculate the result from question IDs and submitted answers; the team must decide the exact timeout/anti-tampering behaviour during the task.
- Results should include overall summary and topic-level correct/total counts, with supportive next-step recommendations.
- A result is not a diagnosis or a measure of fixed ability.

### API error
Use a consistent JSON error shape. Initial proposal:
```json
{
  "detail": "A user-safe explanation of what went wrong."
}
```
FastAPI's standard `detail` shape is acceptable unless the team approves a shared structured error schema later.

## 4. Planned endpoint inventory

The endpoints below are a roadmap, not a claim they exist yet. Keep routes thin and call domain services.

| Method | Path | Owner | Purpose |
|---|---|---|---|
| GET | `/health` | Member 1 coordinates | API health; implemented in TASK-002 |
| GET | `/api/v1/careers` | Member 2 | List/filter illustrative career summaries |
| GET | `/api/v1/careers/{career_id}` | Member 2 | Career detail and illustrative roadmap |
| GET | `/api/v1/interest-assessment` | Member 2 | Return interest questions/options without answer keys |
| POST | `/api/v1/interest-assessment/submit` | Member 2 | Score answers and return explanations/recommendations |
| GET | `/api/v1/math-assessment` | Member 3 | Return question IDs, prompts, options and topic tags without answer keys |
| POST | `/api/v1/math-assessment/submit` | Member 3 | Score submitted answers and return topic-level analysis |
| GET | `/api/v1/discovery-activities` | Member 2 | List Interest Discovery Lab activities |
| POST | `/api/v1/career-assistant` | Member 2 | Rule-based, clearly labelled demo response |
| GET | `/api/v1/affordability-examples` | Member 3 | Fictional affordability/scholarship examples clearly labelled as demo |

Do not add all endpoints in TASK-002. Implement only the health endpoint and the minimal scaffold; later endpoints belong to their assigned tasks.

## 5. API ownership and change process

- Member 2 owns career/interest schemas, scoring and career endpoints.
- Member 3 owns math/readiness schemas, scoring and readiness endpoints.
- Member 1 owns the frontend API client, TypeScript types and cross-stack integration.
- The owner proposes a contract change first; affected members agree before updating Pydantic models, TypeScript types and consumers.
- Contract changes should be documented in a focused PR. Do not silently change field names or response shapes.
- Add tests for request validation, successful responses, empty data and safe error cases where relevant.
