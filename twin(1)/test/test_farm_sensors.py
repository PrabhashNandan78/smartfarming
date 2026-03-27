from FarmTwin.farm import FarmTwin
from FarmTwin.geometry.state import FarmGeometry

geometry = FarmGeometry(
    num_rows=4,
    num_cols=6,
    row_spacing=0.5,
    col_spacing=0.5
)

farm = FarmTwin("FARM_002", geometry)

readings = farm.read_sensors()

for r in readings:
    print(r)
