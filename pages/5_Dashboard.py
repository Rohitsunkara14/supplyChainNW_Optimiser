import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Dashboard",
    layout="wide"
)


st.title("Supply Chain Optimization Dashboard")


if "optimization_results" not in st.session_state:

    st.warning(
        "Run the optimization model first from the Network Optimization page."
    )

    st.stop()


results = st.session_state["optimization_results"]


warehouses = pd.read_csv(
    "data/warehouses.csv"
)

customers = pd.read_csv(
    "data/customers.csv"
)


# ----------------------------
# KPI Section
# ----------------------------

st.subheader("Key Performance Indicators")


total_customers = results["customer_id"].nunique()

total_warehouses = results["warehouse_id"].nunique()

total_cost = results["transportation_cost"].sum()

total_demand = results["demand"].sum()


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "Customers Served",
        total_customers
    )


with col2:
    st.metric(
        "Warehouses Used",
        total_warehouses
    )


with col3:
    st.metric(
        "Total Demand",
        f"{total_demand:,.0f}"
    )


with col4:
    st.metric(
        "Transportation Cost",
        f"${total_cost:,.0f}"
    )


# ----------------------------
# Warehouse Demand Chart
# ----------------------------

st.divider()

st.subheader("Demand Served by Warehouse")


warehouse_summary = (
    results
    .groupby("warehouse_id")["demand"]
    .sum()
    .reset_index()
)


fig = px.bar(
    warehouse_summary,
    x="warehouse_id",
    y="demand",
    title="Customer Demand Allocation"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


# ----------------------------
# Warehouse Map
# ----------------------------

st.divider()

st.subheader("Warehouse Locations")


fig_map = px.scatter_mapbox(
    warehouses,
    lat="latitude",
    lon="longitude",
    hover_name="warehouse_name",
    zoom=3,
    height=500
)


fig_map.update_layout(
    mapbox_style="open-street-map"
)


st.plotly_chart(
    fig_map,
    use_container_width=True
)


# ----------------------------
# Results Table
# ----------------------------

st.divider()

st.subheader("Optimization Results")

st.dataframe(
    results,
    use_container_width=True
)