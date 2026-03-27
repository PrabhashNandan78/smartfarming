from FarmTwin.farm import FarmTwin
from FarmTwin.geometry.state import FarmGeometry
from Visualization.encoding import encode_plant_visual

geometry = FarmGeometry(2, 3, 0.5, 0.5)
farm = FarmTwin("FARM_001", geometry)

farm.advance_time(days=5)
snap = farm.snapshot()

encoded = encode_plant_visual(snap["plants"][0])
print(encoded)
