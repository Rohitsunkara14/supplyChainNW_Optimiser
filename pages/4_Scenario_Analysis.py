import streamlit as st
import pandas as pd
import plotly.express as px

from utils.scenarios import (
    apply_scenario,
    calculate_metrics
)


st.set_page_config(
    page_title="Scenario Analysis",
)


st.title("Scenario Analysis")


if "optimization_results" not in st.session_state:

    st.warning(
        "Run optimization first."
    )

    st.stop()


results = st.session_state[
    "optimization_results"
]


scenario = st.selectbox(
    "Select Scenario",
    [
        "Baseline",
        "Demand Increase +20%",
        "Transportation Cost +15%"
    ]
)


if scenario == "Baseline":

    scenario_results = results

else:

    scenario_results = apply_scenario(
        results,
        scenario
    )


metrics = calculate_metrics(
    scenario_results
)


st.divider()


st.subheader(
    "Scenario Results"
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Demand",
        f"{metrics['Total Demand']:,.0f}"
    )


with col2:

    st.metric(
        "Transportation Cost",
        f"${metrics['Transportation Cost']:,.0f}"
    )


with col3:

    st.metric(
        "Customers Served",
        metrics["Customers Served"]
    )


with col4:

    st.metric(
        "Warehouses Used",
        metrics["Warehouses Used"]
    )


st.divider()


st.subheader(
    "Allocation Details"
)


st.dataframe(
    scenario_results,
    use_container_width=True
)