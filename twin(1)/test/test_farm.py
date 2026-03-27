from FarmTwin.farm import FarmTwin
from FarmTwin.geometry.state import FarmGeometry

geometry = FarmGeometry(
    num_rows=2,
    num_cols=3,
    row_spacing=0.5,
    col_spacing=0.5
)

farm = FarmTwin(
    farm_id="FARM_001",
    geometry=geometry
)

farm.advance_time(days=5)
snap = farm.snapshot()

print(f"Day: {snap['day']}")
print(f"Number of plants: {len(snap['plants'])}")
print(snap['plants'][0])
