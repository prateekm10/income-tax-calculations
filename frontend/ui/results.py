import streamlit as st

def setup_results_area():
    if not st.session_state.get("calculation_done"):
        st.info("Please calculate your tax first on the 'Tax Calculator' tab.")
        return

    st.subheader("Detailed Tax Regime Comparison")

    st.write("DEBUG: session_state keys =>", list(st.session_state.keys()))

    new_result = st.session_state.get("new_regime_result", {})
    old_result = st.session_state.get("old_regime_result", {})
    st.write("DEBUG: new_result =>", new_result)
    st.write("DEBUG: old_result =>", old_result)


    # Card style
    card_style = """
    <style>
    .card {
        background-color: #f0f2f6;
        padding: 15px;
        margin: 10px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .card h4 {
        margin-bottom: 10px;
    }
    .card p {
        margin: 5px 0;
        font-size: 16px;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
    }
    table, th, td {
        border: 1px solid #ddd;
    }
    th, td {
        padding: 8px;
        text-align: left;
    }
    th {
        background-color: #fafafa;
    }
    </style>
    """
    st.markdown(card_style, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # -----------------------------
    # New Regime Card
    # -----------------------------
    with col1:
        st.markdown("#### New Regime")
        if new_result:
            # Basic card info
            card_html = f"""
            <div class="card">
                <h4>New Regime Summary</h4>
                <p><strong>Taxable Income:</strong> ₹{new_result.get('taxable_income', 0):,.2f}</p>
                <p><strong>Income Tax:</strong> ₹{new_result.get('income_tax', 0):,.2f}</p>
                <p><strong>Digital Assets Tax:</strong> ₹{new_result.get('digital_assets_tax', 0):,.2f}</p>
                <p><strong>Cess:</strong> ₹{new_result.get('cess', 0):,.2f}</p>
                <p><strong>Total Tax:</strong> ₹{new_result.get('total_tax', 0):,.2f}</p>
            """
            # Rebate if present
            if "rebate" in new_result:
                card_html += f"<p><strong>Rebate:</strong> ₹{new_result.get('rebate', 0):,.2f}</p>"
            card_html += "</div>"
            st.markdown(card_html, unsafe_allow_html=True)

            # Optional: Show Deductions if stored (like "total_deductions" or "standard_deduction")
            # if "standard_deduction" in new_result:
            #     st.write(f"**Standard Deduction:** ₹{new_result['standard_deduction']:,.2f}")

            # Slab-Wise Breakdown if present
            slab_breakup = new_result.get("slab_breakup", [])
            if slab_breakup:
                st.markdown("**Slab-wise Breakdown**")
                # Build an HTML table or use st.table
                table_html = """
                <table>
                    <tr>
                        <th>Income Range</th>
                        <th>Amount (₹)</th>
                        <th>Rate</th>
                        <th>Tax (₹)</th>
                    </tr>
                """
                for slab in slab_breakup:
                    table_html += f"""
                    <tr>
                        <td>{slab.get('range', '')}</td>
                        <td>{slab.get('amount', 0):,.2f}</td>
                        <td>{slab.get('rate', '')}</td>
                        <td>{slab.get('tax', 0):,.2f}</td>
                    </tr>
                    """
                table_html += "</table>"
                st.markdown(table_html, unsafe_allow_html=True)

        else:
            st.info("New Regime result not available.")

    # -----------------------------
    # Old Regime Card
    # -----------------------------
    with col2:
        st.markdown("#### Old Regime")
        if old_result:
            card_html = f"""
            <div class="card">
                <h4>Old Regime Summary</h4>
                <p><strong>Taxable Income:</strong> ₹{old_result.get('taxable_income', 0):,.2f}</p>
                <p><strong>Income Tax:</strong> ₹{old_result.get('income_tax', 0):,.2f}</p>
                <p><strong>Digital Assets Tax:</strong> ₹{old_result.get('digital_assets_tax', 0):,.2f}</p>
                <p><strong>Cess:</strong> ₹{old_result.get('cess', 0):,.2f}</p>
                <p><strong>Total Tax:</strong> ₹{old_result.get('total_tax', 0):,.2f}</p>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)

            # If you stored total_deductions or standard_deduction, you can show them:
            # if "total_deductions" in old_result:
            #     st.write(f"**Total Deductions:** ₹{old_result['total_deductions']:,.2f}")

            # Slab-Wise Breakdown
            slab_breakup = old_result.get("slab_breakup", [])
            if slab_breakup:
                st.markdown("**Slab-wise Breakdown**")
                table_html = """
                <table>
                    <tr>
                        <th>Income Range</th>
                        <th>Amount (₹)</th>
                        <th>Rate</th>
                        <th>Tax (₹)</th>
                    </tr>
                """
                for slab in slab_breakup:
                    table_html += f"""
                    <tr>
                        <td>{slab.get('range', '')}</td>
                        <td>{slab.get('amount', 0):,.2f}</td>
                        <td>{slab.get('rate', '')}</td>
                        <td>{slab.get('tax', 0):,.2f}</td>
                    </tr>
                    """
                table_html += "</table>"
                st.markdown(table_html, unsafe_allow_html=True)

        else:
            st.info("Old Regime result not available.")
