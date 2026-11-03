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

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/") 
def home():
    return render_template("home.html")

#Results route using fake data first
@app.route("/results")
def results():
    # Fake data lets us test the page before connecting the API.
    artworks = [
        {
            "title": "Water Lilies",
            "artist_title": "Claude Monet",
            "date_display": "1906"
        },
        {
            "title": "Haystacks",
            "artist_title": "Claude Monet",
            "date_display": "1891"
        }
    ]

    return render_template("results.html", artworks=artworks)
