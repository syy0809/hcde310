## AI Conversations

*The following conversations are reconstructed in English from earlier ChatGPT discussions, rather than verbatim transcripts.*

### Conversation 1: Flask Results Route

**Me:** How can I create a results page for my Flask application?

**ChatGPT:** Create a `/results` route in `app.py`. Use `request.args.get()` to receive the search term and `render_template()` to display the results page.

### Conversation 2: Connecting the API

**Me:** How can I connect my Flask app to the Art Institute of Chicago API?

**ChatGPT:** Use the Python requests library to send an API request. Create a `search_art(term)` function that returns artwork data based on the user's search term.

### Conversation 3: Displaying Search Results

**Me:** How can I display artwork information on my results page?

**ChatGPT:** Use a Jinja for loop in `results.html` to display each artwork's title, artist, and date.

### Conversation 4: Empty Input

**Me:** How can I handle an empty search input?

**ChatGPT:** Check whether the search term is empty before calling the API. If it is empty, display "Please enter a search term."

### Conversation 5: No Results

**Me:** How can I test whether my app handles searches with no results?

**ChatGPT:** Search for a term that is unlikely to match any artworks. If the API returns an empty list, display "No artworks found. Please try another search."

### Conversation 6: Unexpected API Results

**Me:** Why does my app display unrelated artworks when I search for a nonsense term?

**ChatGPT:** The API may return results that do not exactly match the search term. Try another search term to test the no-results condition.

### Conversation 7: API Error Testing

**Me:** How can I test whether my app handles API errors?

**ChatGPT:** Temporarily change the API URL to an invalid endpoint. Search for an artist and check whether the app displays an error message. Restore the correct URL afterward.

### Conversation 8: Missing Artwork Information

**Me:** How can I handle artworks with missing dates?

**ChatGPT:** Add a fallback value in the HTML template. For example, display "Unknown date" when the date field is missing.

### Conversation 9: Testing with Fake Data

**Me:** How can I test missing artwork information using fake data?

**ChatGPT:** Temporarily replace the API results with fake artwork data containing a missing field. Check the displayed result and restore the real API afterward.

### Conversation 10: Python Indentation Error

**Me:** What does "IndentationError: unexpected indent" mean?

**ChatGPT:** It means a line of Python code has incorrect indentation. Check that the lines inside each function are consistently indented.

## What Surprised Me

One thing that surprised me was how HTML can be used to organize and structure a webpage. Before this assignment, I did not realize how different HTML elements could work together to create a functional website. Working with HTML templates gave me many new ideas and inspired me to explore more creative web layouts and structures. It also made me interested in building more interactive and visually engaging websites in the future.

Another thing that surprised me was that the API returned unrelated artworks when I searched for a nonsense term. I expected no results, but the API still returned artwork data. This helped me understand that API responses do not always match my expectations.

## What I Changed

I tested my app with different search terms and checked how it handled errors. I updated the results page to display "Unknown date" when artwork information was missing. I also tested API errors by temporarily changing the API URL to an invalid endpoint and then restoring the correct URL.