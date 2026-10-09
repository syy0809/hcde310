# HW1 Part 2: Lists and loops
# Run it:  python3 part2.py
# Your output must match expected/part2.txt exactly.

from artworks import titles
# 1. print each title on its own line starting from number 1 
for i in range (len(titles)):
    print(f"{i + 1}. {titles[i]}")

# 2. print the total number of the titles
print(f"Titles: {len(titles)}")

# 3. count titles containing "a" in upper or lower case
count = 0
for title in titles:
    if "a" in title.lower():
        count += 1
print(f'Titles with an "a": {count}')

# 4. print the longest title
longest = ""
for title in titles:
    if len(title) > len(longest):
        longest = title
print(f"Longest: {longest}")




