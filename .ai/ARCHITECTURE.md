# ARCHITECTURE — LIFEPath INDIA

## Principle
One modular Python Streamlit application backed by static fictional data. No separate frontend/backend services.

## Flow
Streamlit interaction → page/view → pure domain service (assessment, matching, roadmap, learning plan) → static demo data/session state → Streamlit components/Plotly.

## Structure
- `app.py`: entry point, page config, shared CSS and navigation.
- `pages/`: onboarding, discovery, career explorer, roadmap, readiness, improvement and path change views.
- `components/`: reusable cards, progress indicators, explanation panels and navigation helpers.
- `services/`: deterministic assessment scoring, matching, readiness analysis and plan generation.
- `data/`: fictional catalogue, activities, quiz questions and demo scholarship cards.
- `assets/`: local visual assets only when necessary.
- `tests/`: automated tests for non-UI logic.
- `.ai/`: agent contract, decisions, tasks, roadmap and logs.

## State
Use `st.session_state` for onboarding answers, assessment results, saved careers, selected goal, plan and completed topics. Initialize safely; don't reset progress on routine reruns. Calculations belong in pure Python functions. Do not imply session data is durable.

## UI
Palette: navy #14213D, teal #20C997, amber #FFBF69, background #F7F9FC, white cards, primary text #182230, secondary #64748B. Use clear hierarchy, spacing, focus states, reduced-motion support and responsive layouts. Do not require remote fonts/images/CDNs.

## Trust boundary
Rule-based recommendations are heuristic and must explain the matching signals. Short diagnostics provide initial indications, not definitive ability measures. Fees and route details are illustrative unless verified.
