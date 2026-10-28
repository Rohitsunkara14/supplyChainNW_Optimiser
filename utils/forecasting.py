import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing


def generate_forecast(
    demand_file="data/demand_history.csv",
    forecast_months=6
):

    demand = pd.read_csv(demand_file)


    # Aggregate all customer demand
    monthly_demand = (
        demand
        .groupby("month")["demand"]
        .sum()
        .reset_index()
    )


    monthly_demand["month"] = pd.to_datetime(
        monthly_demand["month"]
    )


    monthly_demand = (
        monthly_demand
        .sort_values("month")
    )


    model = ExponentialSmoothing(
        monthly_demand["demand"],
        trend="add",
        seasonal=None
    )


    fitted_model = model.fit()


    future = fitted_model.forecast(
        forecast_months
    )


    forecast_df = pd.DataFrame(
        {
            "month": future.index,
            "forecast_demand": future.values
        }
    )


    return monthly_demand, forecast_df