# CODING STANDARDS

## Python
- Use descriptive names and type hints for reusable domain functions.
- Keep modules focused, avoid circular imports, and separate UI from business logic.
- Make scoring/matching deterministic and testable.
- Validate inputs and handle missing answers gracefully.
- Avoid broad exception handling without a clear recovery path.

## Streamlit
- Call `st.set_page_config` before other Streamlit UI commands.
- Use unique, stable widget keys.
- Initialize session state safely and respect rerun behaviour.
- Use forms where inputs should submit together.
- Avoid fragile selectors coupled to Streamlit's internal DOM.
- Keep custom CSS scoped and maintainable.
- Do not claim permanent persistence for session state.

## Data
- Keep careers, activities and question sets readable in `data/`.
- Label illustrative values and demo content.
- Future verified facts should include source URL, last-verified date and supported claim.
- Use consistent identifiers for clusters and skills.

## Tests
Test recommendation scoring, topic analysis, plan generation and path changes. Include empty input, ties, zero/full score, duplicates and timer-expiry behaviour. Do not treat quiz results as proof of career suitability.

## UI/UX
Use approved palette; give every button a meaningful action; use supportive non-shaming language; maintain contrast, accessible labels, focus states and reduced-motion support.
