# Supply Chain Network Optimizer

A decision-support application that optimizes warehouse-to-customer allocation, analyzes transportation costs, forecasts demand, and evaluates supply chain scenarios using Python, Streamlit, and Google OR-Tools.

---

## Overview

Supply chain teams must decide:

- Which warehouses should serve which customers?
- How can transportation costs be minimized?
- Can the current network handle demand changes?
- What happens under different business scenarios?

This project solves a simplified strategic network planning problem by combining:

- Operations Research
- Demand Analytics
- Forecasting
- Interactive Business Intelligence

---

# Features

## 1. Network Optimization

Uses Google OR-Tools to optimize warehouse-to-customer assignments.

The model considers:

- Warehouse capacity constraints
- Customer demand requirements
- Transportation distance costs

Outputs:

- Optimal customer allocation
- Warehouse utilization
- Transportation cost analysis

---

## 2. Demand Forecasting

Forecasts future demand using historical demand patterns.

Capabilities:

- Historical demand analysis
- Future demand projection
- Trend visualization

---

## 3. Scenario Analysis

Evaluate supply chain decisions under changing conditions.

Scenarios:

- Baseline network
- Demand increase (+20%)
- Transportation cost increase (+15%)

---

## 4. Interactive Dashboard

Provides:

- Network KPIs
- Warehouse demand allocation
- Geographic warehouse visualization
- Optimization results

---
# Project Architecture

Data Generation
|
|
v
CSV Datasets
|
|
+----------------+
| |
v v
Forecasting Optimization Engine
| |
| |
+----------------+
|
v
Streamlit Dashboard

---

# Tech Stack

## Programming

- Python

## Analytics

- Pandas
- NumPy
- Plotly

## Optimization

- Google OR-Tools

## Forecasting

- Statsmodels

## Application

- Streamlit

---

# Project Structure

├── app.py

├── pages/
│ ├── Upload Data
│ ├── Demand Forecasting
│ ├── Network Optimization
│ ├── Scenario Analysis
│ └── Dashboard

├── utils/
│ ├── data_generator.py
│ ├── optimizer.py
│ ├── forecasting.py
│ └── scenarios.py

├── data/
│ ├── warehouses.csv
│ ├── customers.csv
│ └── demand_history.csv

---

# Running the Application

Clone the repository:

git clone <repository-url>

Create environment: python -m venv .venv

Activate:
Windows: .venv\Scripts\activate

Install dependencies: pip install -r requirements.txt

Run: streamlit run app.py

---

## Generate Sample Data

The project includes a synthetic data generator.

Run:

python utils/data_generator.py

This creates:

- warehouses.csv
- customers.csv
- demand_history.csv

--- 

# Optimization Model

The optimization problem is formulated as:

Minimize: Total Transportation Cost
Subject to: Each customer receives supply from one warehouse, Warehouse capacity cannot be exceeded


Decision variable:
x(w,c)
1 = warehouse w serves customer c
0 = otherwise


---

# Example Business Questions Answered

✔ Which warehouse should serve each customer?

✔ What is the expected transportation cost?

✔ How much demand does each warehouse handle?

✔ How does the network perform under increased demand?

---

# Future Improvements

Potential extensions:

- Multi-product optimization
- Inventory planning
- Vehicle routing
- Real-world geographic distance APIs
- Additional supply chain constraints


