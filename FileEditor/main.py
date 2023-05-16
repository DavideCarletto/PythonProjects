import tkinter as tk
from tkinter import filedialog
import os

def edit_file(files_path):
    files = os.listdir(files_path)

    for file_name in files:
        if(file_name.startswith(".")):
            new_file_name = file_name[1:]
            os.rename(files_path+"/"+file_name, files_path+"/"+new_file_name)

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    files_path = filedialog.askdirectory()
    edit_file(files_path)
