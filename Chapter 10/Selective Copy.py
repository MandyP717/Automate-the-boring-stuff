"""
Write a program that walks through a folder tree and searches for files with
a certain file extension (such as .pdf or .jpg). Copy these files from whatever
location they are in to a new folder.
"""

import pathlib
import tkinter as tk
from tkinter import Button, Entry, Label, Message, filedialog


def choose_folder():
    tk.filedialog.askdirectory()


# root window
root = tk.Tk()
root.geometry("285x300")
root.title("Selective Copy")
root.resizable(width=False, height=False)

# Content
# Description of program
intro = Message(
    root,
    text="Write a program that walks through a folder tree and searches for files\
 with a certain file extension (such as .pdf or .jpg). Copy these files from\
 whatever location they are in to a new folder.",
    justify="left",
    width=250,
)

# Enter ext to search
label_ext = Label(root, text="Enter target extension: ")
button_ext = Entry(root)

# Select folder to search
label_folder = Label(root, text="Select a folder to search: ")
button_folder = Button(root, text="Select folder", command=choose_folder)

# Destination
label_destination = Label(root, text="Choose a folder to save: ")
button_destination = Button(root, text="Destination Folder", command=choose_folder)

# Grid of all widgets
intro.grid(column=0, row=0, columnspan=2)
label_ext.grid(column=0, row=1, sticky="w", padx=5, pady=2)
button_ext.grid(column=1, row=1, sticky="e", padx=5, pady=2)
label_folder.grid(column=0, row=2, sticky="w", padx=5, pady=2)
button_folder.grid(column=1, row=2, sticky="e", padx=5, pady=2)
label_destination.grid(column=0, row=3, sticky="w", padx=5, pady=2)
button_destination.grid(column=1, row=3, sticky="e", padx=5, pady=2)


root.mainloop()
