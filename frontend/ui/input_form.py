import streamlit as st

from logic.tax_calculations import calculate_new_regime_2025, calculate_old_regime_2025

def setup_input_form():
    """
    Displays the Income Tax input form with top-level user info (Assessment Year,
    Tax Payer, etc.) and regime-specific fields for both Old and New Regimes.
    """
    # -------------------------------
    # A. TOP-LEVEL INFO (as per official site)
    # -------------------------------
    st.subheader("Basic Information")

    col_top1, col_top2, col_top3, col_top4 = st.columns(4)
    with col_top1:
        st.selectbox(
            "Assessment Year",
            options=["2025-26"],  # Add more if needed
            key="assessment_year"
        )
    with col_top2:
        st.selectbox(
            "Tax Payer",
            options=[
                "Individual", "HUF", "AOP/BOI", "Company", "Firm",
                "LLP", "Local Authority", "Co-op Society", "Trust"
            ],
            index=0,
            key="tax_payer_type"
        )
    with col_top3:
        st.selectbox(
            "Category (Age)",
            options=[
                "Less than 60",
                "Senior Citizen (60-79)",
                "Super Senior Citizen (80+)"
            ],
            index=0,
            key="age_category"
        )
    with col_top4:
        st.selectbox(
            "Residential Status",
            options=["Resident", "Non-Resident", "Resident but Not Ordinarily Resident"],
            index=0,
            key="residential_status"
        )

    # -------------------------------
    # B. FINANCIAL YEAR & REGIME SELECTION
    # -------------------------------
    st.subheader("Select Financial Year and Preferred Regime")
    col_year, col_regime = st.columns(2)
    with col_year:
        st.selectbox(
            "Financial Year",
            options=["2025-26"],  # You can add more years if needed
            key="financial_year"
        )
    with col_regime:
        st.radio(
            "Preferred Tax Regime",
            options=["New Regime", "Old Regime"],
            horizontal=True,
            key="preferred_regime"
        )

    # -------------------------------
    # C. COMMON INCOME FIELDS
    # -------------------------------
    st.subheader("Income Details")
    colA, colB = st.columns(2)
    with colA:
        st.number_input(
            "Income from Salary/Pension (₹)",
            min_value=0.0,
            key="income_salary",
            help="Include your basic salary, HRA, allowances, and pension."
        )
        st.number_input(
            "Income from House Property (₹)",
            min_value=0.0,
            key="income_rental",
            help="Rental income less standard deduction of 30%, or net income from house property."
        )
    with colB:
        st.number_input(
            "Income from Digital Assets (30% tax) (₹)",
            min_value=0.0,
            key="income_digital_assets",
            help="Cryptocurrency, NFTs, and other digital assets (taxed at 30%)."
        )

    # -------------------------------
    # D. REGIME-SPECIFIC FIELDS
    # -------------------------------
    if st.session_state["preferred_regime"] == "Old Regime":
        # --- Old Regime Fields ---
        st.subheader("Deductions & Exemptions (Old Regime Only)")
        colC, colD = st.columns(2)
        with colC:
            st.number_input(
                "Basic Deductions - 80C (max ₹1.5L) (₹)",
                min_value=0.0,
                max_value=150000.0,
                key="basic_deduction_80c",
                help="PPF, ELSS, LIC, EPF, etc. (Limit: ₹1,50,000)"
            )
            st.number_input(
                "Interest on Housing Loan (max ₹2L) (₹)",
                min_value=0.0,
                max_value=200000.0,
                key="home_loan_interest",
                help="Interest on housing loan for self-occupied property (Limit: ₹2,00,000)."
            )
            st.number_input(
                "NPS Contribution - 80CCD(1B) (max ₹50K) (₹)",
                min_value=0.0,
                max_value=50000.0,
                key="nps_80ccd",
                help="Additional deduction for NPS contribution (Limit: ₹50,000)."
            )
            st.number_input(
            "Education Loan Interest - 80E (₹)",
            min_value=0.0,
            key="ded_80e",
            help="Interest paid on education loans for higher studies (deduction available for up to 8 years)."
        )
        with colD:
            st.number_input(
                "Medical Insurance - 80D (max ₹25K/50K) (₹)",
                min_value=0.0,
                max_value=50000.0,
                key="medical_insurance_80d",
                help="Health insurance premiums for self and family."
            )
            st.number_input(
                "Donations to Charity - 80G (₹)",
                min_value=0.0,
                key="donations_80g",
                help="Donations to approved funds and charitable institutions."
            )
           #Deduction for Disability - Section 80U
            st.number_input(
            "Deduction for Disability - 80U (₹)",
            min_value=0.0,
            key="ded_80u",
            help="Deduction for disabled individuals. Maximum limit: ₹75,000 (40-80% disability) or ₹1,25,000 (80%+ disability)."
            )
            #Home Loan Interest (First Time) - Section 80EE
            st.number_input(
            "Home Loan Interest (First Time) - 80EE (₹)",
            min_value=0.0,
            key="ded_80ee",
            help="Additional deduction for home loan interest for first-time buyers."
            )
        st.info("Under Old Regime, you can claim multiple deductions but face higher slab rates beyond ₹5 lakh.")
    
    else:
        # --- New Regime Fields ---
        st.subheader("Additional Fields (New Regime)")
        st.write("""
        Under the New Regime (FY 2025-26), you generally **cannot** claim 
        most of the deductions like 80C, 80D, 80G, etc. However, a standard deduction 
        of ₹50,000 is available if you have salary income. 
        """)
        st.number_input(
            "Income other than Salary and Special Rate Income (₹)",
            min_value=0.0,
            key="other_income_new_regime",
            help="Additional taxable income not from salary or digital assets."
        )
        st.info("No other major deductions apply under the New Regime, except the standard deduction on salary.")
    
   # =========================================
# input_form.py
# =========================================
import streamlit as st
from logic.tax_calculations import calculate_new_regime_2025, calculate_old_regime_2025

def setup_input_form():
    """
    Displays the Income Tax input form with top-level user info (Assessment Year,
    Tax Payer, etc.) and regime-specific fields for both Old and New Regimes.
    """
    # -------------------------------
    # A. TOP-LEVEL INFO
    # -------------------------------
    st.subheader("Basic Information")

    col_top1, col_top2, col_top3, col_top4 = st.columns(4)
    with col_top1:
        st.selectbox(
            "Assessment Year",
            options=["2025-26"],
            key="assessment_year"
        )
    with col_top2:
        st.selectbox(
            "Tax Payer",
            options=["Individual","HUF","AOP/BOI","Company","Firm","LLP","Local Authority","Co-op Society","Trust"],
            index=0,
            key="tax_payer_type"
        )
    with col_top3:
        st.selectbox(
            "Category (Age)",
            options=["Less than 60","Senior Citizen (60-79)","Super Senior Citizen (80+)"],
            index=0,
            key="age_category"
        )
    with col_top4:
        st.selectbox(
            "Residential Status",
            options=["Resident","Non-Resident","Resident but Not Ordinarily Resident"],
            index=0,
            key="residential_status"
        )

    # -------------------------------
    # B. FINANCIAL YEAR & REGIME SELECTION
    # -------------------------------
    st.subheader("Select Financial Year and Preferred Regime")
    col_year, col_regime = st.columns(2)
    with col_year:
        st.selectbox(
            "Financial Year",
            options=["2025-26"],
            key="financial_year"
        )
    with col_regime:
        st.radio(
            "Preferred Tax Regime",
            options=["New Regime", "Old Regime"],
            horizontal=True,
            key="preferred_regime"
        )

    # -------------------------------
    # C. COMMON INCOME FIELDS
    # -------------------------------
    st.subheader("Income Details")
    colA, colB = st.columns(2)
    with colA:
        st.number_input(
            "Income from Salary/Pension (₹)",
            min_value=0.0,
            key="income_salary",
            help="Include your basic salary, HRA, allowances, and pension."
        )
        st.number_input(
            "Income from House Property (₹)",
            min_value=0.0,
            key="income_rental",
            help="Rental income less standard deduction of 30%, or net income from house property."
        )
    with colB:
        st.number_input(
            "Income from Digital Assets (30% tax) (₹)",
            min_value=0.0,
            key="income_digital_assets",
            help="Cryptocurrency, NFTs, and other digital assets (taxed at 30%)."
        )

    # -------------------------------
    # D. REGIME-SPECIFIC FIELDS
    # -------------------------------
    if st.session_state["preferred_regime"] == "Old Regime":
        st.subheader("Deductions & Exemptions (Old Regime Only)")
        colC, colD = st.columns(2)
        with colC:
            st.number_input(
                "Basic Deductions - 80C (max ₹1.5L) (₹)",
                min_value=0.0,
                max_value=150000.0,
                key="basic_deduction_80c",
                help="PPF, ELSS, LIC, EPF, etc. (Limit: ₹1,50,000)"
            )
            st.number_input(
                "Interest on Housing Loan (max ₹2L) (₹)",
                min_value=0.0,
                max_value=200000.0,
                key="home_loan_interest",
                help="Interest on housing loan for self-occupied property (Limit: ₹2,00,000)."
            )
            st.number_input(
                "NPS Contribution - 80CCD(1B) (max ₹50K) (₹)",
                min_value=0.0,
                max_value=50000.0,
                key="nps_80ccd",
                help="Additional deduction for NPS contribution (Limit: ₹50,000)."
            )
            st.number_input(
            "Education Loan Interest - 80E (₹)",
            min_value=0.0,
            key="ded_80e",
            help="Interest paid on education loans for higher studies (deduction available for up to 8 years)."
        )
        with colD:
            st.number_input(
                "Medical Insurance - 80D (max ₹25K/50K) (₹)",
                min_value=0.0,
                max_value=50000.0,
                key="medical_insurance_80d",
                help="Health insurance premiums for self and family."
            )
            st.number_input(
                "Donations to Charity - 80G (₹)",
                min_value=0.0,
                key="donations_80g",
                help="Donations to approved funds and charitable institutions."
            )
            st.number_input(
            "Deduction for Disability - 80U (₹)",
            min_value=0.0,
            key="ded_80u",
            help="Deduction for disabled individuals. Maximum limit: ₹75,000 (40-80% disability) or ₹1,25,000 (80%+ disability)."
            )
            #Home Loan Interest (First Time) - Section 80EE
            st.number_input(
            "Home Loan Interest (First Time) - 80EE (₹)",
            min_value=0.0,
            key="ded_80ee",
            help="Additional deduction for home loan interest for first-time buyers."
            )
        st.info("Under Old Regime, you can claim multiple deductions but face higher slab rates beyond ₹5 lakh.")
    
    else:
        st.subheader("Additional Fields (New Regime)")
        st.write("""
        Under the New Regime (FY 2025-26), you generally **cannot** claim 
        most deductions like 80C, 80D, 80G, etc. However, a standard deduction 
        of ₹50,000 is available if you have salary income. 
        """)
        st.number_input(
            "Income other than Salary and Special Rate Income (₹)",
            min_value=0.0,
            key="other_income_new_regime",
            help="Additional taxable income not from salary or digital assets."
        )
        st.info("No other major deductions apply under the New Regime, except the standard deduction on salary.")

    # -------------------------------
    # E. CALCULATE TAX BUTTON
    # -------------------------------
    if st.button("Calculate Tax", type="primary", use_container_width=True):
        # === NEW/CHANGED: Always calculate BOTH new and old, for side-by-side. ===
        new_result = calculate_new_regime_2025(
            salary=st.session_state.income_salary,
            house_property=st.session_state.income_rental,
            other_income=st.session_state.get("other_income_new_regime", 0.0),
            digital_assets=st.session_state.income_digital_assets
        )

        old_result = calculate_old_regime_2025(
            salary=st.session_state.income_salary,
            house_property=st.session_state.income_rental,
            other_income=0.0,  # only if you want that set to 0 for old regime
            digital_assets=st.session_state.income_digital_assets,
            ded_80c=st.session_state.get("basic_deduction_80c", 0.0),
            ded_80d=st.session_state.get("medical_insurance_80d", 0.0),
            ded_80ccd=st.session_state.get("nps_80ccd", 0.0),
            ded_80g=st.session_state.get("donations_80g", 0.0),
            ded_other=st.session_state.get("other_deductions", 0.0),
            ded_80e=st.session_state.get("ded_80e", 0.0),
            ded_80u=st.session_state.get("ded_80u", 0.0),
            ded_80ee=st.session_state.get("ded_80ee", 0.0),
            home_loan_interest=st.session_state.get("home_loan_interest", 0.0),
        )

        # === Save both results in session_state for the comparison tab ===
        st.session_state["new_regime_result"] = new_result
        st.session_state["old_regime_result"] = old_result
        st.session_state["calculation_done"] = True

        st.success("Tax calculations complete! Check the Detailed Comparison tab.")

    # Then display a quick summary for whichever regime the user "prefers"
    if st.session_state.get("calculation_done"):
        st.subheader("Tax Summary (Preferred Regime)")
        
        if st.session_state["preferred_regime"] == "New Regime":
            result = st.session_state.get("new_regime_result", {})
        else:
            result = st.session_state.get("old_regime_result", {})

        if not result:
            st.info("No result found. Please calculate again.")
        else:
            st.write(f"**Taxable Income**: ₹{result.get('taxable_income', 0):,.2f}")
            st.write(f"**Total Tax**: ₹{result.get('total_tax', 0):,.2f}")
            st.write(f"**Slab-based Tax**: ₹{result.get('income_tax', 0):,.2f}")
            st.write(f"**Digital Assets Tax**: ₹{result.get('digital_assets_tax', 0):,.2f}")
            st.write(f"**Cess**: ₹{result.get('cess', 0):,.2f}")

            # If there's a 'rebate' field in the new regime, show it
            if "rebate" in result:
                st.write(f"**Rebate**: ₹{result['rebate']:,.2f}")

            # NEW: Show net income after tax
            if "net_income_after_tax" in result:
                st.write(f"**Net Income (After Tax)**: ₹{result['net_income_after_tax']:,.2f}")
