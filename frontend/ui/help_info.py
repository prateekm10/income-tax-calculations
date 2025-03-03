# frontend/ui/help_info.py
import streamlit as st
import pandas as pd

def display_tax_info():
    st.title("Tax Information FY 2025-26")
    tab1, tab2 = st.tabs(["New Regime", "Old Regime"])
    
    with tab1:
        st.header("New Tax Regime (FY 2025-26)")
        st.subheader("Income Tax Slabs")
        new_regime_slabs = [
            ["₹0 - ₹3,00,000", "No tax"],
            ["₹3,00,001 - ₹6,00,000", "5%"],
            ["₹6,00,001 - ₹9,00,000", "10%"],
            ["₹9,00,001 - ₹12,00,000", "15%"],
            ["₹12,00,001 - ₹15,00,000", "20%"],
            ["Above ₹15,00,000", "30%"]
        ]
        st.table(pd.DataFrame(new_regime_slabs, columns=["Income Range", "Tax Rate"]))
        st.markdown("""
        - Standard Deduction: ₹50,000  
        - Health & Education Cess: 4% of income tax  
        **Note:** Under the new regime, most deductions and exemptions are not available.
        """)
    
    with tab2:
        st.header("Old Tax Regime (FY 2025-26)")
        st.subheader("Income Tax Slabs")
        old_regime_slabs = [
            ["₹0 - ₹2,50,000", "No tax"],
            ["₹2,50,001 - ₹5,00,000", "5%"],
            ["₹5,00,001 - ₹10,00,000", "20%"],
            ["Above ₹10,00,000", "30%"]
        ]
        st.table(pd.DataFrame(old_regime_slabs, columns=["Income Range", "Tax Rate"]))
        st.markdown("""
        - Standard Deduction: ₹50,000  
        - Health & Education Cess: 4% of income tax  
        **Major Deductions Available:**  
        - Section 80C: Up to ₹1,50,000  
        - Section 80D: Up to ₹25,000 (₹50,000 for senior citizens)  
        - Section 80EEA: Housing loan interest up to ₹2,00,000  
        - Section 80CCD(1B): Additional NPS contribution up to ₹50,000
        """)
    
    if st.button("Back to Calculator", type="primary"):
        st.experimental_set_query_params()

def display_about():
    st.title("About the Tax Calculator")
    st.markdown("""
    ## Indian Income Tax Calculator  
    ### Version 1.0  
    This application calculates and compares income tax under both the old and new tax regimes for Indian taxpayers as per FY 2025-26 rules.  
    Developed using Python and Streamlit.  
    **Features:**  
    - Calculate tax under both old and new regimes  
    - Compare tax liabilities side by side  
    - Get tax planning recommendations  
    - Visualize your tax breakdown  
    - Save and load tax profiles  
    """)
    if st.button("Back to Calculator", type="primary"):
        st.experimental_set_query_params()
