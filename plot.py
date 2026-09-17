# /// script
# requires-python = ">=3.10"
# ///

from pathlib import Path
from zipfile import ZipFile
import csv

HERE = Path(__file__).parent
DATA = HERE / "data" / "hk-jellyfish.zip"


def main():
    with ZipFile(DATA) as z:
        with z.open("occurrence.txt") as f:
            reader = csv.DictReader(
                (line.decode("utf-8") for line in f),
                delimiter="\t",
            )

            first_row = next(reader)

            print("First row:")
            print(first_row)

            value = first_row["decimalLatitude"]

            print("\nOne value:")
            print(value)

            print("\nType:")
            print(type(value))


if __name__ == "__main__":
    main()