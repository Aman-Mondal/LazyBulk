import streamlit as st
from services.auth.login import render_login
from services.state.defaultSession import initial_session_default
 
def main():
    st.set_page_config(
        page_icon="O",
        page_title="LazyBulk",
        initial_sidebar_state="expanded",
        layout="centered"
    )

    if not render_login():
        return

    initial_session_default()

    st.write("Hello")

if __name__ == "__main__":
    main()
