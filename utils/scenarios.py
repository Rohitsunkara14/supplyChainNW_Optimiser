import pandas as pd


def apply_scenario(
    results,
    scenario
):

    scenario_results = results.copy()


    if scenario == "Demand Increase +20%":

        scenario_results["demand"] = (
            scenario_results["demand"] * 1.20
        )


    elif scenario == "Transportation Cost +15%":

        scenario_results["transportation_cost"] = (
            scenario_results["transportation_cost"] * 1.15
        )


    return scenario_results



def calculate_metrics(results):

    metrics = {

        "Total Demand":
            results["demand"].sum(),

        "Transportation Cost":
            results["transportation_cost"].sum(),

        "Customers Served":
            results["customer_id"].nunique(),

        "Warehouses Used":
            results["warehouse_id"].nunique()

    }


    return metrics