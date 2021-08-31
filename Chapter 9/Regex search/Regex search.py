"""
Regex Search
Write a program that opens all .txt files in a folder and searches for any
line that matches a user-supplied regular expression. The results should
be printed to the screen.
"""

import re
from pathlib import Path, PurePath
import glob

# Get all .txt files from current directory
path = str(Path.cwd() / "*.txt")

# Put all found files in a list
txt_file = glob.glob(path)

# Ask user for a regular expression
search_term = input("What are you searching for? \n")
# Loop through all the files to find the supplied expression
found_search_results = {}
for x in txt_file:
    with open(x, "r") as f:
        read_stuff = f.read()
        search_results = re.findall(search_term, read_stuff)
        found_search_results[PurePath(x).name] = search_results
        f.close()


# Save all found result to a list
# Print the list to show the result
print(found_search_results)
