"""
Write a program that walks through a folder tree and searches for files with
a certain file extension (such as .pdf or .jpg). Copy these files from whatever
location they are in to a new folder.
"""

import pathlib

my_home = input("Please enter your absolute path of the target directory:\n")

# Not possible to search a second filetype. Chain the results together
print(list(pathlib.Path(my_home).glob("**/*.jpg")))
