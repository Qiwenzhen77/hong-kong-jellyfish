# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "numpy", "pillow"]
# ///

from pathlib import Path
import shutil

import plot


HERE = Path(__file__).parent
OUT = HERE / "out"
SITE = HERE / "site"


def main():
    SITE.mkdir(exist_ok=True)

    # Run the existing visualization script.
    # plot.py is not modified.
    plot.main()

    # Copy the generated animation into the website.
    gif_source = OUT / "jellyfish-observations.gif"
    gif_target = SITE / "jellyfish-observations.gif"

    if not gif_source.exists():
        raise FileNotFoundError(
            "jellyfish-observations.gif was not generated."
        )

    shutil.copy2(gif_source, gif_target)

    # Create the webpage.
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Jellyfish Observations in Hong Kong</title>

    <style>
        body {
            margin: 0;
            background: #071d2b;
            color: #f6f0df;
            font-family: Arial, sans-serif;
        }

        main {
            max-width: 1100px;
            margin: 0 auto;
            padding: 60px 30px;
            text-align: center;
        }

        h1 {
            font-size: 42px;
            font-weight: 400;
            margin-bottom: 10px;
        }

        .subtitle {
            color: #8fc8bd;
            margin-bottom: 40px;
        }

        img {
            width: 100%;
            max-width: 1000px;
            display: block;
            margin: 0 auto;
        }

        .description {
            max-width: 720px;
            margin: 40px auto;
            line-height: 1.8;
            color: #b8d8d2;
            text-align: left;
        }

        a {
            color: #ffd166;
        }

        footer {
            margin-top: 50px;
            font-size: 13px;
            color: #6f929d;
        }
    </style>
</head>

<body>

<main>

    <h1>Jellyfish Observations in Hong Kong</h1>

    <div class="subtitle">
        1,536 real observations · 2021–2025
    </div>

    <img
        src="jellyfish-observations.gif"
        alt="Animated visualization of jellyfish observations in Hong Kong"
    >

    <div class="description">

        <p>
            Each jellyfish represents a real observation from
            the Hong Kong Jellyfish citizen science dataset.
        </p>

        <p>
            Position is based on the recorded latitude and longitude.
            Colour represents species, size represents individual count,
            and the animation follows the observation dates.
        </p>

        <p>
            The data comes from the
            <a href="https://ipt.taibif.tw/resource?r=hk-jellyfish">
                Hong Kong Jellyfish citizen science dataset
            </a>.
        </p>

    </div>

    <footer>
        Creative Programming for Designers and Artists · Assignment 2
    </footer>

</main>

</body>
</html>
"""

    (SITE / "index.html").write_text(
        html,
        encoding="utf-8",
    )

    print("Website generated:")
    print(SITE / "index.html")


if __name__ == "__main__":
    main()