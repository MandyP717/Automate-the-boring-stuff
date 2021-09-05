"""
Regex Search
Write a program that opens all .txt files in a folder and searches for any
line that matches a user-supplied regular expression. The results should
be printed to the screen.
"""

import re
from pathlib import Path, PurePath
import glob
import pprint

# Get all .txt files from current directory
# Put all found files in a list
path = str(Path.cwd() / "*.txt")
txt_file = glob.glob(path)

# Ask user for a regular expression
search_term = input("What are you searching for? \n")
# Loop through all the files to find the supplied expression
found_search_results = {}
for x in txt_file:
    found_search_results[PurePath(x).name] = []
    with open(x, "r") as f:
        for paragraph in f:
            data = paragraph.split(". ")
            for line in data:
                if re.search(rf"\b{search_term}\b", line):
                    found_search_results[PurePath(x).name].append(line)
        f.close()


# Save all found result to a list
# Print the list to show the result
pprint.pprint(found_search_results)
