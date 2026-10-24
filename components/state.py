"""Stable initial session state for the navigation skeleton.

Future tasks may extend this schema only after agreement with feature owners.
Values are transient: Streamlit session state is not durable storage.
"""
import streamlit as st

DEFAULT_STATE = {
    "student_profile": {},
    "onboarding_completed": False,
    "interest_answers": {},
    "assessment_results": {},
    "saved_career_ids": [],
    "selected_career_id": None,
    "roadmap_progress": {},
    "completed_topics": [],
}


def initialize_session_state() -> None:
    """Add missing state keys without overwriting the current session."""
    for key, default in DEFAULT_STATE.items():
        if key not in st.session_state:
            st.session_state[key] = default.copy() if isinstance(default, (dict, list)) else default
