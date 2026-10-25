# HW3 Part 4 – Save the results

AI Use: Stage 3 (Little helper)

Write a new function, `save_results(artworks, filename)`, that writes one line per artwork (title, artist, date) to a `.txt` file. Call it so every search saves its results. Then run `fetch.py` for real once, with a search you pick, and **commit the `.txt` file it made**: that's your proof the live call works.

You may have the AI write this function (about 10 lines) using the **[Stage 3 helper prompt](https://canvas.uw.edu/courses/1959879/pages/stage-3-little-helper-prompt)** (rules on the [AI Use Card](https://canvas.uw.edu/courses/1959879/pages/ai-use-card)). Copilot autocomplete stays off. With or without AI, write each step in `ai_log.md` **as you go**:

Done early? Add `sort_by_date(artworks)` too (not graded).

---

## 1. Try
*paste your own attempt or plan for the function, even if it doesn't work*

My plan was to create a function called save_results(artworks, filename) that loops through the artwork list and writes each artwork's title, artist, and date to a text file.

I planned to use with open(filename, "w", encoding="utf-8") to create the file and file.write() to save each artwork on a separate line. I also wanted to use a default value when an artist's name was missing.

## 2. Chat (AI only)
*paste the whole conversation, your messages and the AI's replies in order, or a share link from the Share button (the link in your address bar only works for you). No AI? Write "No AI used."*

I used ChatGPT as a helper for Part 4. I asked how to write the save_results() function and where to call it in fetch.py.

ChatGPT helped me understand how to open a text file, loop through the artwork list, handle missing artist names, and write each artwork's information on a separate line.

I also asked ChatGPT to review my code and help me understand the results from check.py.

Full AI conversation: https://chatgpt.com/share/6ade827b-6d00-83e8-a58c-2df01d583ed9

**Student:** I need to write a function called `save_results(artworks, filename)` that saves each artwork's title, artist, and date to a text file. How should I do this?

**ChatGPT:** You can use `with open(filename, "w", encoding="utf-8")` to create a text file. Then use a `for` loop to go through the artworks and `file.write()` to write each artwork on a separate line. You should also provide default values for missing information.

```python
def save_results(artworks, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for artwork in artworks:
            title = artwork.get("title") or "Unknown title"
            artist = artwork.get("artist_title") or "Unknown"
            date = artwork.get("date_display") or "Unknown date"

            file.write(f"Title: {title} | Artist: {artist} | Date: {date}\n")
```

### Conversation 2: Calling the Function

**Student:** Where should I call `save_results()` in `fetch.py`?

**ChatGPT:** Call it after the API request succeeds and after you get the artwork list from the JSON response.

```python
if response.status_code == 200:
    data = response.json()
    artworks = data["data"]

    save_results(artworks, "artworks.txt")
    print("Results saved to artworks.txt")
```

This saves the search results whenever the API request succeeds.

### Conversation 3: Testing the Program

**Student:** How can I check whether my function works?

**ChatGPT:** Run `python3 check.py` to test your code. Then run `python3 fetch.py` and enter a search term such as `cat`. Open `artworks.txt` to check whether the file contains the artwork information.

### Conversation 4: Checking the File

**Student:** My `artworks.txt` contains 10 artworks. Each line shows the title, artist, and date. Is this correct?

**ChatGPT:** Yes. Your file follows the requirements. Each artwork is on a separate line, and the required information is included. Missing artist names are correctly displayed as `Unknown`.

### Conversation 5: Making a Manual Change

**Student:** I manually changed this line in my `save_results()` function:

```python
file.write(f"Date: {date} | Title: {title} | Artist: {artist}\n")
```

What should I do next?

**ChatGPT:** Your change is correct. You moved the date to the beginning of each line. Save your code, run `python3 check.py`, and run `python3 fetch.py` again. Then check the updated `artworks.txt` file.

### Conversation 6: Checking the Updated Results

**Student:** I ran the program again. My updated file now contains lines like these:

```text
Date: 1893 | Title: Lion (One of a Pair, South Pedestal) | Artist: Edward Kemeys
Date: 1901 | Title: Nude with Cats | Artist: Pablo Picasso
Date: 17th century | Title: Baroque Pearl Mounted as a Cat Holding a Mouse | Artist: Unknown
```

Is this correct?

**ChatGPT:** Yes. The new file format is correct. The date now appears first, and each line still contains the title and artist. This confirms that your manual change worked.

### Conversation 7: Keeping the Modified Code

**Student:** Do I need to change the code back to the original format?

**ChatGPT:** No. You should keep the modified code because it still meets the assignment requirements. It also demonstrates the manual change you made yourself.

### Conversation 8: Reviewing the AI Log

**Student:** Can you check whether my `ai_log.md` meets all the requirements for full credit?

**ChatGPT:** Your AI log includes all five required sections, but you still need to include the complete AI conversation or a share link. You should also be honest about whether you wrote your prediction before running the function. Your reflection and manual code change meet the requirements.

## 3. Predict, then compare
*before you run the function, write what you think the file will contain for the sample data (`check.py` uses it) or for your search. Then paste what it actually contains. (A wrong prediction gets full credit. Don't edit it after running.)*

Prediction (written before my next run):

I predict that when I run fetch.py and search for cat, the program will create a file called artworks.txt. Each artwork will appear on a separate line, with the date first, followed by the title and artist.

I expect the file to contain artwork information similar to my previous search. If an artwork has no artist name, I expect the program to display Unknown instead of None.

Actual result (complete after running):

After saving my prediction, I ran python3 fetch.py and searched for cat. The program successfully created artworks.txt with the following 10 artworks:

Date: 1893 | Title: Lion (One of a Pair, South Pedestal) | Artist: Edward Kemeys
Date: 1901 | Title: Nude with Cats | Artist: Pablo Picasso
Date: 17th century | Title: Baroque Pearl Mounted as a Cat Holding a Mouse | Artist: Unknown
Date: 1962 | Title: Cat Making Up | Artist: Inagaki Tomoo
Date: c. 1948 | Title: Homesickness | Artist: René Magritte
Date: 1909 | Title: Winter: Cat on a Cushion | Artist: Théophile-Alexandre Pierre Steinlen
Date: 100 BCE–200 CE | Title: Border Fragments | Artist: Nasca
Date: 1977 | Title: The Return of Odysseus (Homage to Pinturicchio and Benin) | Artist: Romare Howard Bearden
Date: 1964 | Title: Lions on the Dreyfus Fund III | Artist: Larry Rivers
Date: 1909 | Title: Summer: Cat on a Balustrade | Artist: Théophile-Alexandre Pierre Steinlen

Comparison (complete after running):

My prediction was correct. The program created artworks.txt, and each artwork appeared on a separate line with the date, title, and artist. The artwork with a missing artist name displayed Unknown instead of None, just as I expected.

This test helped me confirm that my save_results() function works correctly after my manual change.

## 4. What surprised me
*one or two sentences. Where were you wrong, or what did you learn? For example: "I thought a missing artist would print `none`, but `.get` gave the fallback `unknown`."*

I learned that using or "Unknown" can handle missing artist names instead of writing None to the file. I was also surprised that the live API returned 10 artworks, while the sample JSON contained only five.


## 5. Change one thing yourself
*once the function works, change one thing about it by hand, no AI. For example: a different line format (date first), a filename based on the search term, or sorted lines. Write what you changed and why, in one or two sentences.*

I manually changed the line format in the save_results() function. Originally, the file showed the title first, followed by the artist and date. I changed it to show the date first, followed by the title and artist.

I made this change because I think putting the date first makes the information easier to scan.

After running fetch.py again, I checked artworks.txt and confirmed that all 10 artworks were saved in the new format.


