import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def setup_analytics_tab():
    """
    Analytics Tab: Display advanced visualizations comparing Old vs New Regime using Plotly.
    This version incorporates interactive expanders for interpretation, enhanced chart titles and labels,
    and a clean aesthetic for a better user experience.
    """
    if not st.session_state.get("calculation_done", False):
        st.info("Please calculate your tax first on the 'Tax Calculator' tab.")
        return

    st.subheader("Tax Analytics")

    # Retrieve results from session state
    new_res = st.session_state.get("new_regime_result", {})
    old_res = st.session_state.get("old_regime_result", {})

    if not new_res or not old_res:
        st.info("Need both Old & New Regime results to show analytics.")
        return

    # -------------------------------------------------------------------------
    # A) Key Metrics Comparison (Bar Chart)
    # -------------------------------------------------------------------------
    st.markdown("### 1. Key Metrics Comparison")
    old_total_tax = old_res.get("total_tax", 0.0)
    new_total_tax = new_res.get("total_tax", 0.0)
    old_net_income = old_res.get("net_income_after_tax", 0.0)
    new_net_income = new_res.get("net_income_after_tax", 0.0)
    old_taxable_inc = old_res.get("taxable_income", 0.0)
    new_taxable_inc = new_res.get("taxable_income", 0.0)
    old_digital_tax = old_res.get("digital_assets_tax", 0.0)
    new_digital_tax = new_res.get("digital_assets_tax", 0.0)

    # Create a DataFrame for key metrics
    df_metrics = pd.DataFrame({
        "Metric": [
            "Taxable Income",
            "Total Tax",
            "Digital Assets Tax",
            "Net Income (After Tax)"
        ],
        "Old Regime": [
            old_taxable_inc,
            old_total_tax,
            old_digital_tax,
            old_net_income
        ],
        "New Regime": [
            new_taxable_inc,
            new_total_tax,
            new_digital_tax,
            new_net_income
        ]
    })
    # Melt the DataFrame for Plotly
    df_long = df_metrics.melt(id_vars="Metric", var_name="Regime", value_name="Value")

    fig_bar = px.bar(
        df_long,
        x="Metric",
        y="Value",
        color="Regime",
        barmode="group",
        title="Key Metrics: Old vs New Regime",
        labels={"Value": "Amount (₹)", "Metric": "Metric"}
    )
    # Improve numeric formatting
    fig_bar.update_yaxes(tickprefix="₹", separatethousands=True)
    st.plotly_chart(fig_bar, use_container_width=True)

    with st.expander("Interpretation"):
        st.markdown("""
        **Key Metrics Interpretation:**
        - **Taxable Income:** Total income subject to tax.
        - **Total Tax:** Overall tax liability computed.
        - **Digital Assets Tax:** Flat tax computed on digital assets.
        - **Net Income (After Tax):** Income remaining after tax deductions.
        """)

    # -------------------------------------------------------------------------
    # B) Slab Tax Breakdown (Grouped Horizontal Bar Chart)
    # -------------------------------------------------------------------------
    st.markdown("### 2. Slab Tax Breakdown Comparison")

    # Retrieve slab data from both regimes
    old_slabs = old_res.get("slab_breakup", [])
    new_slabs = new_res.get("slab_breakup", [])

    if not old_slabs or not new_slabs:
        st.info("Slab breakdown data not available in one or both regimes.")
    else:
        # Convert each list to a DataFrame and add a regime column
        df_old_slabs = pd.DataFrame(old_slabs)
        df_old_slabs["Regime"] = "Old Regime"
        df_new_slabs = pd.DataFrame(new_slabs)
        df_new_slabs["Regime"] = "New Regime"

        # Rename columns for consistency (assuming keys 'range' and 'tax')
        df_old_slabs.rename(columns={"range": "Slab", "tax": "SlabTax"}, inplace=True)
        df_new_slabs.rename(columns={"range": "Slab", "tax": "SlabTax"}, inplace=True)

        # Combine the two DataFrames
        df_slabs = pd.concat([df_old_slabs, df_new_slabs], ignore_index=True)
        df_slabs.fillna(0, inplace=True)

        fig_slabs = px.bar(
            df_slabs,
            x="SlabTax",
            y="Slab",
            color="Regime",
            orientation="h",
            title="Income Slab-wise Tax Contribution",
            labels={"SlabTax": "Tax Amount (₹)", "Slab": "Income Slab"}
        )
        fig_slabs.update_xaxes(tickprefix="₹", separatethousands=True)
        st.plotly_chart(fig_slabs, use_container_width=True)

        with st.expander("Interpretation"):
            st.markdown("""
            **Slab Breakdown Interpretation:**
            - Each horizontal bar shows the tax amount for a specific income slab.
            - Longer bars indicate a higher tax contribution within that slab.
            - Compare between regimes to identify the tax impact of different income ranges.
            """)

    # -------------------------------------------------------------------------
    # C) Tax Components Breakdown (Sunburst Chart)
    # -------------------------------------------------------------------------
    st.markdown("### 3. Tax Components Breakdown (Sunburst Chart)")

    # Construct a DataFrame for tax components from each regime
    components_data = {
        "Regime": ["Old Regime", "Old Regime", "Old Regime",
                   "New Regime", "New Regime", "New Regime"],
        "Component": ["Slab Tax", "Digital Assets Tax", "Cess",
                      "Slab Tax", "Digital Assets Tax", "Cess"],
        "Amount": [
            old_res.get("income_tax", 0.0),
            old_res.get("digital_assets_tax", 0.0),
            old_res.get("cess", 0.0),
            new_res.get("income_tax", 0.0),
            new_res.get("digital_assets_tax", 0.0),
            new_res.get("cess", 0.0)
        ]
    }
    df_components = pd.DataFrame(components_data)

    fig_sunburst = px.sunburst(
        df_components,
        path=["Regime", "Component"],
        values="Amount",
        title="Tax Components Breakdown by Regime",
        color="Component",
        color_discrete_map={"Slab Tax": "#636EFA", "Digital Assets Tax": "#EF553B", "Cess": "#00CC96"}
    )
    fig_sunburst.update_traces(textinfo="label+percent entry")
    st.plotly_chart(fig_sunburst, use_container_width=True)

    with st.expander("Interpretation"):
        st.markdown("""
        **Sunburst Chart Interpretation:**
        - Visualizes how total tax is distributed into slab tax, digital assets tax, and cess.
        - Hover over segments to see detailed percentage contributions.
        - Helps in comparing the allocation of tax components between regimes.
        """)

    st.markdown("### 4. Tax Components Breakdown (Stacked Bar Chart)")

    fig_stack = px.bar(
        df_components,
        x="Regime",
        y="Amount",
        color="Component",
        title="Tax Components Breakdown by Regime (Stacked)",
        labels={"Amount": "Amount (₹)", "Regime": "Tax Regime"},
        barmode="stack",
        color_discrete_map={"Slab Tax": "#636EFA", "Digital Assets Tax": "#EF553B", "Cess": "#00CC96"}
    )
    fig_stack.update_yaxes(tickprefix="₹", separatethousands=True)
    st.plotly_chart(fig_stack, use_container_width=True)

    with st.expander("Stacked Bar Chart Interpretation"):
        st.markdown("""
        **Stacked Bar Chart Interpretation:**
        - Displays tax components for each regime as a stack, showing their cumulative contribution.
        - Makes it easy to compare the overall composition of tax across regimes.
        - Allows direct comparison of the weight of each component between the Old and New Regimes.
        """)

    # -------------------------------------------------------------------------
    # D) Tax vs. Taxable Income Bubble Chart
    # -------------------------------------------------------------------------
    st.markdown("### 5. Tax vs. Taxable Income Bubble Chart")

    # Create a DataFrame for the bubble chart comparing taxable income vs total tax
    df_bubble = pd.DataFrame({
        "Regime": ["Old Regime", "New Regime"],
        "Taxable Income": [old_taxable_inc, new_taxable_inc],
        "Total Tax": [old_total_tax, new_total_tax],
        "Net Income After Tax": [old_net_income, new_net_income]
    })

    fig_bubble = px.scatter(
        df_bubble,
        x="Taxable Income",
        y="Total Tax",
        size="Net Income After Tax",
        color="Regime",
        hover_name="Regime",
        title="Taxable Income vs Total Tax (Bubble Size = Net Income After Tax)",
        labels={"Taxable Income": "Taxable Income (₹)", "Total Tax": "Total Tax (₹)"}
    )
    fig_bubble.update_xaxes(tickprefix="₹", separatethousands=True)
    fig_bubble.update_yaxes(tickprefix="₹", separatethousands=True)
    st.plotly_chart(fig_bubble, use_container_width=True)

    with st.expander("Interpretation"):
        st.markdown("""
        **Bubble Chart Interpretation:**
        - Plots taxable income against total tax for each regime.
        - Bubble size indicates net income after tax, providing a sense of the overall tax burden.
        - Use this chart to visually assess which regime leaves you with more post-tax income.
        """)

    # -------------------------------------------------------------------------
    # E) Observations & Next Steps
    # -------------------------------------------------------------------------
    st.write("---")
    st.write("#### Observations & Next Steps")
    if "df_old_slabs" in locals() and "df_new_slabs" in locals():
        old_slab_total = df_old_slabs["SlabTax"].sum() if "SlabTax" in df_old_slabs else 0
        new_slab_total = df_new_slabs["SlabTax"].sum() if "SlabTax" in df_new_slabs else 0
    else:
        old_slab_total, new_slab_total = 0, 0

    st.write(f"- **Total Slab Tax (Old Regime):** ₹{old_slab_total:,.2f}")
    st.write(f"- **Total Slab Tax (New Regime):** ₹{new_slab_total:,.2f}")
    st.write("""
    Analyze these observations to refine your tax planning strategy.
    Use the interactive charts above to explore different facets of your tax liability,
    and identify opportunities for optimizing your overall tax burden.
    """)
