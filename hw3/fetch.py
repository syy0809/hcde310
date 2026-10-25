# HW3 Part 2 + Part 3 + Part 4
#
# Instructions: README.md in this folder (same as the assignment on Canvas).

import requests

FIELDS = "id,title,artist_title,artist_display,date_display"

# Functions go here (above the code that runs)

def count_by_artist(artworks):
    counts = {}

    for artwork in artworks:
        artist = artwork.get("artist_title") or "Unknown"

        if artist in counts:
            counts[artist] += 1
        else:
            counts[artist] = 1

    return counts


def save_results(artworks, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for artwork in artworks:
            title = artwork.get("title") or "Unknown title"
            artist = artwork.get("artist_title") or "Unknown"
            date = artwork.get("date_display") or "Unknown date"

            file.write(f"Date: {date} | Title: {title} | Artist: {artist}\n")

term = input("Search the Art Institute for: ")

url = "https://api.artic.edu/api/v1/artworks/search"     
params = {
    "q": term,
    "fields": FIELDS
}  
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    artworks = data["data"]

    save_results(artworks, "artworks.txt")
    print("Results saved to artworks.txt")

    if not artworks:
        print("No artworks found.")
    else:
        for artwork in artworks:
            title = artwork.get("title") or "Unknown title"
            artist = artwork.get("artist_title") or "Unknown artist"
            artist_info = artwork.get("artist_display") or "No artist information"
            date = artwork.get("date_display") or "Unknown date"

            print(f"Title: {title}")
            print(f"Artist: {artist}")
            print(f"Artist information: {artist_info}")
            print(f"Date: {date}")
            print("--------------------")
        artist_counts = count_by_artist(artworks)

        print("Artwork counts by artist:")

        for artist, count in artist_counts.items():
            print(f"{artist}: {count}")


else:
    print(f"Request failed: {response.status_code} {response.reason}")



