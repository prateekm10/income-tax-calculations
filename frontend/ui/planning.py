# planning.py
import streamlit as st
import pandas as pd

def setup_planning_tab():
    if not st.session_state.get("calculation_done", False):
        st.info("Please calculate your tax first on the 'Tax Calculator' tab.")
        return
    
    st.subheader("Tax Planning - Comparison and Recommendations")

    # 1) Retrieve results for both regimes
    new_res = st.session_state.get("new_regime_result", {})
    old_res = st.session_state.get("old_regime_result", {})

    # If either result is missing, just show a message
    if not new_res or not old_res:
        st.info("We need both Old and New Regime calculations for comprehensive planning.")
        return

    # 2) Extract key amounts from each result
    # (Add more fields if you want to highlight them)
    new_total_tax = new_res.get("total_tax", 0.0)
    old_total_tax = old_res.get("total_tax", 0.0)
    new_net_income = new_res.get("net_income_after_tax", 0.0)
    old_net_income = old_res.get("net_income_after_tax", 0.0)
    new_taxable_inc = new_res.get("taxable_income", 0.0)
    old_taxable_inc = old_res.get("taxable_income", 0.0)
    new_digital_tax = new_res.get("digital_assets_tax", 0.0)
    old_digital_tax = old_res.get("digital_assets_tax", 0.0)

    # 3) Compute differences
    tax_diff = old_total_tax - new_total_tax  # +ve => new is cheaper, -ve => old is cheaper
    net_income_diff = new_net_income - old_net_income
    digital_assets_diff = old_digital_tax - new_digital_tax

    # 4) Create a small summary table
    #    Each row: Parameter, Old Regime Value, New Regime Value, Difference
    data = [
        {
            "Parameter": "Taxable Income",
            "Old Regime (₹)": old_taxable_inc,
            "New Regime (₹)": new_taxable_inc,
            "Difference": new_taxable_inc - old_taxable_inc
        },
        {
            "Parameter": "Total Tax",
            "Old Regime (₹)": old_total_tax,
            "New Regime (₹)": new_total_tax,
            "Difference": tax_diff
        },
        {
            "Parameter": "Net Income (After Tax)",
            "Old Regime (₹)": old_net_income,
            "New Regime (₹)": new_net_income,
            "Difference": net_income_diff
        },
        {
            "Parameter": "Digital Assets Tax",
            "Old Regime (₹)": old_digital_tax,
            "New Regime (₹)": new_digital_tax,
            "Difference": digital_assets_diff
        },
    ]

    df = pd.DataFrame(data)
    # Format numeric columns with thousands separators
    numeric_cols = ["Old Regime (₹)", "New Regime (₹)", "Difference"]
    for col in numeric_cols:
        df[col] = df[col].apply(lambda x: f"₹{x:,.2f}")

    st.write("### Differences Overview")
    st.table(df)

    # 5) Provide a short recommendation text
    st.write("### Recommendations")
    if tax_diff > 0:
        # positive => old_tax - new_tax > 0 => new is cheaper
        st.success(
            f"**New Regime** could save you approximately **₹{tax_diff:,.2f}** "
            f"in taxes compared to the Old Regime."
        )
    elif tax_diff < 0:
        # negative => old_tax - new_tax < 0 => old is cheaper
        st.success(
            f"**Old Regime** could save you approximately **₹{abs(tax_diff):,.2f}** "
            f"in taxes compared to the New Regime."
        )
    else:
        st.info("No difference in total tax between Old and New Regimes based on your inputs.")

    # 6) (Optional) Additional commentary about large digital asset holdings, etc.
    if abs(digital_assets_diff) > 0:
        st.write(
            f"**Digital Assets Impact**: The difference in digital assets tax between the two regimes "
            f"is ₹{abs(digital_assets_diff):,.2f}. (Note: Digital asset tax rates are generally flat 30%.)"
        )

    st.write("""
    - If you have **significant deductions** (like 80C, 80D, HRA, home loan interest), 
      the **Old Regime** might be more beneficial.
    - If you **don't** have many deductions or your income is primarily from salary 
      (plus minimal investments), the **New Regime** might offer a lower tax rate.
    - Always compare **both** to find the best fit for your specific financial situation.
    """)
