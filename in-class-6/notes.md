# In-class 6 notes

## What happens with a wrong key? What status code?

When I tested the API with an incorrect key, the request failed and returned a 403 (Forbidden) status code. This means NASA rejected the request because the API key was invalid.

## Where does your key live, and why isn't it in earth.py?

My NASA API key is stored in a local .env file. I use load_dotenv() and os.getenv("NASA_API_KEY") to access it in Python. I don't put the key directly in earth.py because it will be uploaded to GitHub. The .env file is ignored by Git to keep my API key private.


## Stuck? Where?

I was not stuck on this assignment. I successfully called the NASA EPIC API and printed the caption, date, and image ID of the first photo.

