# HW5 test_app.py: one example test. Add your own below it (step 5).
# Run from this folder:  python3 -m pytest
from app import app


def test_home_shows_search_form():
    client = app.test_client()        # a pretend browser, no server needed
    page = client.get("/")            # like typing "/" in the address bar
    assert page.status_code == 200    # the page loaded
    assert b"Artist name" in page.data  # the form's label is on the page

def test_empty_artist_shows_message():
    client = app.test_client()                        # a pretend browser
    page = client.post("/results", data={"artist": ""}) # submit an empty search
    assert page.status_code == 200                    # the page loaded
    assert b"No search term entered." in page.data    # the error message appears
