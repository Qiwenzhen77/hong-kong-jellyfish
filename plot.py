# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib"]
# ///

from pathlib import Path
from zipfile import ZipFile
import csv
import matplotlib.pyplot as plt


HERE = Path(__file__).parent
DATA = HERE / "data" / "hk-jellyfish.zip"
OUT = HERE / "out"


def main():
    OUT.mkdir(exist_ok=True)

    latitudes = []
    longitudes = []

    with ZipFile(DATA) as z:
        with z.open("occurrence.txt") as f:
            reader = csv.DictReader(
                (line.decode("utf-8") for line in f),
                delimiter="\t",
            )

            for row in reader:
                if row["decimalLatitude"] and row["decimalLongitude"]:
                    latitudes.append(float(row["decimalLatitude"]))
                    longitudes.append(float(row["decimalLongitude"]))

    plt.figure(figsize=(8, 8))

    plt.scatter(
        longitudes,
        latitudes,
        s=12,
        alpha=0.5,
    )

    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Jellyfish Observations in Hong Kong")

    plt.savefig(OUT / "jellyfish-observations.png", dpi=300)
    plt.savefig(OUT / "jellyfish-observations.svg")

    plt.show()


if __name__ == "__main__":
    main()