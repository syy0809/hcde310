# In-class 6: NASA EPIC (photos of the whole Earth from space), with the key kept in .env
#
# 1. Load the key from .env (python-dotenv: load_dotenv(), then os.getenv("NASA_API_KEY"))
# 2. Call https://api.nasa.gov/EPIC/api/natural with your key as the api_key parameter,
#    and timeout=10 so it gives up instead of hanging if the server is slow
# 3. Check r.status_code before you use the data
# 4. The reply is a list of today's photos. Print the caption and the date of the first one

import os
import requests
from dotenv import load_dotenv

# Load the NASA API key from .env
load_dotenv()
api_key = os.getenv("NASA_API_KEY")

# Call the NASA EPIC API
url = "https://api.nasa.gov/EPIC/api/natural"
r = requests.get(url, params={"api_key": api_key}, timeout=10)

# Check the status code
print("Status code:", r.status_code)

if r.status_code == 200:
    data = r.json()

    if len(data) > 0:
        first_photo = data[0]
        print("Caption:", first_photo["caption"])
        print("Date:", first_photo["date"])
        print("Image ID:", first_photo["image"])
    else:
        print("No photos found.")
else:
    print("Request failed.")
