# frontend/ui/analytics.py
import streamlit as st

def setup_analytics_tab():
    if not st.session_state.get("calculation_done", False):
        st.info("Please calculate your tax first on the 'Tax Calculator' tab.")
        return
    
    st.subheader("Tax Analytics")
    st.write("Placeholder: Additional charts and data analysis will be shown here.")
