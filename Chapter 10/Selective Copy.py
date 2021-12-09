"""
Write a program that walks through a folder tree and searches for files with
a certain file extension (such as .pdf or .jpg). Copy these files from whatever
location they are in to a new folder.
"""

from pathlib import *
import tkinter as tk
from tkinter import Button, Entry, Label, Message, StringVar, filedialog
import shutil
from datetime import datetime
import tkinter


def choose_folder(ext):
    if ext != "." and ext != "":
        global extension_files  # cannot return extension files ->declared global
        chosen_folder = Path(tk.filedialog.askdirectory())  # tkinter returns strings
        extension_files = list(
            chosen_folder.glob("**/*{}".format(ext))
        )  # save target files
    else:
        tk.messagebox.showerror(
            title="No extension",
            message="Please fill in the extension you want to find!",
        )


def move_files(path, name):
    if not name:
        name = datetime.now().strftime("%d-%b-%Y (%Hh%Mm%Ss)")
    chosen_folder = Path(tk.filedialog.askdirectory()) / str(name)
    chosen_folder.mkdir(parents=True, exist_ok=True)
    for file in path:
        shutil.copy(file, chosen_folder)
    tkinter.messagebox.showinfo(
        title="Finished", message="Moved found files to map '{}'".format(name)
    )


selected_filepaths = {}

# root window
root = tk.Tk()
root.geometry("300x280")
root.title("Selective Copy")
root.resizable(width=False, height=False)

# Content
# Description of program
intro = Message(
    root,
    text="This program walks through a chosen folder tree and searches for files\
 with the given file extension (such as .pdf or .jpg). It copies the found files\
 to a map located in the chosen destination folder",
    justify="left",
    width=255,
)

# Enter ext to search
label_ext = Label(root, text="Enter target extension: ")
fill_entry = StringVar(root, value=".")
field_ext = Entry(root, textvariable=fill_entry)

# Select folder to search
label_folder = Label(root, text="Select a folder to search: ")
button_folder = Button(
    root,
    text="Select folder",
    command=lambda: choose_folder(field_ext.get()),  # .get() to return str from entry
)

# Enter name for new folder (default is date and time)
folder_name = Label(root, text="Enter name for new folder: ")
folder_field = Entry(root)

# Destination
label_destination = Label(root, text="Choose a folder to save: ")
button_destination = Button(
    root,
    text="Destination Folder",
    command=lambda: move_files(extension_files, folder_field.get()),
)

# Grid of all widgets
intro.grid(column=0, row=0, columnspan=2)
label_ext.grid(column=0, row=1, sticky="w", padx=5, pady=2)
field_ext.grid(column=1, row=1, sticky="e", padx=5, pady=2)
label_folder.grid(column=0, row=2, sticky="w", padx=5, pady=2)
button_folder.grid(column=1, row=2, sticky="e", padx=5, pady=2)
folder_name.grid(column=0, row=3, sticky="w", padx=5, pady=2)
folder_field.grid(column=1, row=3, sticky="e", padx=5, pady=2)
label_destination.grid(column=0, row=4, sticky="w", padx=5, pady=2)
button_destination.grid(column=1, row=4, sticky="e", padx=5, pady=2)


root.mainloop()
