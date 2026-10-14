# HW2 Part 1 – Model first (in `design.md`, no code)

---

## 1. Why is `artworks` a list of dictionaries and not one big dictionary? What would you lose or gain the other way?

I think using a list of dictionaries makes more sense because we have multiple artworks, and each artwork has its own information. Each dictionary stores details like the title, artist, year, and medium, while the list keeps all the artworks together. If we used one big dictionary with artwork titles as keys, it might be easier to look up a specific artwork, but artworks with the same title could be a problem because dictionary keys must be unique. Also, using a list makes it easier to go through all the artworks one by one, while still keeping each artwork's information organized separately.

## 2. Which fields are sometimes missing? What should the app show when they are?
I noticed that some artworks are missing the artist, year, or medium. For example, "Untitled (vase)" only has a title, and "Nighthawks" does not have a medium. I think the app should display "Unknown" when information is missing instead of showing an error. This way, users can still see the available information even if some details are missing, and the app can handle incomplete records without crashing.