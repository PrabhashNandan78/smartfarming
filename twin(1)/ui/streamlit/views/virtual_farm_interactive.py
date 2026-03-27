import plotly.express as px
import streamlit as st
import pandas as pd


def render_virtual_farm_interactive(snapshot):
    """
    Interactive virtual farm with hover + click
    """

    records = []
    for p in snapshot["plants"]:
        records.append({
            "plant_id": p["plant_id"],
            "x": p["spatial"]["x_coord"],
            "y": p["spatial"]["y_coord"],
            "LAI": p["growth_state"]["LAI"],
            "water_stress": p["stress_state"]["water_stress"],
            "health": p["health_state"]["health_score"],
            "color": "Healthy" if p["stress_state"]["water_stress"] < 0.3 else "Stressed",
            "size": max(p["growth_state"]["LAI"], 0.05)
        })

    df = pd.DataFrame(records)

    fig = px.scatter(
        df,
        x="x",
        y="y",
        size="size",
        color="color",
        hover_name="plant_id",
        hover_data=["LAI", "water_stress", "health"],
        title="Interactive Virtual Farm View",
        size_max=40
    )

    fig.update_layout(
        plot_bgcolor="#0e1117",
        paper_bgcolor="#0e1117",
        font_color="white",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
    )

    selected = st.plotly_chart(
        fig,
        use_container_width=True,
        on_select="rerun"
    )

    return selected
