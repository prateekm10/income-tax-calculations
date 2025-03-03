# frontend/utils/session_state.py
import streamlit as st

def init_session_state():
    default_values = {
        "income_salary": 0.0,
        "income_digital_assets": 0.0,
        "income_rental": 0.0,
        "basic_deduction_80c": 0.0,
        "medical_insurance_80d": 0.0,
        "home_loan_interest": 0.0,
        "donations_80g": 0.0,
        "nps_80ccd": 0.0,
        "other_deductions": 0.0,
        "preferred_regime": "New Regime",
        "financial_year": "2025-26",
        "calculation_done": False,
        "new_regime_result": None,
        "old_regime_result": None
    }
    for key, value in default_values.items():
        if key not in st.session_state:
            st.session_state[key] = value

def reset_session_state():
    keys_to_reset = [
        "income_salary", "income_digital_assets", "income_rental",
        "basic_deduction_80c", "medical_insurance_80d", "home_loan_interest",
        "donations_80g", "nps_80ccd", "other_deductions",
        "preferred_regime", "calculation_done",
        "new_regime_result", "old_regime_result"
    ]
    for key in keys_to_reset:
        if key in st.session_state:
            if key in ["preferred_regime", "financial_year"]:
                st.session_state[key] = "New Regime" if key == "preferred_regime" else "2025-26"
            elif key == "calculation_done":
                st.session_state[key] = False
            else:
                st.session_state[key] = 0.0
