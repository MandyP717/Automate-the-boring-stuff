"""
Create a Mad Libs program that reads in text files and lets the user add
their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
appears in the text file. For example, a text file may look like this:

The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.

The program would find these occurrences and prompt the user to
replace them.

Enter an adjective:
silly

Enter a noun:
chandelier

Enter a verb:
screamed

Enter a noun:
pickup truck

The following text file would then be created:
The silly panda walked to the chandelier and then screamed. A nearby pickup
truck was unaffected by these events.
The results should be printed to the screen and saved to a new text file.
"""

from pathlib import Path, PurePath
import glob
import re


def text_menu(dictionary):  # Menu design
    print(30 * "-", "Please pick a text file to read", 30 * "-")
    for k, v in dictionary.items():
        print(f"{k}:", PurePath(v).name)  # Doesn't print the whole path only filename
    print(93 * "-")


def chosen_option(dictionary):
    loop = True
    while loop:
        try:
            choice = int(input("Please enter your choice here [a number]: \n"))
            if choice > len(dictionary):
                print("Please pick a number displayed in the menu.")
                continue
        except ValueError:  # When choice can't be turned into integer
            print("Please enter an integer")
        else:
            loop = False
    return choice


# Find .txt files in the current work directory
path = str(Path.cwd() / "*.txt")  # Glob doesn't accept PATH

# Put all found .txt in dictionary
menu_txt_files = {count + 1: link for count, link in enumerate(glob.glob(path))}
text_menu(menu_txt_files)

# Read the chosen specific file
chosen_file = menu_txt_files[chosen_option(menu_txt_files)]  # validates input
read_file = Path(chosen_file).read_text()
print(f"You have picked [{PurePath(chosen_file).name}] to read:")
print(read_file)

# Find ADJECTIVE/VERB/NOUN, if found give a prompt (use regex)
# Lets user change it
new_sentence = []
pattern_mine = re.compile(r"NOUN|VERB|ADJECTIVE|ADVERB")
for word in read_file.split():
    first_search = re.search(pattern_mine, word)
    if bool(first_search):
        change_it = input(f"\nEnter a {first_search.group().lower()}: \n")
        subbed_word = re.sub(pattern_mine, change_it, word)
        new_sentence.append(subbed_word)
    else:
        new_sentence.append(word)

# Print the result
new_sentence = ' '.join(new_sentence)
print("\nYour filled in sentence is:")
print(f'{new_sentence} \n')

# Save the result to a new text file
with open(input("Choose a name for your new text file: \n"), "w") as f:
    f.write(new_sentence)
    f.close()
