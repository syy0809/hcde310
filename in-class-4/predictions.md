# Class 4: Five broken snippets

Your name: Yuyao Sun
Collaborator: Matt shi

# Part 1: Predict

**Don't run anything yet.** Read each snippet in `exercise.py` and write your guesses. A wrong guess is fine: the point is to compare.

## Snippet 1
- Which line breaks? The print statement.
- What error will Python show? (the kind and the message) KeyError: 'Room'
- What's the fix? Change exhibit["Room"] to exhibit["room"] and convert the number to a string.

## Snippet 2
- Which line breaks? The print statement.
- What error will Python show? (the kind and the message) TypeError: can only concatenate str (not "int") to str
- What's the fix? Use str(exhibit["room"]).

## Snippet 3
- Which line breaks? The print statement inside the for loop.
- What error will Python show? (the kind and the message) IndexError: list index out of range
- What's the fix? Change range(len(exhibits) + 1) to range(len(exhibits))

## Snippet 4
- Which line breaks? The last print statement.
- What error will Python show? (the kind and the message) NameError: name 'visit' is not defined
- What's the fix? Change visit to visits.

## Snippet 5
- Which line breaks? The last print statement.
- What error will Python show? (the kind and the message) AttributeError: 'NoneType' object has no attribute 'upper'
- What's the fix? Change print(longest) inside the function to return longest.

# Part 2: Run

Run `python3 exercise.py`. Python stops at the first error, so fix that snippet in `exercise.py`, run again, and see the next one. Fill in what actually happened.

## Snippet 1
- Which line broke? Line 8.
- What error did Python show? KeyError: 'Room'
- What's the fix? I changed "Room" to "room" because dictionary keys are case-sensitive. I also used an f-string to print the room number.


## Snippet 2
- Which line broke? Line 12.
- What error did Python show? TypeError: can only concatenate str (not "int") to str
- What's the fix? I used an f-string because Python cannot directly concatenate a string and an integer.


## Snippet 3
- Which line broke? Line 17.
- What error did Python show? IndexError: list index out of range
- What's the fix? I removed + 1 from range(len(exhibits) + 1) because the list only has three items.

## Snippet 4
- Which line broke? Line 29.
- What error did Python show? NameError: name 'visit' is not defined
- What's the fix? I changed visit to visits because the variable name was incorrect.

## Snippet 5
- Which line broke? Line 41.
- What error did Python show? AttributeError: 'NoneType' object has no attribute 'upper'
- What's the fix? I changed print(longest) to return longest because the function needs to return the longest title.

When all five are fixed, run `python3 check.py` until it says ✓.

Bonus: Snippet 5 prints something *before* it crashes. What, and why does it still crash?

# Part 3: Tutor practice (one snippet)

Pick one snippet. Write your guess first, then ask your tutor. Paste the chat (or a share link) below.

- Snippet #: snippet 5 
- Our guess before asking: We thought the function would print the longest title, but we were not sure why the last line caused an error.
- Chat: https://chatgpt.com/share/6acd54a8-8850-83e9-aa44-66572e50b829
- Did it give you too much? What did you do?
Yes, the tutor initially provided more information than we needed. We focused on understanding the difference between print() and return and then corrected the code ourselves.
