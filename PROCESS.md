# Process

## Tools used

I used ChatGPT to help write and debug the plotting code, Python and matplotlib
to read the data and make the visualization, and uv to run the script.

## What I kept

I kept the latitude and longitude of each observation because they show where
the jellyfish were found. I also kept the real date and species fields so that
the animation and colours come from the dataset.

## What I rejected

I rejected a generic scatter plot with identical circular points because it did
not look like jellyfish and hid the differences between observations.

## Correction

ChatGPT's first jellyfish marker created long diagonal lines because the path
was encoded incorrectly. I corrected the marker, ran the script again, and
checked the final PNG and GIF.
