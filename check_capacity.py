import pandas as pd


warehouses = pd.read_csv("data/warehouses.csv")
demand = pd.read_csv("data/demand_history.csv")


total_capacity = warehouses["capacity"].sum()


customer_demand = (
    demand.groupby("customer_id")["demand"]
    .mean()
)


total_demand = customer_demand.sum()

max_customer = customer_demand.max()


print("Warehouse capacities:")
print(warehouses[["warehouse_id", "capacity"]])

print("\nTotal capacity:")
print(total_capacity)

print("\nTotal demand:")
print(total_demand)

print("\nLargest customer demand:")
print(max_customer)