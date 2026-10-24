"""LifePath India — Streamlit application entry point (TASK-002)."""
import streamlit as st

from components.state import initialize_session_state
#Tile page initialize
st.set_page_config(
    page_title="LifePath India",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)
initialize_session_state()

st.sidebar.title("🧭 LifePath India")
st.sidebar.caption("Every Interest Has a Future")
st.sidebar.info("Prototype: the experience is being built step by step.")
navigation = st.navigation(
    {
        "Start here": [
            st.Page("pages/home.py", title="Home", icon="🏠", default=True),
            st.Page("pages/onboarding.py", title="Get started", icon="✨"),
        ],
        "Explore": [
            st.Page("pages/discovery.py", title="Discover interests", icon="🔎"),
            st.Page("pages/careers.py", title="Explore careers", icon="🧩"),
            st.Page("pages/roadmap.py", title="My roadmap", icon="🗺️"),
        ],
        "My journey": [
            st.Page("pages/readiness.py", title="Practice skills", icon="🧠"),
            st.Page("pages/dashboard.py", title="Dashboard", icon="📊"),
            st.Page("pages/change_path.py", title="Change my path", icon="🔁"),
        ],
    }
)
navigation.run()
