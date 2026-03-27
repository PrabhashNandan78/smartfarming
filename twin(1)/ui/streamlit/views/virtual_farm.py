import matplotlib.pyplot as plt
import streamlit as st


def render_virtual_farm(
    encoded_plants,
    title="Virtual Farm View",
    zoom=1.0,
    pan_x=0.0,
    pan_y=0.0
):
    fig, ax = plt.subplots(figsize=(10, 6))

    xs = [p["x"] for p in encoded_plants]
    ys = [p["y"] for p in encoded_plants]
    sizes = [p["size"] * 1400 for p in encoded_plants]
    colors = [p["color"] for p in encoded_plants]

    # --- Plants ---
    ax.scatter(xs, ys, s=sizes, c=colors, alpha=0.9)

    xs = [p["x"] for p in encoded_plants]
    ys = [p["y"] for p in encoded_plants]

    x_center = sum(xs) / len(xs)
    y_center = sum(ys) / len(ys)

    x_range = (max(xs) - min(xs)) / zoom
    y_range = (max(ys) - min(ys)) / zoom

    ax.set_xlim(
        x_center - x_range / 2 + pan_x,
        x_center + x_range / 2 + pan_x
    )
    ax.set_ylim(
        y_center - y_range / 2 + pan_y,
        y_center + y_range / 2 + pan_y
    )


    # --- Farm boundary ---
    xmin, xmax = min(xs) - 0.3, max(xs) + 0.3
    ymin, ymax = min(ys) - 0.3, max(ys) + 0.3

    ax.plot(
        [xmin, xmax, xmax, xmin, xmin],
        [ymin, ymin, ymax, ymax, ymin],
        color="#444444",
        linewidth=2
    )

    # --- Row lines ---
    row_positions = sorted(set(ys))
    for y in row_positions:
        ax.hlines(
            y,
            xmin=xmin,
            xmax=xmax,
            colors="#222222",
            linestyles="dashed",
            linewidth=1,
            alpha=0.6
        )

    # --- Styling ---
    ax.set_title(title, color="white")
    ax.set_aspect("equal")
    ax.axis("off")

    fig.patch.set_facecolor("#0e1117")
    ax.set_facecolor("#0e1117")

    st.pyplot(fig)
