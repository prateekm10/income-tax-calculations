# # import streamlit as st
# # import pandas as pd
# # import plotly.express as px
# # import plotly.graph_objects as go

# # def setup_analytics_tab():
# #     """
# #     Analytics Tab: Display advanced visualizations comparing Old vs New Regime using Plotly.
# #     This version incorporates interactive expanders for interpretation, enhanced chart titles and labels,
# #     and a clean aesthetic for a better user experience.
# #     """
# #     if not st.session_state.get("calculation_done", False):
# #         st.info("Please calculate your tax first on the 'Tax Calculator' tab.")
# #         return

# #     st.subheader("Tax Analytics")

# #     # Retrieve results from session state
# #     new_res = st.session_state.get("new_regime_result", {})
# #     old_res = st.session_state.get("old_regime_result", {})

# #     if not new_res or not old_res:
# #         st.info("Need both Old & New Regime results to show analytics.")
# #         return

# #     # -------------------------------------------------------------------------
# #     # A) Key Metrics Comparison (Bar Chart)
# #     # -------------------------------------------------------------------------
# #     st.markdown("### 1. Key Metrics Comparison")
# #     old_total_tax = old_res.get("total_tax", 0.0)
# #     new_total_tax = new_res.get("total_tax", 0.0)
# #     old_net_income = old_res.get("net_income_after_tax", 0.0)
# #     new_net_income = new_res.get("net_income_after_tax", 0.0)
# #     old_taxable_inc = old_res.get("taxable_income", 0.0)
# #     new_taxable_inc = new_res.get("taxable_income", 0.0)
# #     old_digital_tax = old_res.get("digital_assets_tax", 0.0)
# #     new_digital_tax = new_res.get("digital_assets_tax", 0.0)

# #     # Create a DataFrame for key metrics
# #     df_metrics = pd.DataFrame({
# #         "Metric": [
# #             "Taxable Income",
# #             "Total Tax",
# #             "Digital Assets Tax",
# #             "Net Income (After Tax)"
# #         ],
# #         "Old Regime": [
# #             old_taxable_inc,
# #             old_total_tax,
# #             old_digital_tax,
# #             old_net_income
# #         ],
# #         "New Regime": [
# #             new_taxable_inc,
# #             new_total_tax,
# #             new_digital_tax,
# #             new_net_income
# #         ]
# #     })
# #     # Melt the DataFrame for Plotly
# #     df_long = df_metrics.melt(id_vars="Metric", var_name="Regime", value_name="Value")

# #     fig_bar = px.bar(
# #         df_long,
# #         x="Metric",
# #         y="Value",
# #         color="Regime",
# #         barmode="group",
# #         title="Key Metrics: Old vs New Regime",
# #         labels={"Value": "Amount (₹)", "Metric": "Metric"}
# #     )
# #     # Improve numeric formatting
# #     fig_bar.update_yaxes(tickprefix="₹", separatethousands=True)
# #     st.plotly_chart(fig_bar, use_container_width=True)

# #     with st.expander("Interpretation"):
# #         st.markdown("""
# #         **Key Metrics Interpretation:**
# #         - **Taxable Income:** Total income subject to tax.
# #         - **Total Tax:** Overall tax liability computed.
# #         - **Digital Assets Tax:** Flat tax computed on digital assets.
# #         - **Net Income (After Tax):** Income remaining after tax deductions.
# #         """)

# #     # -------------------------------------------------------------------------
# #     # B) Slab Tax Breakdown (Grouped Horizontal Bar Chart)
# #     # -------------------------------------------------------------------------
# #     st.markdown("### 2. Slab Tax Breakdown Comparison")

# #     # Retrieve slab data from both regimes
# #     old_slabs = old_res.get("slab_breakup", [])
# #     new_slabs = new_res.get("slab_breakup", [])

# #     if not old_slabs or not new_slabs:
# #         st.info("Slab breakdown data not available in one or both regimes.")
# #     else:
# #         # Convert each list to a DataFrame and add a regime column
# #         df_old_slabs = pd.DataFrame(old_slabs)
# #         df_old_slabs["Regime"] = "Old Regime"
# #         df_new_slabs = pd.DataFrame(new_slabs)
# #         df_new_slabs["Regime"] = "New Regime"

# #         # Rename columns for consistency (assuming keys 'range' and 'tax')
# #         df_old_slabs.rename(columns={"range": "Slab", "tax": "SlabTax"}, inplace=True)
# #         df_new_slabs.rename(columns={"range": "Slab", "tax": "SlabTax"}, inplace=True)

# #         # Combine the two DataFrames
# #         df_slabs = pd.concat([df_old_slabs, df_new_slabs], ignore_index=True)
# #         df_slabs.fillna(0, inplace=True)

# #         fig_slabs = px.bar(
# #             df_slabs,
# #             x="SlabTax",
# #             y="Slab",
# #             color="Regime",
# #             orientation="h",
# #             title="Income Slab-wise Tax Contribution",
# #             labels={"SlabTax": "Tax Amount (₹)", "Slab": "Income Slab"}
# #         )
# #         fig_slabs.update_xaxes(tickprefix="₹", separatethousands=True)
# #         st.plotly_chart(fig_slabs, use_container_width=True)

# #         with st.expander("Interpretation"):
# #             st.markdown("""
# #             **Slab Breakdown Interpretation:**
# #             - Each horizontal bar shows the tax amount for a specific income slab.
# #             - Longer bars indicate a higher tax contribution within that slab.
# #             - Compare between regimes to identify the tax impact of different income ranges.
# #             """)

# #     # -------------------------------------------------------------------------
# #     # C) Tax Components Breakdown (Sunburst Chart)
# #     # -------------------------------------------------------------------------
# #     st.markdown("### 3. Tax Components Breakdown (Sunburst Chart)")

# #     # Construct a DataFrame for tax components from each regime
# #     components_data = {
# #         "Regime": ["Old Regime", "Old Regime", "Old Regime",
# #                    "New Regime", "New Regime", "New Regime"],
# #         "Component": ["Slab Tax", "Digital Assets Tax", "Cess",
# #                       "Slab Tax", "Digital Assets Tax", "Cess"],
# #         "Amount": [
# #             old_res.get("income_tax", 0.0),
# #             old_res.get("digital_assets_tax", 0.0),
# #             old_res.get("cess", 0.0),
# #             new_res.get("income_tax", 0.0),
# #             new_res.get("digital_assets_tax", 0.0),
# #             new_res.get("cess", 0.0)
# #         ]
# #     }
# #     df_components = pd.DataFrame(components_data)

# #     fig_sunburst = px.sunburst(
# #         df_components,
# #         path=["Regime", "Component"],
# #         values="Amount",
# #         title="Tax Components Breakdown by Regime",
# #         color="Component",
# #         color_discrete_map={"Slab Tax": "#636EFA", "Digital Assets Tax": "#EF553B", "Cess": "#00CC96"}
# #     )
# #     fig_sunburst.update_traces(textinfo="label+percent entry")
# #     st.plotly_chart(fig_sunburst, use_container_width=True)

# #     with st.expander("Interpretation"):
# #         st.markdown("""
# #         **Sunburst Chart Interpretation:**
# #         - Visualizes how total tax is distributed into slab tax, digital assets tax, and cess.
# #         - Hover over segments to see detailed percentage contributions.
# #         - Helps in comparing the allocation of tax components between regimes.
# #         """)

# #     st.markdown("### 4. Tax Components Breakdown (Stacked Bar Chart)")

# #     fig_stack = px.bar(
# #         df_components,
# #         x="Regime",
# #         y="Amount",
# #         color="Component",
# #         title="Tax Components Breakdown by Regime (Stacked)",
# #         labels={"Amount": "Amount (₹)", "Regime": "Tax Regime"},
# #         barmode="stack",
# #         color_discrete_map={"Slab Tax": "#636EFA", "Digital Assets Tax": "#EF553B", "Cess": "#00CC96"}
# #     )
# #     fig_stack.update_yaxes(tickprefix="₹", separatethousands=True)
# #     st.plotly_chart(fig_stack, use_container_width=True)

# #     with st.expander("Stacked Bar Chart Interpretation"):
# #         st.markdown("""
# #         **Stacked Bar Chart Interpretation:**
# #         - Displays tax components for each regime as a stack, showing their cumulative contribution.
# #         - Makes it easy to compare the overall composition of tax across regimes.
# #         - Allows direct comparison of the weight of each component between the Old and New Regimes.
# #         """)

# #     # -------------------------------------------------------------------------
# #     # D) Tax vs. Taxable Income Bubble Chart
# #     # -------------------------------------------------------------------------
# #     st.markdown("### 5. Tax vs. Taxable Income Bubble Chart")

# #     # Create a DataFrame for the bubble chart comparing taxable income vs total tax
# #     df_bubble = pd.DataFrame({
# #         "Regime": ["Old Regime", "New Regime"],
# #         "Taxable Income": [old_taxable_inc, new_taxable_inc],
# #         "Total Tax": [old_total_tax, new_total_tax],
# #         "Net Income After Tax": [old_net_income, new_net_income]
# #     })

# #     fig_bubble = px.scatter(
# #         df_bubble,
# #         x="Taxable Income",
# #         y="Total Tax",
# #         size="Net Income After Tax",
# #         color="Regime",
# #         hover_name="Regime",
# #         title="Taxable Income vs Total Tax (Bubble Size = Net Income After Tax)",
# #         labels={"Taxable Income": "Taxable Income (₹)", "Total Tax": "Total Tax (₹)"}
# #     )
# #     fig_bubble.update_xaxes(tickprefix="₹", separatethousands=True)
# #     fig_bubble.update_yaxes(tickprefix="₹", separatethousands=True)
# #     st.plotly_chart(fig_bubble, use_container_width=True)

# #     with st.expander("Interpretation"):
# #         st.markdown("""
# #         **Bubble Chart Interpretation:**
# #         - Plots taxable income against total tax for each regime.
# #         - Bubble size indicates net income after tax, providing a sense of the overall tax burden.
# #         - Use this chart to visually assess which regime leaves you with more post-tax income.
# #         """)

# #         # -------------------------------------------------------------------------
# #     # F) Waterfall Chart (Chart #6)
# #     # -------------------------------------------------------------------------
# #     st.markdown("### 6. Waterfall Chart")

# #     # Extract relevant amounts from old regime
# #     old_gross_income = old_res.get("gross_income", 0.0)
# #     old_total_deductions = old_res.get("total_deductions", 0.0)
# #     old_slab_tax = old_res.get("income_tax", 0.0)
# #     old_digital_tax = old_res.get("digital_assets_tax", 0.0)
# #     old_cess = old_res.get("cess", 0.0)
# #     old_net_income = old_res.get("net_income_after_tax", 0.0)

# #     # Create a DataFrame that outlines the steps from gross to net income
# #     df_waterfall = pd.DataFrame({
# #         "label": [
# #             "Gross Income",
# #             "(-) Deductions",
# #             "(-) Slab Tax",
# #             "(-) Digital Assets Tax",
# #             "(-) Cess",
# #             "Net Income"
# #         ],
# #         "value": [
# #             old_gross_income,
# #             -old_total_deductions,
# #             -old_slab_tax,
# #             -old_digital_tax,
# #             -old_cess,
# #             old_net_income
# #         ],
# #         "measure": [
# #             "relative",  # Starting point
# #             "relative",  # Subtract deductions
# #             "relative",  # Subtract slab tax
# #             "relative",  # Subtract digital assets tax
# #             "relative",  # Subtract cess
# #             "total"      # Final total (Net Income)
# #         ]
# #     })

# #     fig_waterfall = go.Figure(
# #         go.Waterfall(
# #             orientation="v",
# #             measure=df_waterfall["measure"],
# #             x=df_waterfall["label"],
# #             y=df_waterfall["value"],
# #             connector={"line": {"color": "rgb(63, 63, 63)"}},
# #         )
# #     )
# #     fig_waterfall.update_layout(
# #         title="Old Regime: From Gross Income to Net Income (Waterfall)",
# #         yaxis=dict(tickprefix="₹", separatethousands=True)
# #     )
# #     st.plotly_chart(fig_waterfall, use_container_width=True, key="waterfall_chart1")

# #     with st.expander("Waterfall Chart Interpretation"):
# #         st.markdown("""
# #         **Waterfall Chart Interpretation**:
# #         - Starts with Gross Income and subtracts deductions, slab tax, digital assets tax, and cess.
# #         - The final bar (Net Income) shows the effective income after all subtractions.
# #         - Hover over each bar for exact amounts.
# #         """)

# #     # -------------------------------------------------------------------------
# #     # G) Interactive Dashboard (Chart #7)
# #     # -------------------------------------------------------------------------
# #     st.markdown("### 7. Interactive Dashboard")
    
# #     # Create two sub-tabs within the dashboard: "Overview" and "Benchmark Comparison"
# #     dashboard_tabs = st.tabs(["Overview", "Benchmark Comparison"])
    
# #     # --- Dashboard Overview Tab ---
# #     with dashboard_tabs[0]:
# #         st.subheader("Overview")
# #         # Display key metrics in a 4-column layout
# #         col1, col2, col3, col4 = st.columns(4)
# #         col1.metric("Taxable Income (Old)", f"₹{old_taxable_inc:,.2f}")
# #         col2.metric("Taxable Income (New)", f"₹{new_taxable_inc:,.2f}")
# #         col3.metric("Total Tax (Old)", f"₹{old_total_tax:,.2f}")
# #         col4.metric("Total Tax (New)", f"₹{new_total_tax:,.2f}")
        
# #         # Display the Waterfall Chart again with a unique key
# #         st.plotly_chart(fig_waterfall, use_container_width=True, key="waterfall_chart_dashboard")
        
# #         st.markdown("""
# #         **Overview Interpretation:**
# #         - Key metrics provide a quick snapshot of your tax calculations.
# #         - The waterfall chart illustrates the step-by-step reduction from gross income to net income.
# #         """)
    
# #     # --- Benchmark Comparison Tab ---
# #     with dashboard_tabs[1]:
# #         st.subheader("Benchmark Comparison")
# #         # Create a dropdown to select a benchmark category
# #         benchmark_category = st.selectbox("Select Benchmark Category", ["Low Income", "Average Income", "High Income"])
        
# #         # For demonstration, assign benchmark effective tax rates based on category.
# #         benchmark_tax_rate = {
# #             "Low Income": 5,
# #             "Average Income": 15,
# #             "High Income": 25
# #         }.get(benchmark_category, 15)
        
# #         st.write(f"**Benchmark Tax Rate:** {benchmark_tax_rate}%")
        
# #         # Compute effective tax rates for both regimes (avoiding division by zero)
# #         gross_old = old_res.get("gross_income", 1)
# #         gross_new = new_res.get("gross_income", 1)
# #         effective_tax_old = (old_total_tax / gross_old * 100) if gross_old > 0 else 0
# #         effective_tax_new = (new_total_tax / gross_new * 100) if gross_new > 0 else 0
        
# #         # Build a DataFrame for the comparison
# #         df_benchmark = pd.DataFrame({
# #             "Category": ["Old Regime", "New Regime", "Benchmark"],
# #             "Effective Tax Rate (%)": [effective_tax_old, effective_tax_new, benchmark_tax_rate]
# #         })
        
# #         # Create a clean, modern bar chart for the comparison
# #         fig_benchmark = px.bar(
# #             df_benchmark,
# #             x="Category",
# #             y="Effective Tax Rate (%)",
# #             color="Category",
# #             text="Effective Tax Rate (%)",
# #             title="Effective Tax Rate: Your Calculation vs Benchmark"
# #         )
# #         fig_benchmark.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
# #         fig_benchmark.update_layout(
# #             uniformtext_minsize=8,
# #             uniformtext_mode='hide',
# #             yaxis=dict(separatethousands=True)
# #         )
# #         st.plotly_chart(fig_benchmark, use_container_width=True, key="benchmark_chart")
        
# #         st.markdown("""
# #         **Benchmark Interpretation:**
# #         - This chart compares your effective tax rates with a benchmark value.
# #         - Use this insight to adjust your financial planning strategies.
# #         """)


# #     # -------------------------------------------------------------------------
# #     # E) Observations & Next Steps
# #     # -------------------------------------------------------------------------
# #     st.write("---")
# #     st.write("#### Observations & Next Steps")
# #     if "df_old_slabs" in locals() and "df_new_slabs" in locals():
# #         old_slab_total = df_old_slabs["SlabTax"].sum() if "SlabTax" in df_old_slabs else 0
# #         new_slab_total = df_new_slabs["SlabTax"].sum() if "SlabTax" in df_new_slabs else 0
# #     else:
# #         old_slab_total, new_slab_total = 0, 0

# #     st.write(f"- **Total Slab Tax (Old Regime):** ₹{old_slab_total:,.2f}")
# #     st.write(f"- **Total Slab Tax (New Regime):** ₹{new_slab_total:,.2f}")
# #     st.write("""
# #     Analyze these observations to refine your tax planning strategy.
# #     Use the interactive charts above to explore different facets of your tax liability,
# #     and identify opportunities for optimizing your overall tax burden.
# #     """)









# ## <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< DASHBOARD LAYOUT >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go

# def setup_analytics_tab():
#     """
#     Analytics Tab: Displays a dashboard composed of two main sections:
#       - Overview: High-level metrics and benchmark comparison.
#       - Details: Sub-tabs for each individual chart.
#     This modular design makes the dashboard clean and easy to extend.
#     """
#     if not st.session_state.get("calculation_done", False):
#         st.info("Please calculate your tax first on the 'Tax Calculator' tab.")
#         return

#     # Retrieve results from session state
#     new_res = st.session_state.get("new_regime_result", {})
#     old_res = st.session_state.get("old_regime_result", {})

#     if not new_res or not old_res:
#         st.info("Need both Old & New Regime results to show analytics.")
#         return

#     # Extract common variables
#     old_total_tax = old_res.get("total_tax", 0.0)
#     new_total_tax = new_res.get("total_tax", 0.0)
#     old_net_income = old_res.get("net_income_after_tax", 0.0)
#     new_net_income = new_res.get("net_income_after_tax", 0.0)
#     old_taxable_inc = old_res.get("taxable_income", 0.0)
#     new_taxable_inc = new_res.get("taxable_income", 0.0)
#     old_digital_tax = old_res.get("digital_assets_tax", 0.0)
#     new_digital_tax = new_res.get("digital_assets_tax", 0.0)

#     # -------------------------------------------------------------------------
#     # Create Main Dashboard Tabs: Overview and Details
#     # -------------------------------------------------------------------------
#     main_tabs = st.tabs(["Overview", "Details"])

#     # ----------------------------
#     # Overview Tab
#     # ----------------------------
#     with main_tabs[0]:
#         st.subheader("Overview")
#         # Display key metrics as individual cards using st.metric
#         col1, col2, col3, col4 = st.columns(4)
#         col1.metric("Taxable Income (Old)", f"₹{old_taxable_inc:,.2f}")
#         col2.metric("Taxable Income (New)", f"₹{new_taxable_inc:,.2f}")
#         col3.metric("Total Tax (Old)", f"₹{old_total_tax:,.2f}")
#         col4.metric("Total Tax (New)", f"₹{new_total_tax:,.2f}")

#         # Create a summary bar chart for key metrics
#         df_metrics = pd.DataFrame({
#             "Metric": [
#                 "Taxable Income",
#                 "Total Tax",
#                 "Digital Assets Tax",
#                 "Net Income (After Tax)"
#             ],
#             "Old Regime": [old_taxable_inc, old_total_tax, old_digital_tax, old_net_income],
#             "New Regime": [new_taxable_inc, new_total_tax, new_digital_tax, new_net_income]
#         })
#         df_long = df_metrics.melt(id_vars="Metric", var_name="Regime", value_name="Value")
#         fig_summary = px.bar(
#             df_long,
#             x="Metric",
#             y="Value",
#             color="Regime",
#             barmode="group",
#             title="Key Metrics Comparison"
#         )
#         fig_summary.update_yaxes(tickprefix="₹", separatethousands=True)
#         st.plotly_chart(fig_summary, use_container_width=True, key="overview_summary")

#         # Benchmark Comparison
#         st.markdown("#### Benchmark Comparison")
#         from plotly.subplots import make_subplots
#         import plotly.graph_objects as go

#         # 1) Calculate effective tax rates
#         gross_old = old_res.get("gross_income", 1)
#         gross_new = new_res.get("gross_income", 1)
#         effective_tax_old = (old_total_tax / gross_old * 100) if gross_old > 0 else 0
#         effective_tax_new = (new_total_tax / gross_new * 100) if gross_new > 0 else 0

#         # 2) Create a dual gauge layout
#         fig_dual_gauge = make_subplots(
#             rows=1, cols=2,
#             specs=[[{"type": "domain"}, {"type": "domain"}]],
#             # We'll omit subplot_titles to reduce text clutter
#         )

#         # 3) Add the Old Regime gauge
#         fig_dual_gauge.add_trace(
#             go.Indicator(
#                 mode="gauge+number",
#                 value=effective_tax_old,
#                 # Minimal text: just "Old Regime"
#                 title={"text": "Old Regime"},
#                 gauge={
#                     "axis": {"range": [0, 40]},  # We'll assume 0-40% range
#                     "bar": {"color": "blue"},
#                     # No extra steps for a cleaner look
#                 },
#                 # Reduce the size of the number text
#                 number={"font": {"size": 36}}
#             ),
#             row=1, col=1
#         )

#         # 4) Add the New Regime gauge
#         fig_dual_gauge.add_trace(
#             go.Indicator(
#                 mode="gauge+number",
#                 value=effective_tax_new,
#                 title={"text": "New Regime"},
#                 gauge={
#                     "axis": {"range": [0, 40]},
#                     "bar": {"color": "green"},
#                 },
#                 number={"font": {"size": 36}}
#             ),
#             row=1, col=2
#         )

#         # 5) Final layout adjustments
#         fig_dual_gauge.update_layout(
#             title_text="Effective Tax Rate: Old vs. New Regime",
#             margin=dict(l=40, r=40)
#         )

#         st.plotly_chart(fig_dual_gauge, use_container_width=True, key="overview_dual_gauge")


#     # ----------------------------
#     # Details Tab with Sub-Tabs for Each Chart
#     # ----------------------------
#     with main_tabs[1]:
#         detail_tabs = st.tabs([
#             "Key Metrics", "Slab Breakdown", "Sunburst", "Stacked", "Bubble", "Waterfall"
#         ])

#         # Sub-tab: Key Metrics (reuse summary bar chart)
#         with detail_tabs[0]:
#             st.markdown("### Key Metrics Comparison")
#             st.plotly_chart(fig_summary, use_container_width=True, key="detail_keymetrics")

#         # Sub-tab: Slab Breakdown
#         with detail_tabs[1]:
#             st.markdown("### Slab Tax Breakdown Comparison")
#             # Retrieve slab data from both regimes; note that the original data contains columns:
#             # 'range', 'amount', 'rate', 'tax'. We will use 'tax' for the tax value and 'range' for the income slab.
#             old_slabs = old_res.get("slab_breakup", [])
#             new_slabs = new_res.get("slab_breakup", [])
#             if not old_slabs or not new_slabs:
#                 st.info("Slab breakdown data not available in one or both regimes.")
#             else:
#                 df_old_slabs = pd.DataFrame(old_slabs)
#                 df_old_slabs["Regime"] = "Old Regime"
#                 df_new_slabs = pd.DataFrame(new_slabs)
#                 df_new_slabs["Regime"] = "New Regime"
#                 # Use the original column names: 'range' for slab and 'tax' for tax amount.
#                 fig_slabs = px.bar(
#                     pd.concat([df_old_slabs, df_new_slabs], ignore_index=True),
#                     x="tax",
#                     y="range",
#                     color="Regime",
#                     orientation="h",
#                     title="Slab-wise Tax Amount Comparison",
#                     labels={"tax": "Tax Amount (₹)", "range": "Income Slab"}
#                 )
#                 fig_slabs.update_xaxes(tickprefix="₹", separatethousands=True)
#                 st.plotly_chart(fig_slabs, use_container_width=True, key="detail_slabs")

#         # Sub-tab: Sunburst Chart
#         with detail_tabs[2]:
#             st.markdown("### Tax Components Breakdown (Sunburst Chart)")
#             components_data = {
#                 "Regime": ["Old Regime", "Old Regime", "Old Regime",
#                            "New Regime", "New Regime", "New Regime"],
#                 "Component": ["Slab Tax", "Digital Assets Tax", "Cess",
#                               "Slab Tax", "Digital Assets Tax", "Cess"],
#                 "Amount": [
#                     old_res.get("income_tax", 0.0),
#                     old_res.get("digital_assets_tax", 0.0),
#                     old_res.get("cess", 0.0),
#                     new_res.get("income_tax", 0.0),
#                     new_res.get("digital_assets_tax", 0.0),
#                     new_res.get("cess", 0.0)
#                 ]
#             }
#             df_components = pd.DataFrame(components_data)
#             fig_sunburst = px.sunburst(
#                 df_components,
#                 path=["Regime", "Component"],
#                 values="Amount",
#                 title="Tax Components Breakdown by Regime",
#                 color="Component",
#                 color_discrete_map={"Slab Tax": "#636EFA", "Digital Assets Tax": "#EF553B", "Cess": "#00CC96"}
#             )
#             fig_sunburst.update_traces(textinfo="label+percent entry")
#             st.plotly_chart(fig_sunburst, use_container_width=True, key="detail_sunburst")

#         # Sub-tab: Stacked Bar Chart
#         with detail_tabs[3]:
#             st.markdown("### Tax Components Breakdown (Stacked Bar Chart)")
#             fig_stack = px.bar(
#                 df_components,
#                 x="Regime",
#                 y="Amount",
#                 color="Component",
#                 title="Tax Components Breakdown by Regime (Stacked)",
#                 labels={"Amount": "Amount (₹)", "Regime": "Tax Regime"},
#                 barmode="stack",
#                 color_discrete_map={"Slab Tax": "#636EFA", "Digital Assets Tax": "#EF553B", "Cess": "#00CC96"}
#             )
#             fig_stack.update_yaxes(tickprefix="₹", separatethousands=True)
#             st.plotly_chart(fig_stack, use_container_width=True, key="detail_stacked")

#         # Sub-tab: Bubble Chart
#         with detail_tabs[4]:
#             st.markdown("### Tax vs. Taxable Income Bubble Chart")
#             df_bubble = pd.DataFrame({
#                 "Regime": ["Old Regime", "New Regime"],
#                 "Taxable Income": [old_taxable_inc, new_taxable_inc],
#                 "Total Tax": [old_total_tax, new_total_tax],
#                 "Net Income After Tax": [old_net_income, new_net_income]
#             })
#             fig_bubble = px.scatter(
#                 df_bubble,
#                 x="Taxable Income",
#                 y="Total Tax",
#                 size="Net Income After Tax",
#                 color="Regime",
#                 hover_name="Regime",
#                 title="Taxable Income vs Total Tax (Bubble Size = Net Income After Tax)",
#                 labels={"Taxable Income": "Taxable Income (₹)", "Total Tax": "Total Tax (₹)"}
#             )
#             fig_bubble.update_xaxes(tickprefix="₹", separatethousands=True)
#             fig_bubble.update_yaxes(tickprefix="₹", separatethousands=True)
#             st.plotly_chart(fig_bubble, use_container_width=True, key="detail_bubble")

#         # Sub-tab: Waterfall Chart
#         with detail_tabs[5]:
#             st.markdown("### Waterfall Chart")
#             old_gross_income = old_res.get("gross_income", 0.0)
#             old_total_deductions = old_res.get("total_deductions", 0.0)
#             old_slab_tax = old_res.get("income_tax", 0.0)
#             old_digital_tax = old_res.get("digital_assets_tax", 0.0)
#             old_cess = old_res.get("cess", 0.0)
#             old_net_income = old_res.get("net_income_after_tax", 0.0)
#             df_waterfall = pd.DataFrame({
#                 "label": [
#                     "Gross Income",
#                     "(-) Deductions",
#                     "(-) Slab Tax",
#                     "(-) Digital Assets Tax",
#                     "(-) Cess",
#                     "Net Income"
#                 ],
#                 "value": [
#                     old_gross_income,
#                     -old_total_deductions,
#                     -old_slab_tax,
#                     -old_digital_tax,
#                     -old_cess,
#                     old_net_income
#                 ],
#                 "measure": [
#                     "relative",
#                     "relative",
#                     "relative",
#                     "relative",
#                     "relative",
#                     "total"
#                 ]
#             })
#             fig_waterfall = go.Figure(
#                 go.Waterfall(
#                     orientation="v",
#                     measure=df_waterfall["measure"],
#                     x=df_waterfall["label"],
#                     y=df_waterfall["value"],
#                     connector={"line": {"color": "rgb(63, 63, 63)"}},
#                 )
#             )
#             fig_waterfall.update_layout(
#                 title="Old Regime: From Gross Income to Net Income (Waterfall)",
#                 yaxis=dict(tickprefix="₹", separatethousands=True)
#             )
#             st.plotly_chart(fig_waterfall, use_container_width=True, key="detail_waterfall")

#     # ----------------------------
#     # Observations & Next Steps
#     # ----------------------------
#     # st.write("---")
#     st.write("#### Observations & Final Planning")
#     try:
#         old_slab_total = df_old_slabs["tax"].sum() if "tax" in df_old_slabs.columns else 0
#         new_slab_total = df_new_slabs["tax"].sum() if "tax" in df_new_slabs.columns else 0
#     except Exception:
#         old_slab_total, new_slab_total = 0, 0
#     # st.write(f"- **Total Slab Tax (Old Regime):** ₹{old_slab_total:,.2f}")
#     # st.write(f"- **Total Slab Tax (New Regime):** ₹{new_slab_total:,.2f}")
#     # st.write("""
#     # Analyze these observations to refine your tax planning strategy.
#     # Use the interactive charts above to explore different facets of your tax liability,
#     # and identify opportunities for optimizing your overall tax burden.
#     # """)


#     # A) Observations & Final Planning Section
#     st.write("---")
#     with st.expander("Observations & Final Planning", expanded=True):
#         st.subheader("Key Observations")
        
#     # Display total slab taxes side by side
#     colA, colB = st.columns(2)
#     with colA:
#         st.metric("Total Slab Tax (Old Regime)", f"₹{old_slab_total:,.2f}")
#     with colB:
#         st.metric("Total Slab Tax (New Regime)", f"₹{new_slab_total:,.2f}")

#     st.markdown("""
#     **Interpretation**:  
#     - If the Old Regime total slab tax is significantly higher than the New Regime, 
#       the New Regime might be more beneficial (and vice versa).
#     - Consider your deductions and overall taxable income to see which regime 
#       leaves you with a lower effective tax rate.
#     """)

#     st.subheader("Next Steps for Tax Planning")
#     st.markdown("""
#     - **Review Deductions**: Ensure you’ve maximized your eligible deductions 
#       (e.g., 80C, 80D) if you’re leaning toward the Old Regime.
#     - **Evaluate Investments**: If you have limited deductions, the New Regime 
#       might be simpler and potentially cheaper.
#     - **Track Changes**: If your income or deductions change substantially, 
#       re-run the calculator to verify which regime is better.
#     """)




























































import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def setup_analytics_tab():
    """
    Analytics Tab: Displays a dashboard composed of two main sections:
      - Overview: High-level metrics and dual gauge chart comparison.
      - Details: Sub-tabs for each individual chart with an expander for interpretation.
    """
    if not st.session_state.get("calculation_done", False):
        st.info("Please calculate your tax first on the 'Tax Calculator' tab.")
        return

    # Retrieve results from session state
    new_res = st.session_state.get("new_regime_result", {})
    old_res = st.session_state.get("old_regime_result", {})

    if not new_res or not old_res:
        st.info("Need both Old & New Regime results to show analytics.")
        return

    # Extract common variables
    old_total_tax = old_res.get("total_tax", 0.0)
    new_total_tax = new_res.get("total_tax", 0.0)
    old_net_income = old_res.get("net_income_after_tax", 0.0)
    new_net_income = new_res.get("net_income_after_tax", 0.0)
    old_taxable_inc = old_res.get("taxable_income", 0.0)
    new_taxable_inc = new_res.get("taxable_income", 0.0)
    old_digital_tax = old_res.get("digital_assets_tax", 0.0)
    new_digital_tax = new_res.get("digital_assets_tax", 0.0)

    # -------------------------------------------------------------------------
    # Create Main Dashboard Tabs: Overview and Details
    # -------------------------------------------------------------------------
    main_tabs = st.tabs(["Overview", "Details"])

    # ----------------------------
    # Overview Tab
    # ----------------------------
    with main_tabs[0]:
        st.subheader("Overview")
        # Key Metrics Cards
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Taxable Income (Old)", f"₹{old_taxable_inc:,.2f}")
        col2.metric("Taxable Income (New)", f"₹{new_taxable_inc:,.2f}")
        col3.metric("Total Tax (Old)", f"₹{old_total_tax:,.2f}")
        col4.metric("Total Tax (New)", f"₹{new_total_tax:,.2f}")

        # Summary Bar Chart for Key Metrics
        df_metrics = pd.DataFrame({
            "Metric": [
                "Taxable Income",
                "Total Tax",
                "Digital Assets Tax",
                "Net Income (After Tax)"
            ],
            "Old Regime": [old_taxable_inc, old_total_tax, old_digital_tax, old_net_income],
            "New Regime": [new_taxable_inc, new_total_tax, new_digital_tax, new_net_income]
        })
        df_long = df_metrics.melt(id_vars="Metric", var_name="Regime", value_name="Value")
        fig_summary = px.bar(
            df_long,
            x="Metric",
            y="Value",
            color="Regime",
            barmode="group",
            title="Key Metrics Comparison"
        )
        fig_summary.update_yaxes(tickprefix="₹", separatethousands=True)
        st.plotly_chart(fig_summary, use_container_width=True, key="overview_summary")
        with st.expander("Interpretation"):
            st.markdown("""
            **Key Metrics Interpretation:**
            - **Taxable Income:** Total income subject to tax.
            - **Total Tax:** Overall tax liability computed.
            - **Digital Assets Tax:** Flat tax computed on digital assets.
            - **Net Income (After Tax):** Income remaining after tax deductions.
            """)

        # Dual Gauge Chart for Effective Tax Rate Comparison
        # Calculate effective tax rates
        gross_old = old_res.get("gross_income", 1)
        gross_new = new_res.get("gross_income", 1)
        effective_tax_old = (old_total_tax / gross_old * 100) if gross_old > 0 else 0
        effective_tax_new = (new_total_tax / gross_new * 100) if gross_new > 0 else 0

        # Create a dual gauge layout
        fig_dual_gauge = make_subplots(
            rows=1, cols=2,
            specs=[[{"type": "domain"}, {"type": "domain"}]]
        )
        fig_dual_gauge.add_trace(
            go.Indicator(
                mode="gauge+number",
                value=effective_tax_old,
                title={"text": "Old Regime"},
                gauge={
                    "axis": {"range": [0, 40]},
                    "bar": {"color": "blue"}
                },
                number={"font": {"size": 36}}
            ),
            row=1, col=1
        )
        fig_dual_gauge.add_trace(
            go.Indicator(
                mode="gauge+number",
                value=effective_tax_new,
                title={"text": "New Regime"},
                gauge={
                    "axis": {"range": [0, 40]},
                    "bar": {"color": "green"}
                },
                number={"font": {"size": 36}}
            ),
            row=1, col=2
        )
        fig_dual_gauge.update_layout(
            title_text="Effective Tax Rate Comparison (Dual Gauge)",
            margin=dict(l=40, r=40)
        )
        st.plotly_chart(fig_dual_gauge, use_container_width=True, key="overview_dual_gauge")
        with st.expander("Gauge Interpretation"):
            st.markdown("""
            **Gauge Chart Interpretation:**
            - Each gauge displays the effective tax rate (Total Tax ÷ Gross Income × 100) for a regime.
            - A lower value indicates a more favorable tax situation.
            - Compare the dials side by side to see which regime taxes a lower percentage of your income.
            """)

    # ----------------------------
    # Details Tab with Sub-Tabs for Each Chart
    # ----------------------------
    with main_tabs[1]:
        detail_tabs = st.tabs([
            "Key Metrics", "Slab Breakdown", "Sunburst", "Stacked", "Bubble", "Funnel"
        ])

        # Sub-tab: Key Metrics (reuse summary bar chart)
        with detail_tabs[0]:
            st.markdown("### Key Metrics Comparison")
            st.plotly_chart(fig_summary, use_container_width=True, key="detail_keymetrics")
            with st.expander("Interpretation"):
                st.markdown("""
                **Key Metrics Chart Interpretation:**
                - The bar chart compares key metrics between the Old and New Regimes.
                - It provides a quick visual comparison of taxable income, total tax, digital assets tax, and net income.
                """)

        # Sub-tab: Slab Breakdown
        with detail_tabs[1]:
            st.markdown("### Slab Tax Breakdown Comparison")
            old_slabs = old_res.get("slab_breakup", [])
            new_slabs = new_res.get("slab_breakup", [])
            if not old_slabs or not new_slabs:
                st.info("Slab breakdown data not available in one or both regimes.")
            else:
                df_old_slabs = pd.DataFrame(old_slabs)
                df_old_slabs["Regime"] = "Old Regime"
                df_new_slabs = pd.DataFrame(new_slabs)
                df_new_slabs["Regime"] = "New Regime"
                # Use original column names: 'range' for income slab and 'tax' for tax amount.
                fig_slabs = px.bar(
                    pd.concat([df_old_slabs, df_new_slabs], ignore_index=True),
                    x="tax",
                    y="range",
                    color="Regime",
                    orientation="h",
                    title="Slab-wise Tax Amount Comparison",
                    labels={"tax": "Tax Amount (₹)", "range": "Income Slab"}
                )
                fig_slabs.update_xaxes(tickprefix="₹", separatethousands=True)
                st.plotly_chart(fig_slabs, use_container_width=True, key="detail_slabs")
                with st.expander("Interpretation"):
                    st.markdown("""
                    **Slab Breakdown Interpretation:**
                    - Each horizontal bar represents an income slab and its corresponding tax amount.
                    - This chart shows how much tax is contributed by each income range in both regimes.
                    """)

        # Sub-tab: Sunburst Chart
        with detail_tabs[2]:
            st.markdown("### Tax Components Breakdown (Sunburst Chart)")
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
            st.plotly_chart(fig_sunburst, use_container_width=True, key="detail_sunburst")
            with st.expander("Interpretation"):
                st.markdown("""
                **Sunburst Chart Interpretation:**
                - The sunburst chart breaks down the total tax into its components (slab tax, digital assets tax, and cess).
                - Hovering over segments shows the percentage contribution of each component.
                """)

        # Sub-tab: Stacked Bar Chart
        with detail_tabs[3]:
            st.markdown("### Tax Components Breakdown (Stacked Bar Chart)")
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
            st.plotly_chart(fig_stack, use_container_width=True, key="detail_stacked")
            with st.expander("Interpretation"):
                st.markdown("""
                **Stacked Bar Chart Interpretation:**
                - This chart stacks tax components for each regime to show their cumulative contribution.
                - It allows direct comparison of the composition of tax between the two regimes.
                """)

        # Sub-tab: Bubble Chart
        with detail_tabs[4]:
            st.markdown("### Tax vs. Taxable Income Bubble Chart")
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
            st.plotly_chart(fig_bubble, use_container_width=True, key="detail_bubble")
            with st.expander("Interpretation"):
                st.markdown("""
                **Bubble Chart Interpretation:**
                - The bubble chart compares taxable income against total tax for each regime.
                - The bubble size represents net income after tax, providing insight into the overall tax burden.
                """)

        # Sub-tab: Funnel Chart (Replacing Waterfall)
       # Inside your Details tab sub-tabs, replace the existing "Waterfall Chart" sub-tab
    # with the following "Funnel Chart" sub-tab code:

    with detail_tabs[5]:
        st.markdown("### Tax Calculation Funnel")
        # Toggle option to choose which regime's funnel to display
        funnel_option = st.radio(
            "Select Regime for Funnel Chart",
            options=["Old Regime", "New Regime", "Both"],
            key="funnel_toggle"
        )
        
        # --- Build Old Regime Funnel Chart ---
        if funnel_option in ["Old Regime", "Both"]:
            old_gross_income = old_res.get("gross_income", 0.0)
            old_total_deductions = old_res.get("total_deductions", 0.0)
            old_taxable_inc = old_res.get("taxable_income", 0.0)
            old_tax = old_res.get("income_tax", 0.0)
            old_total_tax = old_res.get("total_tax", 0.0)
            fig_funnel_old = go.Figure(go.Funnel(
                y=["Gross Income", "Deductions", "Taxable Income", "Income Tax", "Total Tax"],
                x=[old_gross_income, old_total_deductions, old_taxable_inc, old_tax, old_total_tax],
                textposition="inside",
                textinfo="value+percent initial"
            ))
            fig_funnel_old.update_layout(title="Tax Calculation Funnel (Old Regime)")
        
        # --- Build New Regime Funnel Chart ---
        if funnel_option in ["New Regime", "Both"]:
            new_gross_income = new_res.get("gross_income", 0.0)
            new_standard_deduction = new_res.get("standard_deduction", 0.0)
            new_taxable_inc = new_res.get("taxable_income", 0.0)
            new_tax = new_res.get("income_tax", 0.0)
            new_total_tax = new_res.get("total_tax", 0.0)
            fig_funnel_new = go.Figure(go.Funnel(
                y=["Gross Income", "Standard Deduction", "Taxable Income", "Income Tax", "Total Tax"],
                x=[new_gross_income, new_standard_deduction, new_taxable_inc, new_tax, new_total_tax],
                textposition="inside",
                textinfo="value+percent initial"
            ))
            fig_funnel_new.update_layout(title="Tax Calculation Funnel (New Regime)")
        
        # --- Display based on toggle selection ---
        if funnel_option == "Old Regime":
            st.plotly_chart(fig_funnel_old, use_container_width=True, key="funnel_old")
        elif funnel_option == "New Regime":
            st.plotly_chart(fig_funnel_new, use_container_width=True, key="funnel_new")
        elif funnel_option == "Both":
            col1, col2 = st.columns(2)
            with col1:
                st.plotly_chart(fig_funnel_old, use_container_width=True, key="funnel_old_both")
            with col2:
                st.plotly_chart(fig_funnel_new, use_container_width=True, key="funnel_new_both")
        
        with st.expander("Funnel Chart Interpretation"):
            st.markdown("""
            **Funnel Chart Interpretation:**
            - The funnel chart visually represents how the income is "filtered" through the tax calculation process.
            - For the Old Regime, it shows stages such as gross income, deductions, taxable income, income tax, and total tax.
            - For the New Regime, it includes the standard deduction stage instead of generic deductions.
            - Use the toggle above to compare the processes side by side.
            """)

    # ----------------------------
    # Observations & Final Planning
    # ----------------------------
    st.write("---")
    with st.expander("Observations & Final Planning", expanded=True):
        st.subheader("Key Observations")
        # Use columns to display metrics side by side
        colA, colB = st.columns(2)
        with colA:
            st.metric("Total Slab Tax (Old Regime)", f"₹{df_old_slabs['tax'].sum() if 'tax' in df_old_slabs.columns else 0:,.2f}")
        with colB:
            st.metric("Total Slab Tax (New Regime)", f"₹{df_new_slabs['tax'].sum() if 'tax' in df_new_slabs.columns else 0:,.2f}")

        st.markdown("""
        **Interpretation**:  
        - Compare the total slab tax between regimes to see which structure is more tax-efficient.
        .
                    
        - A lower slab tax typically indicates a more favorable regime for your specific income profile.
        """)

        st.subheader("Next Steps for Tax Planning")
        st.markdown("""
        - **Review Deductions**: Ensure you’ve maximized your eligible deductions (e.g., 80C, 80D) if you’re leaning toward the Old Regime.
        - **Evaluate Investments**: If you have limited deductions, the New Regime might be simpler and potentially cheaper.
        - **Monitor Changes**: Re-run the calculator if your income or deductions change substantially.
        """)

