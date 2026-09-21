# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "numpy", "pillow"]
# ///

from datetime import datetime
import csv
from pathlib import Path
from zipfile import ZipFile

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.path import Path as MatplotlibPath


HERE = Path(__file__).parent
DATA = HERE / "data" / "hk-jellyfish.zip"
OUT = HERE / "out"


def jellyfish_marker():
    """Build one reusable jellyfish silhouette for every observation."""
    vertices = [
        (-0.72, 0.05), (-0.55, 0.42), (-0.22, 0.62), (0.0, 0.66),
        (0.22, 0.62), (0.55, 0.42), (0.72, 0.05), (0.0, -0.02),
        (-0.72, 0.05),
        (-0.45, -0.05), (-0.34, -0.34), (-0.43, -0.67),
        (-0.18, -0.1), (-0.08, -0.38), (-0.02, -0.72),
        (0.18, -0.1), (0.28, -0.38), (0.23, -0.68),
        (0.48, -0.05), (0.4, -0.32), (0.52, -0.6),
    ]
    codes = [
        MatplotlibPath.MOVETO,
        MatplotlibPath.LINETO, MatplotlibPath.LINETO, MatplotlibPath.LINETO,
        MatplotlibPath.LINETO, MatplotlibPath.LINETO, MatplotlibPath.LINETO,
        MatplotlibPath.LINETO, MatplotlibPath.CLOSEPOLY,
        MatplotlibPath.MOVETO, MatplotlibPath.LINETO, MatplotlibPath.LINETO,
        MatplotlibPath.MOVETO, MatplotlibPath.LINETO, MatplotlibPath.LINETO,
        MatplotlibPath.MOVETO, MatplotlibPath.LINETO, MatplotlibPath.LINETO,
        MatplotlibPath.MOVETO, MatplotlibPath.LINETO, MatplotlibPath.LINETO,
    ]
    return MatplotlibPath(vertices, codes)


def load_observations():
    observations = []
    with ZipFile(DATA) as archive:
        with archive.open("occurrence.txt") as source:
            reader = csv.DictReader(
                (line.decode("utf-8") for line in source), delimiter="\t"
            )
            for row in reader:
                if not row["decimalLatitude"] or not row["decimalLongitude"]:
                    continue
                date_text = row["eventDate"][:10]
                observations.append(
                    {
                        "latitude": float(row["decimalLatitude"]),
                        "longitude": float(row["decimalLongitude"]),
                        "date": datetime.fromisoformat(date_text),
                        "species": row["scientificName"] or row["vernacularName"] or "Unknown",
                        "count": max(float(row["individualCount"] or 1), 1),
                    }
                )
    return sorted(observations, key=lambda item: item["date"])


def main():
    OUT.mkdir(exist_ok=True)
    observations = load_observations()
    longitudes = np.array([item["longitude"] for item in observations])
    latitudes = np.array([item["latitude"] for item in observations])
    counts = np.array([item["count"] for item in observations])
    species = [item["species"] for item in observations]
    species_names = sorted(set(species))
    palette = ["#ff8066", "#ffd166", "#5eead4", "#7dd3fc", "#f9a8d4", "#a7f3d0", "#fca5a5", "#c4b5fd"]
    species_colors = {
        name: palette[index % len(palette)]
        for index, name in enumerate(species_names)
    }
    point_colors = [species_colors[name] for name in species]
    point_sizes = 34 + 72 * np.log1p(counts) / np.log1p(counts.max())

    fig, ax = plt.subplots(figsize=(10, 8), facecolor="#071d2b")
    ax.set_facecolor("#0b2d3d")
    ax.set_xlim(longitudes.min() - 0.08, longitudes.max() + 0.08)
    ax.set_ylim(latitudes.min() - 0.08, latitudes.max() + 0.08)
    ax.grid(color="#8dd3c7", alpha=0.13, linewidth=0.8)
    ax.tick_params(colors="#b8d8d2")
    for spine in ax.spines.values():
        spine.set_color("#376575")
    ax.set_xlabel("Longitude", color="#b8d8d2")
    ax.set_ylabel("Latitude", color="#b8d8d2")
    ax.set_title("Jellyfish in Hong Kong waters", loc="left", color="#f6f0df", fontsize=19, pad=18)
    subtitle = ax.text(
        0.0, 1.01, "Each glyph is one observation  /  colour = species  /  size = individualCount",
        transform=ax.transAxes, color="#8fc8bd", fontsize=9, va="bottom",
    )
    date_label = ax.text(
        0.98, 1.01, "", transform=ax.transAxes, ha="right", color="#ffd166",
        fontsize=12, va="bottom", family="monospace",
    )
    points = ax.scatter([], [], marker=jellyfish_marker(), s=[], c=[], linewidths=0.35, edgecolors="#f6f0df")

    legend_names = species_names[:8]
    handles = [
        plt.Line2D([], [], marker=jellyfish_marker(), linestyle="", markersize=10,
                   markerfacecolor=species_colors[name], markeredgecolor="#f6f0df",
                   markeredgewidth=0.35, label=name)
        for name in legend_names
    ]
    legend = ax.legend(handles=handles, title="Species", loc="lower left", fontsize=8,
                       title_fontsize=9, frameon=False, labelcolor="#d9eeea")
    plt.setp(legend.get_title(), color="#ffd166")

    frame_count = 48
    frame_sizes = np.linspace(1, len(observations), frame_count, dtype=int)

    def draw_frame(frame):
        end = frame_sizes[frame]
        points.set_offsets(np.column_stack((longitudes[:end], latitudes[:end])))
        points.set_sizes(point_sizes[:end])
        points.set_color(point_colors[:end])
        date_label.set_text(observations[end - 1]["date"].strftime("%Y  /  %b"))
        subtitle.set_text(f"{end:,} observations  /  colour = species  /  size = individualCount")
        return points, date_label, subtitle

    animation = FuncAnimation(fig, draw_frame, frames=frame_count, interval=140, blit=False)
    animation.save(OUT / "jellyfish-observations.gif", writer=PillowWriter(fps=8), dpi=120)
    draw_frame(frame_count - 1)
    fig.savefig(OUT / "jellyfish-observations.png", dpi=300, facecolor=fig.get_facecolor())
    fig.savefig(OUT / "jellyfish-observations.svg", facecolor=fig.get_facecolor())
    plt.close(fig)


if __name__ == "__main__":
    main()