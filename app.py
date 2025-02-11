import os
import sys
import pathlib
import shutil
import json
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
        
        # images and icons var
        self.logo_icon = ttk.PhotoImage(file="./images/x-logo2.png")
        self.setting_icon = ttk.PhotoImage(file="./images/setting.png")
        
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
        self.create_file_menu()
        self.main_content()
        # self.side_bar()
        
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
        
        
        
    def set_setting(self, to_set):
        self.settings_container = ttk.Toplevel(title="Setting", iconphoto="./images/setting.png")
        
        # setting functions
        def read_settings():
            with open ("./prop_info/settings.json", "r") as settings_file:
                settings_info = json.load(settings_file)
                return settings_info
            
        def write_setings():
            pass
        
        
        def set_resizable(self):
            if self.settings_screen_resizable:
                self.settings_container.resizable(True, True)
            else:
                self.settings_container.resizable(False, False)
        
        def change_resizable():
            state = resizable_state.get()
            new_settings = read_settings()
            
            new_settings["settings"]["resizable"] = state and True or False
            
            with open(file="./prop_info/settings.json", mode="w") as settings_file:
                json.dump(new_settings, settings_file)
            
            self.settings_screen_resizable = read_settings()["settings"]['resizable']
            set_resizable(self)
            
            
        self.settings_screen_resizable = read_settings()["settings"]['resizable']
        set_resizable(self)
        
        
        # self.settings_container = ttk.Toplevel(title="Setting", iconphoto="./images/setting.png")
        # set_resizable(self)
                
        
            
        # display
        width = round(0.35 * self.screen_width)
        height = round(0.50 * self.screen_height)
        x = round((self.screen_width - width) / 2)
        y = round((self.screen_height - height) / 2)
        self.settings_container.geometry("{}x{}+{}+{}".format(width, height, x, y))
        style = self.settings_container.style
        style.configure(".", font=("Calibri", 12))
        
        
        
        # adding conditional contents
        resizable_state = ttk.IntVar()
        resizable_state.set(self.settings_screen_resizable and 1)
        if (to_set == "view"):
            wrapper = ttk.Frame(master=self.settings_container, padding=20)
            check = ttk.Checkbutton(
                master=wrapper,
                text="Window resizable",
                variable=resizable_state,
                command=change_resizable
            )
            
            check.pack()
            wrapper.pack(fill=BOTH, expand=True)
            
            
        elif (to_set == "history"):
            print("check history")
        elif (to_set == "others"):
            print("other settings")
        else:
            print("unknown settings.")
        
    def view_settings(self):
        self.set_setting("view")
    
    def history_settings(self):
        self.set_setting("history")
    
    def other_settings(self):
        self.set_setting("others")
        
    
    def create_file_menu(self):
        # creating menu
        menu = tk.Menu()
        self.master.config(menu = menu)
        
        # file menu
        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_dialog)
        file_menu.add_command(label="Open folder", command=self.open_folder_dialog)
        # file_menu.add_command(label="Save as", command=self.save_as_dialog)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.destroy)
        menu.add_cascade(label="File", menu=file_menu)
        
        # setting menu
        settings_menu = tk.Menu(master=menu, tearoff=0)
        settings_menu.add_command(label="View", command=self.view_settings)
        settings_menu.add_command(label="History", command=self.history_settings)
        settings_menu.add_command(label="Others", command=self.other_settings)
        
        menu.add_cascade(label="Settings", menu=settings_menu)
    
    
        
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
        
    def side_bar(self):
        container = ttk.Frame(self)
        label = ttk.Label(
            master=container,
            text="Instructions"
        )
        
        label.pack()
        container.pack(fill=X)
    
    def set_display(self):
        # settings
        # setting screen and coordinates
        main.geometry("{}x{}+{}+{}".format(self.frame_width, self.frame_height, self.x, self.y))
        main.iconphoto(False, self.logo_icon)
        
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
    # main = ttk.Window("IX - file renamer", themename="darkly")
    main = ttk.Window("Xchanger", themename="darkly")
    
    app = MainFrame(main)
    main.mainloop()
    
    # ...