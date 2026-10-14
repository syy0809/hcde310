# HW2 Part 5 – Debug log (`debug_log.md`)

Record **at least 2 errors** you hit. No errors? Break something on purpose and log it. For each error, write:

---

## Entry 1

### 1. Error message
*copy it exactly*
✗ part3.py doesn't match yet. Lines with - are expected, + are yours:
   -{'Vincent van Gogh': 1, 'Edward Hopper': 1, 'Grant Wood': 1, 'Georges Seurat': 1, 'Pablo Picasso': 1, 'Claude Monet': 2, 'Mary Cassatt': 1, "Georgia O'Keeffe": 1, 'Unknown': 1}
   -Most works: Claude Monet (2)
   +{'Vincent van Gogh': 1, 'Edward Hopper': 1, 'Grant Wood': 1, 'Georges Seurat': 1, 'Pablo Picasso': 1, 'Claude Monet': 1, 'Mary Cassatt': 1, "Georgia O'Keeffe": 1, 'Unknown': 1}
   +Most works: Vincent van Gogh (1)
   No Python error message appeared, but the output was incorrect. Claude Monet was counted as having 1 artwork instead of 2.


### 2. What I thought it meant

At first, I thought there was something wrong with how I counted the artworks because the program ran, but the result did not match the expected output.

### 3. What it actually meant

I realized that I wrote works_count.get("artist", 0) instead of works_count.get(artist, 0). I confused the string "artist" with the variable artist. Because of this, the program kept counting each artist as having only one artwork.

### 4. The fix

remove the quotation marks for the variable artist
works_count[artist] = works_count.get(artist, 0) + 1

## Entry 2

### 1. Error message
*copy it exactly*
✗ part4.py doesn't match yet. Lines with - are expected, + are yours:
   -['Water Lilies', 'Stacks of Wheat (End of Summer)']
   -[]
   +['Water Lilies']
   +None
   The expected result was a list containing two artworks by Claude Monet, but my function only returned one artwork, "Water Lilies". Also, when I searched for an artist named "Nobody", my function returned None instead of an empty list [].

### 2. What I thought it meant

At first, I thought there was something wrong with my if statement because the function only found one artwork by Claude Monet.

### 3. What it actually meant

I realized that I put return titles inside the if statement. This caused the function to stop as soon as it found the first matching artwork. When there was no matching artist, the function returned None instead of an empty list.

### 4. The fix

I moved return titles outside the for loop so the function could check all the artworks before returning the list. I also removed the unnecessary pass statement. After fixing the code, the function returned both artworks by Claude Monet and an empty list for "Nobody".
