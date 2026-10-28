
import requests
import json

# Open-Meteo API
url = "https://api.open-meteo.com/v1/forecast"

# API parameters
params = {
    "latitude": 47.6062,
    "longitude": -122.3321,
    "current": "temperature_2m,relative_humidity_2m",
    "hourly": "temperature_2m,precipitation_probability",
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "America/Los_Angeles"
}

# Send API request
response = requests.get(url, params=params, timeout=15)

print("Status Code:", response.status_code)
print("URL:", response.url)

response.raise_for_status()

# Convert JSON response into Python data
data = response.json()

# Create a shorter JSON sample for P0
sample = {
    "latitude": data["latitude"],
    "longitude": data["longitude"],
    "timezone": data["timezone"],
    "current": data["current"]
}

# Print the trimmed JSON
print(json.dumps(sample, indent=2))
