# hong-kong-jellyfish

## What is this?

This project visualizes jellyfish observations in Hong Kong.

The natural phenomenon is jellyfish occurrence in Hong Kong waters. The dataset contains real observations collected from 2021 to 2025.

## Data source

The data comes from the [Jellyfish in Hong Kong: a citizen science dataset](https://ipt.taibif.tw/resource?r=hk-jellyfish) published through TaiBIF.

The dataset contains 1,536 observation records in the current dataset version.

## Visualization

The visualization shows the geographic distribution of jellyfish observations in Hong Kong. Each observation is drawn as a small jellyfish rather than a generic dot. The latitude and longitude place the jellyfish on the map. Its colour is controlled by the recorded `scientificName`, while its size is scaled from the real `individualCount` field. This keeps the visual changes tied to the data rather than to decorative randomness.

The animated version reveals the observations in chronological order using the recorded `eventDate`. The date label moves from 2021 to 2025 as the observation record grows, so the animation shows when and where the observations accumulated. The static image shows the complete dataset.

![Jellyfish observations in Hong Kong](out/jellyfish-observations.png)

![Animated jellyfish observations in Hong Kong](out/jellyfish-observations.gif)

## How to run

Run the following commands from the project folder:

```bash
uv run fetch.py
uv run plot.py
```

The plotting script writes a PNG, SVG, and animated GIF into `out/`. The GIF can be viewed directly on GitHub, while the SVG preserves the jellyfish shapes for closer inspection.