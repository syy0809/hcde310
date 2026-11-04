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