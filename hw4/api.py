# Reuses the Art Institute of Chicago API from HW3.
import requests

URL = "https://api.artic.edu/api/v1/artworks/search"

FIELDS = "id,title,artist_title,artist_display,date_display"

# Search for artworks using a user's search term.
def search_art(term):
    try:
        response = requests.get(
            URL,
            params={"q": term, "fields": FIELDS},
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=10
        )

        if response.status_code != 200:
            return None

        data = response.json()
        return data["data"]

    except (requests.RequestException, ValueError, KeyError):
        return None
