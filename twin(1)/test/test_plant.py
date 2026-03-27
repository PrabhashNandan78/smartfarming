from PlantTwin.plant import PlantTwin

plant = PlantTwin(
    plant_id="P_001",
    row_index=0,
    col_index=0,
    x_coord=0.0,
    y_coord=0.0
)

plant.update_state(
    growth_state={"days_after_sowing": 10, "LAI": 0.8},
    stress_state={"water_stress": 0.2},
    health_state={"health_score": 0.95}
)

snap = plant.snapshot()
print(snap)
