
import streamlit as st
from ui.input_form import setup_input_form
from ui.results import setup_results_area
from ui.planning import setup_planning_tab
from ui.analytics import setup_analytics_tab
from utils.session_state import init_session_state, reset_session_state
from utils.profile import save_profile, load_profile


# Page Configuration
st.set_page_config(
    page_title="Indian Income Tax Calculator FY 2025-26",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    st.title("Indian Income Tax Calculator FY 2025-26")

    # Sidebar Operations
    with st.sidebar:
        st.header("File Operations")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Save Profile", use_container_width=True):
                save_profile()
        with col2:
            if st.button("Load Profile", use_container_width=True):
                load_profile()
        st.divider()
        st.header("Help")
        # ... Help buttons and Reset Form ...
        if st.button("Reset Form", use_container_width=True):
            reset_session_state()
            st.experimental_rerun()

    # Initialize session state
    init_session_state()

    # Check if any help screen is toggled here (optional logic)

    # Create Tabs for the UI
    tab1, tab2, tab3, tab4 = st.tabs(["Tax Calculator", "Detailed Tax Regime Comparison", "Tax Planning", "Analytics"])

    with tab1:
        setup_input_form()
    with tab2:
        setup_results_area()
    with tab3:
        setup_planning_tab()
    with tab4:
        setup_analytics_tab()

if __name__ == "__main__":
    main()
