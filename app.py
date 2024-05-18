import os
import sys
import pathlib
import shutil
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class MainFrame(ttk.Frame):
    def __init__(self, master, frame_width, frame_height):
        super().__init__(master, padding=10)
        self.pack(expand=True)
        
        # vars
        self.frame_width = frame_width
        self.frame_height = frame_height
        
        # create form inputs
        self.form()
        
    def form(self):
        name = self.input_field("Name")
        email = self.input_field("Email ID")
    
    def input_field(self, title):
        container = ttk.Frame(master=self)
        label = ttk.Label(master=container, text=title)
        entry = ttk.Entry(master=container, width=round(0.05 * self.frame_width))
        label.pack(side=LEFT)
        entry.pack(side=RIGHT, padx=(10, 0))
        container.pack(fill=BOTH, expand=True, pady=7)
        return entry
        
    def default_text(self):
        container = ttk.Frame(self)
        label = ttk.Label(master=container, text="This is a simple sample text")
        label.pack()
        container.pack(fill=BOTH, expand=True)
        
        
        
if (__name__ == "__main__"):
    main = ttk.Window("IX - file renamer", themename="darkly")
    # settings
    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()
    
    frame_width = round(0.70 * screen_width)
    frame_height = round(0.80 * screen_height)
    x = round((screen_width - frame_width) / 2)
    y = round((screen_height - frame_height) / 2)
    print(x, y)
    
    # main.geometry("{}x{}+{}+{}".format(frame_width, frame_height, x, y))
    main.geometry("{}x{}+{}+{}".format(frame_width, frame_height, x, y))
    
    app = MainFrame(main, frame_width, frame_height)
    main.mainloop()