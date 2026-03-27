import matplotlib.pyplot as plt
from Visualization.encoding import encode_plant_visual


def plot_side_by_side(snapshot_a, snapshot_b, title_a, title_b):
    """
    Compare two farm snapshots side by side.
    """

    encoded_a = [encode_plant_visual(p) for p in snapshot_a["plants"]]
    encoded_b = [encode_plant_visual(p) for p in snapshot_b["plants"]]

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    for ax, encoded, title in zip(
        axes,
        [encoded_a, encoded_b],
        [title_a, title_b],
    ):
        xs = [p["x"] for p in encoded]
        ys = [p["y"] for p in encoded]
        sizes = [p["size"] * 300 for p in encoded]
        colors = [p["color"] for p in encoded]

        ax.scatter(xs, ys, s=sizes, c=colors, alpha=0.85)
        for p in encoded:
            ax.text(
                p["x"],
                p["y"] + 0.08,
                f"{p['LAI']}",
                ha="center",
                fontsize=8
            )

        ax.set_title(title)
        ax.set_xlabel("X position (m)")
        ax.set_ylabel("Y position (m)")
        ax.grid(True)
        ax.axis("equal")

    plt.tight_layout()
    plt.show()
