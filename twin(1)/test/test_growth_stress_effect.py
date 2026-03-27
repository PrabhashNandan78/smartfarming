from FarmTwin.farm import FarmTwin
from FarmTwin.geometry.state import FarmGeometry

geometry = FarmGeometry(2, 4, 0.5, 0.5)
farm = FarmTwin("FARM_004", geometry)

# Force artificial drought on row 0
for sensor in farm.sensors:
    if sensor.attached_row == 0:
        sensor.base_moisture = 28.0  # severe stress
    else:
        sensor.base_moisture = 45.0  # no stress

farm.advance_time(days=10)

for plant in farm.plants:
    print(
        plant.plant_id.plant_id,
        "row:", plant.spatial.row_index,
        "LAI:", round(plant.growth_state.LAI, 2),
        "biomass:", round(plant.growth_state.biomass, 2),
        "stress:", round(plant.stress_state.water_stress, 2)
    )
