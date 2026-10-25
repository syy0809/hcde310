# HW3 Part 1 – Read the response first

AI Use: Stage 2 (Tutor)

Open `sample_response.json` (a saved Art Institute of Chicago search). In `notes.md`:

---

## 1. The total number of results is at `data["pagination"]["total"]`. What's the path to the first artwork's title?

data["data"][0]["title"]

## 2. Find 3 more fields you'd want to show a user, and their paths

Artist name: data["data"][0]["artist_title"]

Date: data["data"][0]["date_display"]

Artwork type: data["data"][0]["artwork_type_title"]

I chose these fields because they help users learn more about each artwork.

## 3. Which fields are `null` for some works?

The artist_title field is null for the third artwork, "Baroque Pearl Mounted as a Cat Holding a Mouse".

Its path is data["data"][2]["artist_title"].

The top-level preference field is also null.

## 4. Predict
*open `fetch.py` and read it, but don't change anything yet. What do you think will happen when you run it?*

I think the program will show a SyntaxError because the if statement is incomplete. It does not have a condition or a colon. The program will stop before asking for a search term or making an API request.

## 5. Run it
*run `python3 fetch.py`. When it asks for a search term, type a word (like `cat`) and press Enter. What actually happened? Read the traceback bottom line first: what went wrong, and which line of your file caused it?*

I ran python3 fetch.py and entered cat as the search term. The program showed a requests.exceptions.MissingSchema error.

The error happened because the URL was an empty string (url = ""). The program tried to make an API request without a valid URL.

The error occurred on line 16 of fetch.py:

response = requests.get(url, params=params)

My prediction was different from the actual result. The program was able to ask for a search term, but it failed when trying to use an empty URL.

