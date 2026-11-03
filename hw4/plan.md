# HW4 Plan: Art Search Web App

## 1. Screen Sketches

![Search Page and Results Page](screen-sketch.png)

## 2. Data needed from the API

I will reuse the Art Institute of Chicago API from HW3.

API endpoint:
https://api.artic.edu/api/v1/artworks/search

The results page will display the following information:

- `title`: The name of the artwork.
- `artist_title`: The artist's name.
- `artist_display`: Additional information about the artist.
- `date_display`: The date of the artwork.

I will use the search term entered by the users to request specific matching artworks.
If a field is missing, I will display a helpful fallback message instead of showing a blank value.

## 3. Function and Route Specifications

### Home Route (/)

Input: None.

Output: Displays the search page with a text input, such as an artist's name and a Search button.

Checks:
1. Open the homepage and confirm the search form appears.
2. Use the Tab key to move between the input and Search button.

### Results Route (/results)

Input: A search term entered by the user.

Output: Displays matching artworks or a helpful message.

Checks:
1. Search "monet" and confirm artwork results appear.
2. Submit an empty search and confirm a helpful message appears.
3. Search a nonsense term and check the no-results message.

### search_art(term) Function

Input: A search term entered by the user, such as "monet".

Output: A list of matching artworks from the Art Institute of Chicago API, or None if the API request fails.

Checks:
1. Search "monet" and confirm the API returns artwork data.
2. Temporarily use an invalid API URL and confirm a helpful error message appears.
3. Check that artworks with missing information display fallback text.

## 4. Browser Test Results

### Test 1: Empty Input

Input: Submit the search form without entering anything.

Result: PASS

The app displayed "Please enter a search term." instead of showing an empty results page.

### Test 2: No Results

Input: Search for "xyzqwerty987654321".

Result: FAIL (Unexpected API Behavior)

The app displayed unrelated artworks instead of showing a no-results message. The API returned artwork data even though the search term was nonsense.

Retest: Search for "123456".

Result: PASS

The app displayed "No artworks found. Please try another search."

### Test 3: API Error

Input: Temporarily change the API URL to an invalid endpoint and search for "monet".

Result: PASS

The app displayed "Could not load artworks. Please try again later." I restored the correct API URL after testing.

### Test 4: Missing Fields

Input: Test an artwork with a missing date_display field.

Result: PASS

The app displayed "Unknown date" instead of leaving the date blank.

### Test 5: Real API Search

Input: Search for "picasso".

Result: PASS

The app displayed real artworks, including titles, artists, and dates.

### Reflection

One unexpected behavior was that the API returned unrelated artworks for a nonsense search term. I learned that an API can return results that do not match the user's expectations. I also learned how to handle empty inputs, missing information, and API errors to make the website more user-friendly.


