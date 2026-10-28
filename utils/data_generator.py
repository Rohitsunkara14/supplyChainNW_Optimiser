import pandas as pd
import random
from faker import Faker
from pathlib import Path
from datetime import datetime


# Create Faker object
fake = Faker()


# Find project folders
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


# Warehouse locations
WAREHOUSES = [
    {
        "warehouse_id": "W001",
        "warehouse_name": "Dallas DC",
        "city": "Dallas",
        "state": "TX",
        "latitude": 32.7767,
        "longitude": -96.7970,
    },
    {
        "warehouse_id": "W002",
        "warehouse_name": "Chicago DC",
        "city": "Chicago",
        "state": "IL",
        "latitude": 41.8781,
        "longitude": -87.6298,
    },
    {
        "warehouse_id": "W003",
        "warehouse_name": "Atlanta DC",
        "city": "Atlanta",
        "state": "GA",
        "latitude": 33.7490,
        "longitude": -84.3880,
    },
    {
        "warehouse_id": "W004",
        "warehouse_name": "Phoenix DC",
        "city": "Phoenix",
        "state": "AZ",
        "latitude": 33.4484,
        "longitude": -112.0740,
    },
    {
        "warehouse_id": "W005",
        "warehouse_name": "Seattle DC",
        "city": "Seattle",
        "state": "WA",
        "latitude": 47.6062,
        "longitude": -122.3321,
    },
]

CUSTOMER_CITIES = [
    {
        "city": "Austin",
        "state": "TX",
        "latitude": 30.2672,
        "longitude": -97.7431,
    },
    {
        "city": "Houston",
        "state": "TX",
        "latitude": 29.7604,
        "longitude": -95.3698,
    },
    {
        "city": "Denver",
        "state": "CO",
        "latitude": 39.7392,
        "longitude": -104.9903,
    },
    {
        "city": "Miami",
        "state": "FL",
        "latitude": 25.7617,
        "longitude": -80.1918,
    },
    {
        "city": "Portland",
        "state": "OR",
        "latitude": 45.5152,
        "longitude": -122.6784,
    },
    {
        "city": "New York",
        "state": "NY",
        "latitude": 40.7128,
        "longitude": -74.0060,
    },
    {
        "city": "Los Angeles",
        "state": "CA",
        "latitude": 34.0522,
        "longitude": -118.2437,
    },
    {
        "city": "Boston",
        "state": "MA",
        "latitude": 42.3601,
        "longitude": -71.0589,
    },
    {
        "city": "Charlotte",
        "state": "NC",
        "latitude": 35.2271,
        "longitude": -80.8431,
    },
    {
        "city": "Las Vegas",
        "state": "NV",
        "latitude": 36.1699,
        "longitude": -115.1398,
    },
]

# Generate warehouse dataset
def generate_warehouses():

    warehouse_data = []

    for warehouse in WAREHOUSES:

        warehouse["capacity"] = random.randint(50000, 80000)

        warehouse["fixed_cost"] = random.randint(350000, 700000)

        warehouse["status"] = "Open"

        warehouse_data.append(warehouse.copy())

    return pd.DataFrame(warehouse_data)

def generate_customers(number_of_customers=500):

    customers = []

    for i in range(number_of_customers):

        location = random.choice(CUSTOMER_CITIES)

        customer = {
            "customer_id": f"C{i+1:04d}",
            "customer_name": f"{location['city']} Retail Center {i+1}",
            "city": location["city"],
            "state": location["state"],
            "latitude": location["latitude"],
            "longitude": location["longitude"],
        }

        customers.append(customer)

    return pd.DataFrame(customers)

# Save warehouse dataset
def save_warehouses():

    df = generate_warehouses()

    output_file = DATA_DIR / "warehouses.csv"

    df.to_csv(output_file, index=False)

    print(f"Created {output_file}")

def save_customers():

    df = generate_customers()

    output_file = DATA_DIR / "customers.csv"

    df.to_csv(output_file, index=False)

    print(f"Created {output_file}")

def generate_demand_history(months=24):

    demand_data = []

    customers = generate_customers()

    dates = pd.date_range(
        end=datetime.today(),
        periods=months,
        freq="MS"
    )

    for _, customer in customers.iterrows():

        base_demand = random.randint(300, 800)

        seasonal_factor = random.uniform(0.9, 1.1)

        for date in dates:

            monthly_variation = random.randint(-50, 50)

            demand = int(
                base_demand * seasonal_factor + monthly_variation
            )

            demand = max(50, demand)

            demand_data.append({
                "month": date.strftime("%Y-%m"),
                "customer_id": customer["customer_id"],
                "demand": demand
            })

    return pd.DataFrame(demand_data)

def save_demand_history():

    df = generate_demand_history()

    output_file = DATA_DIR / "demand_history.csv"

    df.to_csv(output_file, index=False)

    print(f"Created {output_file}")

if __name__ == "__main__":

    save_warehouses()

    save_customers()

    save_demand_history()