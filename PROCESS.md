# Process

## Tools used

- Python, matplotlib, NumPy, Pillow, and uv
- GitHub Actions for the Assignment 2 check
- Coding assistance for debugging and visualization design

## Data

I used the official Hong Kong jellyfish citizen science dataset from TaiBIF.
The raw ZIP file remains unchanged in `data/`. The plotting script reads the
observation records directly from that archive.

## What I kept

I kept the latitude, longitude, event date, scientific name, and individual
count. These are real fields from the dataset, so they control the position,
animation order, colour, and size of the visualization.

## What I rejected

I rejected a generic scatter plot with identical circular points. It hid the
fact that each record describes a jellyfish observation. I also rejected random
decorative variation because the visual changes should come from the data.

## Iteration

I first made a static scatter plot. I then replaced the circles with a custom
jellyfish marker, sorted records by `eventDate`, and added a 48-frame GIF that
reveals the observations chronologically. The first marker path created long
diagonal artefacts because its curve control points were encoded incorrectly.
I replaced it with explicit line segments for the bell and tentacles, then
reran the script and checked the PNG and GIF output.
