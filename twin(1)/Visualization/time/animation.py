import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Visualization.encoding import encode_plant_visual


def animate_farm(history_snapshots, interval=600):
    """
    Animate farm evolution over time.

    history_snapshots : list of farm snapshots
    interval          : milliseconds between frames
    """

    fig, ax = plt.subplots(figsize=(6, 6))

    def update(frame_idx):
        ax.clear()

        snapshot = history_snapshots[frame_idx]
        encoded = [encode_plant_visual(p) for p in snapshot["plants"]]

        xs = [p["x"] for p in encoded]
        ys = [p["y"] for p in encoded]
        sizes = [p["size"] * 300 for p in encoded]
        colors = [p["color"] for p in encoded]

        ax.scatter(xs, ys, s=sizes, c=colors, alpha=0.85)
        ax.set_title(f"Farm at Day {snapshot['day']}")
        ax.set_xlabel("X position (m)")
        ax.set_ylabel("Y position (m)")
        ax.grid(True)
        ax.axis("equal")

    anim = FuncAnimation(
        fig,
        update,
        frames=len(history_snapshots),
        interval=interval,
        repeat=False
    )

    plt.show()
