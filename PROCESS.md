# Process

## Tools used

I used Python's standard-library `zipfile`, `csv`, and `datetime` modules to
read the raw Darwin Core tab-separated file and parse dates. I used matplotlib
for the map, custom `Path` markers, labels, and legends; NumPy for the numeric
arrays and point-size scaling; Pillow through matplotlib's `PillowWriter` for
the GIF; and uv to run the scripts with their declared dependencies. I used
GitHub Actions to run the Assignment 2 checker after each push. Coding
assistance helped draft and debug the plotting code, but I checked the real
column names and ran the generated program myself.

## Data decisions

I kept `decimalLatitude`, `decimalLongitude`, `eventDate`, `scientificName`,
and `individualCount` because they are real fields in the downloaded file.
They control position, animation order, colour, and size respectively. I did
not invent a column name: I inspected the header before writing the parser.
The script skips rows without usable latitude or longitude because they cannot
be placed on this geographic plot. Four records have no individual count, so
the script uses 1 for those sizes rather than silently dropping the records.

## What I kept

I kept matplotlib. It was already used by the project, and its `Path` marker
API let each observation remain a recognizable jellyfish instead of becoming
another generic dot. It also produced the PNG, SVG, and GIF from one plotting
script, so the static image and animation use the same visual mapping.

## What I rejected

I rejected pandas for this version. The source is one tab-separated file inside
a ZIP, and a small `csv.DictReader` loop was enough to parse the five fields we
needed; adding pandas would have added a large dependency without helping the
visual result. I also rejected random decorative variation because colour,
size, and time should be explainable from the data.

## Corrections to the generated code

The first marker implementation used matplotlib curve control points with the
wrong `Path` codes. That produced long diagonal lines across the figure. I
replaced the curves with explicit line segments for the bell and tentacles,
reran the script, and inspected the output. I also verified that the output
GIF had 48 frames and that the Assignment 2 checker passed.
