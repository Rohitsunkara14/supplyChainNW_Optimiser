import streamlit as st
import plotly.express as px

from utils.forecasting import generate_forecast


st.set_page_config(
    page_title="Demand Forecasting",
)


st.title("Demand Forecasting")


st.write(
    """
    Forecast future customer demand using historical demand patterns.
    """
)


if st.button("Generate Forecast"):

    with st.spinner("Creating forecast..."):

        history, forecast = generate_forecast()


        st.session_state["history"] = history

        st.session_state["forecast"] = forecast


        st.success(
            "Forecast generated successfully!"
        )



if "forecast" in st.session_state:


    history = st.session_state["history"]

    forecast = st.session_state["forecast"]


    st.divider()


    st.subheader(
        "Demand Forecast"
    )


    fig = px.line()


    fig.add_scatter(
        x=history["month"],
        y=history["demand"],
        name="Historical Demand"
    )


    fig.add_scatter(
        x=forecast["month"],
        y=forecast["forecast_demand"],
        name="Forecast"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    st.subheader(
        "Forecast Table"
    )


    st.dataframe(
        forecast,
        use_container_width=True
    )