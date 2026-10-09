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

Looking back at my Day 1 app, AIC Floor Finder, I can now recognize some programming concepts that I learned this week, such as lists, loops, and if statements. For example, in line 52, the code uses a list to store different museum floors. In line 68, a while loop is used to load gallery information. Also, in line 127, an if statement checks whether an artwork is currently on view. These programming concepts help my app display different floors, search for artworks, and show their locations. After learning Python this week, I have a better understanding of how my Day 1 app works.

