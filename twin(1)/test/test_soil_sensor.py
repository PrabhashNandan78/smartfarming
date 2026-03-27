from FarmTwin.farm import FarmTwin
from FarmTwin.geometry.state import FarmGeometry
from SensorTwin.soil_moisture.sensor import SoilMoistureSensorTwin

geometry = FarmGeometry(3, 5, 0.5, 0.5)
farm = FarmTwin("FARM_001", geometry)

sensor = SoilMoistureSensorTwin(
    sensor_id="SM_ROW_1",
    attached_row=1
)

snapshot = farm.snapshot()
reading = sensor.read(snapshot)

print(reading)
