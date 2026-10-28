import streamlit as st
import pandas as pd

from utils.optimizer import optimize_network


st.set_page_config(
    page_title="Network Optimization",
)


st.title("Network Optimization")

st.write(
    """
    Optimize warehouse-to-customer assignments using
    Google OR-Tools.
    """
)


if st.button("Run Optimization"):

    with st.spinner("Running optimization model..."):

        try:

            results = optimize_network()

            st.success("Optimization completed successfully!")

            st.session_state["optimization_results"] = results


        except Exception as e:

            st.error(f"Optimization failed: {e}")



if "optimization_results" in st.session_state:

    results = st.session_state["optimization_results"]


    st.divider()

    st.subheader("Optimization Summary")


col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        "Customer Assignments",
        len(results)
    )


with col2:
    st.metric(
        "Warehouses Used",
        results["warehouse_id"].nunique()
    )


with col3:

    total_cost = results["transportation_cost"].sum()

    st.metric(
        "Transportation Cost",
        f"${total_cost:,.0f}"
    )

    st.divider()


    st.subheader("Allocation Results")

    st.subheader("Warehouse Utilization")


utilization = (
    results
    .groupby("warehouse_id")["demand"]
    .sum()
    .reset_index()
)


warehouse_capacity = pd.read_csv(
    "data/warehouses.csv"
)


utilization = utilization.merge(
    warehouse_capacity[
        ["warehouse_id", "capacity"]
    ],
    on="warehouse_id"
)


utilization["utilization_%"] = (
    utilization["demand"]
    /
    utilization["capacity"]
    *
    100
)


st.dataframe(
    utilization,
    use_container_width=True
)

