from FarmTwin.farm import FarmTwin
from FarmTwin.geometry.state import FarmGeometry

geometry = FarmGeometry(4, 6, 0.5, 0.5)
farm = FarmTwin("FARM_003", geometry)

farm.infer_water_stress()

for plant in farm.plants[:6]:
    print(
        plant.plant_id.plant_id,
        plant.stress_state.water_stress
    )
