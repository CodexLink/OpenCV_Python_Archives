from tkinter import *
from tkinter import filedialog

root = Tk()

root.withdraw()

initial_file = "test.jpg"
default_ext = ".jpg"
file_types = (("JPEG File", ".jpg"), ("PNG file", ".png"), ("All Files", "."))
directory = filedialog.askopenfilename(
    # directory = filedialog.askopenfile(
    # directory = filedialog.asksaveasfilename(
    initialfile=initial_file,
    defaultextension=default_ext,
    filetypes=file_types,
)
