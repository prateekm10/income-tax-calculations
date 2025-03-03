# results.py
import streamlit as st
import pandas as pd  # for slab breakdown tables

def setup_results_area():
    # 1) Check if calculation was done
    if not st.session_state.get("calculation_done"):
        st.info("Please calculate your tax first on the 'Tax Calculator' tab.")
        return

    # 2) Heading
    st.subheader("Detailed Tax Regime Comparison")

    # 3) Retrieve results from session state
    new_result = st.session_state.get("new_regime_result", {})
    old_result = st.session_state.get("old_regime_result", {})

    # 4) Create two columns: New Regime (left), Old Regime (right)
    col_left, col_right = st.columns(2)

    # -----------------------------
    # Left Column: New Regime
    # -----------------------------
    with col_left:
        st.subheader("New Regime")

        if new_result:
            # Show numeric fields
            st.write(f"**Taxable Income:** ₹{new_result.get('taxable_income', 0):,.2f}")
            st.write(f"**Income Tax:** ₹{new_result.get('income_tax', 0):,.2f}")
            st.write(f"**Digital Assets Tax:** ₹{new_result.get('digital_assets_tax', 0):,.2f}")
            st.write(f"**Cess:** ₹{new_result.get('cess', 0):,.2f}")
            st.write(f"**Total Tax:** ₹{new_result.get('total_tax', 0):,.2f}")

            # Show net income if it exists
            if "net_income_after_tax" in new_result:
                st.write(f"**Net Income (After Tax):** ₹{new_result['net_income_after_tax']:,.2f}")

            # Show rebate if present
            if "rebate" in new_result and new_result["rebate"] > 0:
                st.write(f"**Rebate:** ₹{new_result['rebate']:,.2f}")

            # Slab-wise breakdown as a table
            slab_breakup = new_result.get("slab_breakup", [])
            if slab_breakup:
                st.write("**Slab-wise Breakdown**")
                df_new = pd.DataFrame(slab_breakup)
                st.table(df_new)
        else:
            st.info("No New Regime result available.")

    # -----------------------------
    # Right Column: Old Regime
    # -----------------------------
    with col_right:
        st.subheader("Old Regime")

        if old_result:
            st.write(f"**Taxable Income:** ₹{old_result.get('taxable_income', 0):,.2f}")
            st.write(f"**Income Tax:** ₹{old_result.get('income_tax', 0):,.2f}")
            st.write(f"**Digital Assets Tax:** ₹{old_result.get('digital_assets_tax', 0):,.2f}")
            st.write(f"**Cess:** ₹{old_result.get('cess', 0):,.2f}")
            st.write(f"**Total Tax:** ₹{old_result.get('total_tax', 0):,.2f}")

            # Show net income if it exists
            if "net_income_after_tax" in old_result:
                st.write(f"**Net Income (After Tax):** ₹{old_result['net_income_after_tax']:,.2f}")

            # If old regime has standard_deduction or total_deductions you want to show, you can add them here
            # e.g. st.write(f"**Total Deductions:** ₹{old_result['total_deductions']:,.2f}")

            # Slab-wise breakdown
            slab_breakup = old_result.get("slab_breakup", [])
            if slab_breakup:
                st.write("**Slab-wise Breakdown**")
                df_old = pd.DataFrame(slab_breakup)
                st.table(df_old)
        else:
            st.info("No Old Regime result available.")
