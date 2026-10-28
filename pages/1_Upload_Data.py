import streamlit as st
import pandas as pd

st.set_page_config(page_title="Upload Data")

st.title("Upload Data")
st.write("Load and inspect the datasets used by the optimizer.")

# Load data
warehouses = pd.read_csv("data/warehouses.csv")
customers = pd.read_csv("data/customers.csv")
demand = pd.read_csv("data/demand_history.csv")

st.success("All datasets loaded successfully.")

# -------------------------
# Dataset Summary
# -------------------------

st.header("Dataset Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Warehouses", warehouses.shape[0])

with col2:
    st.metric("Customers", customers.shape[0])

with col3:
    st.metric("Demand Records", demand.shape[0])

# -------------------------
# Preview Data
# -------------------------

st.header("Warehouse Data")
st.dataframe(warehouses, use_container_width=True)

st.header("Customer Data")
st.dataframe(customers.head(10), use_container_width=True)

st.header("Demand History")
st.dataframe(demand.head(10), use_container_width=True)