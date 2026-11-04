# Open Library Search API Guide

### 1. What Is the Open Library Search API?
The Open Library Search API is a free API that allows developers to search for books and retrieve information such as titles, authors, publication years, and cover IDs. Designers can use this API to build book discovery websites, digital libraries, or reading recommendation tools. Instead of manually collecting book information, they can use the API to retrieve book data and display it in their projects.

### 2. Setup
I used Python and the requests library to access the Open Library Search API.

Make sure Python is installed on your computer.

Install the requests library by running:

pip install requests

Create a Python file named example.py.

Use the following API endpoint:

https://openlibrary.org/search.json

Run the Python file in Terminal:

python example.py

The example does not require an API key or authentication. I tested the API using Python and successfully received a response with status code 200.

### 3. Working Example

This example searches for books about artificial intelligence using the Open Library Search API. It requests five results and displays the first three in JSON format.

```python
import requests
import json

# Open Library Search API
url = "https://openlibrary.org/search.json"

# API parameters
params = {
    "q": "artificial intelligence",
    "limit": 5,
    "fields": "key,title,author_name,first_publish_year,cover_i"
}

# Send API request
response = requests.get(url, params=params, timeout=15)

# Check the response
print("Status Code:", response.status_code)
print("URL:", response.url)

response.raise_for_status()

# Convert JSON response to Python data
data = response.json()

# Select a few fields for the sample
sample = {
    "numFound": data.get("numFound"),
    "docs": data.get("docs", [])[:3]
}

# Print the JSON sample
print(json.dumps(sample, indent=2))
```

### Actual Output

```text
Status Code: 200
URL: https://openlibrary.org/search.json?q=artificial+intelligence&limit=5&fields=key%2Ctitle%2Cauthor_name%2Cfirst_publish_year%2Ccover_i
{
  "numFound": 23024,
  "docs": [
    {
      "author_name": [
        "Stuart J. Russell",
        "Peter Norvig"
      ],
      "cover_i": 92018,
      "first_publish_year": 1994,
      "key": "/works/OL2896994W",
      "title": "Artificial intelligence"
    },
    {
      "author_name": [
        "Patrick Henry Winston"
      ],
      "cover_i": 135105,
      "first_publish_year": 1977,
      "key": "/works/OL2024373W",
      "title": "Artificial intelligence"
    },
    {
      "author_name": [
        "Elaine A. Rich"
      ],
      "cover_i": 55159,
      "first_publish_year": 1983,
      "key": "/works/OL4453349W",
      "title": "Artificial intelligence"
    }
  ]
}
```

### 4. Gotchas

One thing I noticed when testing the Open Library Search API was that different books can have the same title. When I searched for "artificial intelligence," the first three results all had the title "Artificial intelligence," but they had different authors and publication years. The API returned enough information to distinguish these books, but I learned that the title alone is not a unique identifier. When using this API to build a book search interface, I should display additional information such as authors and publication years to help users identify the correct book.

Another thing I learned was the difference between the total number of matches and the number of results displayed. My API response showed `numFound: 23024`, but I set `limit` to 5 and used `[:3]` to display only the first three books. At first, these different numbers could be confusing, so it is important to understand how the API returns and filters results.

I also checked whether the first five books were missing author names, publication years, or cover IDs. None of these fields were missing in my test. However, a designer should still consider how to handle missing information when building a book search interface.

### 5. Design Angle

**Project Idea: Book Discovery Website**

One project idea is a book discovery website where users can search for books by title, author, or topic. The website would use the Open Library Search API to display book titles, authors, publication years, and cover images. Users could explore different books and find ones that match their interests.

**UX Consideration: Clear and Accurate Search Results**

One important UX consideration is how to present search results clearly. During my testing, I noticed that several books had the same title but different authors. If a website only displayed book titles, users might have difficulty identifying the book they wanted. To improve the experience, I would display the author, publication year, and cover image alongside each title. I would also provide helpful fallback text when information is missing.

### 6. AI Use

I used ChatGPT to help organize and revise this Markdown guide, and understand the testing results. The Python example was reused from my P0 assignment. I personally ran the code and confirmed that it successfully returned book data from the Open Library Search API with status code 200. I also tested the returned book fields myself.