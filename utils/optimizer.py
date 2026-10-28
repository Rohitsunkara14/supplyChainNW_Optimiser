import pandas as pd
import numpy as np
from ortools.linear_solver import pywraplp


def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate approximate distance between two coordinates.
    """

    return np.sqrt(
        (lat1 - lat2) ** 2 +
        (lon1 - lon2) ** 2
    ) * 69


def optimize_network(
        warehouses_file="data/warehouses.csv",
        customers_file="data/customers.csv",
        demand_file="data/demand_history.csv"
):

    # Load datasets

    warehouses = pd.read_csv(warehouses_file)

    customers = pd.read_csv(customers_file)

    demand = pd.read_csv(demand_file)


    # Calculate average customer demand

    customer_demand = (
        demand
        .groupby("customer_id")["demand"]
        .mean()
        .reset_index()
    )


    customers = customers.merge(
        customer_demand,
        on="customer_id"
    )


    # Create optimization solver

    solver = pywraplp.Solver.CreateSolver(
        "SCIP"
    )


    if not solver:
        raise Exception(
            "Solver unavailable"
        )


    # Decision variables

    routes = {}

    for w in warehouses.itertuples():

        for c in customers.itertuples():

            routes[w.warehouse_id, c.customer_id] = (
                solver.BoolVar(
                    f"{w.warehouse_id}_{c.customer_id}"
                )
            )


    # Objective function

    objective = solver.Objective()


    for w in warehouses.itertuples():

        for c in customers.itertuples():

            distance = calculate_distance(
                w.latitude,
                w.longitude,
                c.latitude,
                c.longitude
            )


            transportation_cost = distance * 2


            objective.SetCoefficient(
                routes[w.warehouse_id, c.customer_id],
                transportation_cost
            )


    objective.SetMinimization()


    # Constraint 1:
    # Every customer must have one warehouse

    for c in customers.itertuples():

        solver.Add(
            sum(
                routes[w.warehouse_id, c.customer_id]
                for w in warehouses.itertuples()
            ) == 1
        )


    # Constraint 2:
    # Warehouse capacity

    for w in warehouses.itertuples():

        solver.Add(
            sum(
                routes[w.warehouse_id, c.customer_id]
                *
                c.demand

                for c in customers.itertuples()

            )

            <= w.capacity
        )


    # Solve

    status = solver.Solve()


    if status != pywraplp.Solver.OPTIMAL:

        raise Exception(
            "No optimal solution found"
        )


    # Collect results

    results = []


    for w in warehouses.itertuples():

        for c in customers.itertuples():

            if routes[w.warehouse_id, c.customer_id].solution_value() == 1:


                results.append({

                    "warehouse_id":
                    w.warehouse_id,

                    "customer_id":
                    c.customer_id,

                    "customer_city":
                    c.city,

                    "demand":
                    round(c.demand,2)

                })


    results_df = pd.DataFrame(results)


# Calculate transportation cost

costs = []

for _, row in results_df.iterrows():

    warehouse = warehouses[
        warehouses["warehouse_id"] == row["warehouse_id"]
    ].iloc[0]


    customer = customers[
        customers["customer_id"] == row["customer_id"]
    ].iloc[0]


    distance = calculate_distance(
        warehouse["latitude"],
        warehouse["longitude"],
        customer["latitude"],
        customer["longitude"]
    )


    transportation_cost = distance * 2


    costs.append(transportation_cost)


results_df["transportation_cost"] = costs


return results_df