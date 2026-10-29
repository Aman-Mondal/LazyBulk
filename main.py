import streamlit as st
from services.auth.login import render_login
from services.state.defaultSession import initial_session_default
from services.config.workout_config import EXERCISES

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
    workout_started = st.session_state.get("workout_started", False)
    with st.sidebar:
        st.title("LazyBulk")

        if st.session_state.username:
            st.caption(f"Login as {st.session_state.username}")

        st.divider()
        st.subheader("Workout Plan")

        if not workout_started:
            st.selectbox("Exercise", options=EXERCISES, key="plan_exercise")
            st.number_input("Sets", min_value=0, max_value=50, key="plan_sets", step=1)
            st.number_input("Reps per set", min_value=0, max_value=100, key="plan_reps", step=1)
            st.markdown("")
            start_session_button = st.button("Start Session", width="stretch", key="start_session_button")

            if start_session_button:
                st.session_state["workout_started"] = True
                st.rerun()
        else:
            st.write("Workout Started")        

if __name__ == "__main__":
    main()
