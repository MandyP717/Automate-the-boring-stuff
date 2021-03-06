#! python3
# Given example:
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.
# Self:
# Add option to del keyword -> py.exe mcb.pyw del <keyword>
# Add option to del all keyword -> py.exe mcb.pyw delete

import shelve, pyperclip, sys

mcbShelf = shelve.open("mcb")

# Save clipboard content.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == "save":
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == "del":
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcbShelf.keys())))  # copies all keys to clipboard
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])  # copies saved value to clipboard
    elif sys.argv[1].lower() == "delete":
        mcbShelf.clear()  # clears shelf

mcbShelf.close()
