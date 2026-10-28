import gradio as gr
import pandas as pd

from utils.optimizer import optimize_network
from utils.forecasting import generate_forecast


def run_optimizer():

    results = optimize_network()

    total_cost = results["transportation_cost"].sum()

    summary = f"""
    Optimization Completed

    Customers Assigned: {len(results)}

    Warehouses Used: {results['warehouse_id'].nunique()}

    Total Demand Served: {results['demand'].sum():,.0f}

    Transportation Cost: ${total_cost:,.0f}
    """

    return summary, results.head(20)



def run_forecast():

    history, forecast = generate_forecast()

    return forecast



with gr.Blocks() as demo:

    gr.Markdown(
        """
        # Supply Chain Network Optimizer

        Strategic network planning platform using:
        - Python
        - OR-Tools
        - Demand Forecasting
        - Scenario Analysis
        """
    )


    with gr.Tab("Network Optimization"):

        optimize_button = gr.Button(
            "Run Optimization"
        )

        summary_output = gr.Textbox(
            label="Optimization Summary"
        )

        table_output = gr.Dataframe(
            label="Allocation Results"
        )


        optimize_button.click(
            run_optimizer,
            outputs=[
                summary_output,
                table_output
            ]
        )


    with gr.Tab("Demand Forecast"):

        forecast_button = gr.Button(
            "Generate Forecast"
        )

        forecast_output = gr.Dataframe()


        forecast_button.click(
            run_forecast,
            outputs=forecast_output
        )


demo.launch()