# APPROVED TECH STACK — LIFEPath INDIA

Status: APPROVED FOR HACKATHON MVP. Do not change without explicit user approval.

## Runtime
- Python 3.11 or later compatible with the installed environment
- Streamlit: application, navigation, forms, widgets and session state
- Pandas: structured career and assessment data where useful
- Plotly: interactive result/progress visualizations
- Custom CSS embedded through Streamlit: visual system, hover states and lightweight animations
- Python standard library: timing, scoring and utilities

## Development AI assistant
- Preferred coding assistant: Gemma 4, when available through the team's chosen editor or model interface.
- Use Gemma 4 for repository understanding, task planning, implementation assistance, code review, debugging, and test drafting.
- This is a developer workflow preference, not an application dependency. No Gemma runtime, model download, hosted inference, API key, Ollama service, or LLM SDK is required by the MVP.
- Do not assume the model can access GitHub, local files, terminals, or execute tests unless the chosen tool explicitly provides those capabilities.

## Testing
- pytest for pure-logic tests (development dependency)
- Git/GitHub for version control

## Explicitly not approved for MVP
- React, Next.js, Vite, TypeScript or Node.js
- FastAPI, Flask, Django or a second web server
- Tailwind, Bootstrap, shadcn/ui or another UI framework
- LangChain, LangGraph, vector DB, embeddings or RAG
- OpenAI/Gemini/Claude API or any hosted/local LLM as a student-facing runtime requirement
- PostgreSQL, MongoDB, Supabase, Firebase or Redis
- Auth/analytics SDKs, paid APIs or required external services
- Any package added without demonstrated need and explicit approval

## Dependency policy
Keep requirements limited to Streamlit, Pandas and Plotly; include pytest only as a development/test dependency if appropriate. Verify environment compatibility before pinning versions. No added animation/icon packages.

## Data and state
- Fictional demo content: data/
- Runtime interactions: st.session_state
- No database or durable personal profile storage in the MVP.
- Do not claim session state survives a new session or server restart.

## Future integrations
A student-facing AI assistant, verified career data imports, official scholarships, persistence, authentication, and production deployment require separate decisions; do not add by default.
