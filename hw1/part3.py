# HW1 Part 3: Decisions
# Run it:  python3 part3.py
# Your output must match expected/part3.txt exactly.

from artworks import titles, years

cutoff = 1900  # works made before this year are "old"

# 1. Print the title of every work made after 1900, one per line
for i in range(len(titles)):
    if years[i] > cutoff:
        print(titles[i])

# 2. print old or modern if the work was made before cutoff
print()
count_old = 0
count_modern = 0

for i in range(len(titles)):
    if years[i] < cutoff:
        print(f"{titles[i]}: old")
        count_old += 1
    else: 
        print(f"{titles[i]}: modern")
        count_modern += 1

# 3. print the numbers of old titles and modern titles
print()
print(f"Old: {count_old}")
print(f"Modern: {count_modern}")




