# frontend/utils/profile.py
import streamlit as st
import json

def save_profile():
    try:
        data = {
            "income_salary": st.session_state.income_salary,
            "income_digital_assets": st.session_state.income_digital_assets,
            "income_rental": st.session_state.income_rental,
            "basic_deduction_80c": st.session_state.basic_deduction_80c,
            "medical_insurance_80d": st.session_state.medical_insurance_80d,
            "home_loan_interest": st.session_state.home_loan_interest,
            "donations_80g": st.session_state.donations_80g,
            "nps_80ccd": st.session_state.nps_80ccd,
            "other_deductions": st.session_state.other_deductions,
            "preferred_regime": st.session_state.preferred_regime,
            "financial_year": st.session_state.financial_year
        }
        json_data = json.dumps(data, indent=4)
        st.sidebar.download_button(
            label="Download Profile",
            data=json_data,
            file_name="tax_profile.json",
            mime="application/json"
        )
        st.sidebar.success("Profile ready for download!")
    except Exception as e:
        st.sidebar.error(f"Failed to save profile: {str(e)}")

def load_profile():
    try:
        uploaded_file = st.sidebar.file_uploader("Upload profile", type="json")
        if uploaded_file is not None:
            data = json.load(uploaded_file)
            st.session_state.income_salary = data.get("income_salary", 0)
            st.session_state.income_digital_assets = data.get("income_digital_assets", 0)
            st.session_state.income_rental = data.get("income_rental", 0)
            st.session_state.basic_deduction_80c = data.get("basic_deduction_80c", 0)
            st.session_state.medical_insurance_80d = data.get("medical_insurance_80d", 0)
            st.session_state.home_loan_interest = data.get("home_loan_interest", 0)
            st.session_state.donations_80g = data.get("donations_80g", 0)
            st.session_state.nps_80ccd = data.get("nps_80ccd", 0)
            st.session_state.other_deductions = data.get("other_deductions", 0)
            st.session_state.preferred_regime = data.get("preferred_regime", "New Regime")
            st.session_state.financial_year = data.get("financial_year", "2025-26")
            st.sidebar.success("Profile loaded successfully!")
            st.experimental_rerun()
    except Exception as e:
        st.sidebar.error(f"Failed to load profile: {str(e)}")
