import requests

URL = "https://api.artic.edu/api/v1/artworks/search"
FIELDS = "id,title,artist_title,date_display,image_id"


def get_artworks(artist):
    params = {"q": artist, "fields": FIELDS, "limit": 10}
    headers = {"User-Agent": "hcde310-artist-search/1.0"}
    response = requests.get(URL, params=params, headers=headers, timeout=10)
    response.raise_for_status()

    artworks = response.json().get("data", [])

    # Keep only artworks that match the artist's name
    matching_artworks = [
        art for art in artworks
        if artist.lower() in (art.get("artist_title") or "").lower()
    ]

    return matching_artworks[:10]

