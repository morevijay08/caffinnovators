"""Temporary interface for routes awaiting their dedicated feature tasks."""
import streamlit as st


def coming_soon(title: str, task: str, description: str) -> None:
    st.title(title)
    st.info(f"This section is planned for {task} and is not implemented yet.")
    st.write(description)
    st.caption(
        "This prototype uses temporary Streamlit session state only. "
        "It does not create a persistent student profile."
    )
