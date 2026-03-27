import time
from Visualization.encoding import encode_plant_visual
from Visualization.plot2d import plot_farm


def replay_farm_over_time(
    farm,
    days,
    delay=0.5,
    title_prefix="Farm State at Day"
):
    """
    Frame-by-frame replay of farm evolution.

    farm  : FarmTwin instance
    days  : number of days to simulate
    delay : seconds between frames
    """

    for day in range(1, days + 1):
        farm.advance_time(days=1)

        snapshot = farm.snapshot()

        encoded_plants = [
            encode_plant_visual(p)
            for p in snapshot["plants"]
        ]

        plot_farm(
            encoded_plants,
            title=f"{title_prefix} {snapshot['day']}"
        )

        time.sleep(delay)
