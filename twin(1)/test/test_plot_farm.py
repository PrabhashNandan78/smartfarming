from FarmTwin.farm import FarmTwin
from FarmTwin.geometry.state import FarmGeometry
from Visualization.encoding import encode_plant_visual
from Visualization.plot2d import plot_farm

geometry = FarmGeometry(
    num_rows=5,
    num_cols=5,
    row_spacing=0.5,
    col_spacing=0.5
)

farm = FarmTwin("FARM_001", geometry)
farm.advance_time(days=10)

snapshot = farm.snapshot()

encoded_plants = [
    encode_plant_visual(p) for p in snapshot["plants"]
]

plot_farm(encoded_plants, title=f"Farm at Day {snapshot['day']}")
