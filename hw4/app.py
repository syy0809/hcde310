# HW4 Art Search Flask App
# Function: This app allows users to search for artworks by artist name using the Art Institute of Chicago.

# Home Route (/)
# 1. When a user opens the homepage, it will show the search form.
# 2. The form should have a text input and a Search button.
# 3. The form sends the user's search term to /results.

# Results Route (/results)
# 1. Read the search term from the form.
# 2. If the input is empty, show a helpful message.
# 3. Call search_art(term) to get artwork data from the API.
# 4. If the API request fails, show an error message.
# 5. If no artworks are found, show a no-results message.
# 6. If an artwork has missing information, use fallback text.
# 7. Display the results on the results page.

from flask import Flask, render_template, request
from api import search_art
app = Flask(__name__)

@app.route("/") 
def home():
    return render_template("home.html")

# Results route using the real API.
@app.route("/results")
def results():
    # Read the search term from the form.
    term = request.args.get("term", "").strip()

    # Empty input: ask the user to enter something.
    if not term:
        return render_template(
            "home.html",
            message="Please enter a search term."
        )

    # Search for artworks using the API.
    artworks = search_art(term)

    # API error: the request failed.
    if artworks is None:
        return render_template(
            "home.html",
            message="Could not load artworks. Please try again later."
        )

    # No results: the API returned an empty list.
    if not artworks:
        return render_template(
            "home.html",
            message="No artworks found. Please try another search."
        )

    # Display the search results.
    return render_template(
        "results.html",
        artworks=artworks,
        term=term
    )
