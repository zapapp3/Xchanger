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
        
        # setting screen display
        self.set_display()
        self.create_menu()
        self.main_content()
        
        # action point
        self.saved_action = None
        
    
    def run_action(self):
        if self.saved_action:
            print(self.saved_action)
        else:
            print("no action to perform.")
    
    # dialog methods
    def open_dialog(self):
        opened_files = fd.askopenfilenames(
            initialdir="",
            filetypes=[("All files", "*.*")],
            title="Open any file"
        )
        
        self.saved_action = (("files", opened_files))
        
    def save_as_dialog(self):
        pass
        
    def open_folder_dialog(self):
        opened_folder = fd.askdirectory(
            initialdir="",
        )
        
        self.saved_action = (("folder", opened_folder))
    
    def create_menu(self):
        menu = tk.Menu()
        self.master.config(menu = menu)
        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_dialog)
        file_menu.add_command(label="Open folder", command=self.open_folder_dialog)
        file_menu.add_command(label="Save as", command=self.save_as_dialog)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.destroy)
        menu.add_cascade(label="File", menu=file_menu)
        
        
    def main_content(self):
        container = ttk.Frame(self)
        button = ttk.Button(
            master=container,
            text="Fetch",
            bootstyle=(PRIMARY, OUTLINE),
            command=self.run_action,
        )
        
        button.pack()
        container.pack()
    
    def set_display(self):
        # settings
        # setting screen and coordinates
        main.geometry("{}x{}+{}+{}".format(self.frame_width, self.frame_height, self.x, self.y))
        
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
    
    app = MainFrame(main)
    main.mainloop()