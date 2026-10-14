# HW2 Part 3 – Counting with a dictionary
#
# In `part3.py`:
#
# 1. Build a dictionary counting works per artist, and print it: `{'Vincent van Gogh': 1, ...}`. A
#    work with no artist counts under `'Unknown'`.
# 2. Print the artist with the most works: `Most works: Claude Monet (2)`
#
# (This is the letter-counting pattern from Class 3, applied to art.)

from artworks import artworks

works_count = {}

for artwork in artworks:
    artist = artwork.get("artist", "Unknown")
    works_count[artist] = works_count.get(artist, 0) + 1 
print(works_count)

most_artist = max(works_count, key=works_count.get)
print(f"Most works: {most_artist} ({works_count[most_artist]})")


