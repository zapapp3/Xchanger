import os
import sys
import pathlib
import shutil
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb


class MainFrame(ttk.Frame):
    def __init__(self, master):
        self.master = master
        super().__init__(self.master, padding=10)
        self.pack(expand=True)
        
        # create form inputs
        # self.form()
        
        # screen variables
        self.screen_width = main.winfo_screenwidth()
        self.screen_height = main.winfo_screenheight()
        
        self.frame_width = round(0.70 * self.screen_width)
        self.frame_height = round(0.80 * self.screen_height)
        self.x = round((self.screen_width - self.frame_width) / 2)
        self.y = round((self.screen_height - self.frame_height) / 2)
        
        self.set_display()
        
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
    
    def create_menu(self):
        pass
    
    
    def set_display(self):
            # settings
        
        
        # setting screen and coordinates
        main.geometry("{}x{}+{}+{}".format(self.frame_width, self.frame_height, self.x, self.y))
        
    def default_text(self):
        container = ttk.Frame(self)
        label = ttk.Label(master=container, text="This is a simple sample text")
        label.pack()
        container.pack(fill=BOTH, expand=True)
        
        
        
if (__name__ == "__main__"):
    main = ttk.Window("IX - file renamer", themename="darkly")
    
    app = MainFrame(main)
    main.mainloop()