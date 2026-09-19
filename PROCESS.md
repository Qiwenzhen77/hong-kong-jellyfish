# Process

## Tools used

- Python
- matplotlib
- uv
- GitHub
- ChatGPT for coding assistance and debugging

## Data

I used the official Hong Kong jellyfish citizen science dataset from TaiBIF.

The raw ZIP file is stored unchanged in the `data/` folder. The plotting script reads the observation data directly from the ZIP file.

## What I kept

I kept the latitude and longitude of each observation and used them to create a spatial scatter plot.

I kept this approach because the geographic location is an important part of the jellyfish observation data, and each point represents a real observation.

## What I rejected

I rejected making a generic tide chart.

The assignment asks for a visualization based on the selected natural phenomenon and its actual data. A tide chart would not represent the jellyfish observations in this dataset.

## Iteration

I first inspected the first row of the dataset and checked the data type of a latitude value.

The latitude was initially read as a string, so I converted latitude and longitude to numbers before plotting them.

I then created a scatter plot showing the geographic distribution of the observations.