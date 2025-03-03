# frontend/ui/planning.py
import streamlit as st

def setup_planning_tab():
    if not st.session_state.get("calculation_done", False):
        st.info("Please calculate your tax first on the 'Tax Calculator' tab.")
        return
    
    st.subheader("Tax Planning Recommendations")
    st.write("Placeholder: Tax planning advice will appear here after further logic integration.")
