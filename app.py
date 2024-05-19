import os
import sys
import pathlib
import shutil
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class MainFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=10)
        self.pack(fill=BOTH, expand=True)
        self.default_text()
        
    def default_text(self):
        container = ttk.Frame(self)
        label = ttk.Label(master=container, text="This is a simple sample text")
        label.pack()
        container.pack(fill=BOTH, expand=True)
        
        
        
if (__name__ == "__main__"):
    main = ttk.Window("IX - file renamer", themename="darkly")
    app = MainFrame(main)
    main.mainloop()
    
    # ...