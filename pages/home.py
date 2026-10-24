"""Entry-page placeholder until TASK-003 landing page."""
import streamlit as st

st.title("🧭 LifePath India")
st.subheader("Every Interest Has a Future")
st.write(
    "Explore interests, learn about different careers, and build skills at your own pace."
)
st.info("TASK-002: This is the working application shell. Student journeys will be added in later tasks.")
st.page_link("pages/onboarding.py", label="Get started", icon="✨")
st.page_link("pages/careers.py", label="Browse career section", icon="🧩")
st.caption("No marks-based career verdicts. Changing your mind is part of learning.")
