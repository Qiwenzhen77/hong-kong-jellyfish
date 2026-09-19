# hong-kong-jellyfish

## What is this?

This project visualizes jellyfish observations in Hong Kong.

The natural phenomenon is jellyfish occurrence in Hong Kong waters. The dataset contains real observations collected from 2021 to 2025.

## Data source

The data comes from the [Jellyfish in Hong Kong: a citizen science dataset](https://ipt.taibif.tw/resource?r=hk-jellyfish) published through TaiBIF.

The dataset contains 1,536 observation records in the current dataset version.

## Visualization

The visualization shows the geographic distribution of jellyfish observations in Hong Kong. Each point represents one observation, using its latitude and longitude.

![Jellyfish observations in Hong Kong](out/jellyfish-observations.png)

## How to run

Run the following commands from the project folder:

```bash
uv run fetch.py
uv run plot.py