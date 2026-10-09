# HW1 notes

## Part 4: Predict, run, explain

**My prediction for `predict.py` (written BEFORE running it):**

0 The Bedroom 1989
1 Nighthawks 2042
2 American Gothic 2030
10
11

**What it actually printed:**

0 The Bedroom 1989
1 Nighthawks 2042
2 American Gothic 2030
10
11

**Explain:** If I was off, which line surprised me and why? If I was right, why do the last two lines print different numbers?

I am proud that I make the right prediction. The reason why the last two lines print different numbers is that:
`len(titles)` means the number of artworks in the `titles` list, so it prints 10.
`len(titles[0])` means the number of characters in the first artwork's title, including the space in the middle, so it prints 11.

## Part 5: Reflection (about 100 words)

Look back at your Day 1 app: its code if you can still open it, or your screenshots of it running. Is there anything you can now recognize (a loop, an `if`, a list)? Where? If you only have screenshots, what do you think the code had to do to make the app behave that way?

