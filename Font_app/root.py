import sys
sys.path.append("./")

import tkinter as tk
from tkinter import *
import Font_app.tab_app.Menu_tab as tab_start
import Font_app.tool_app.tool_resetdata as resetdata
from Font_app.tab_app.Menu_tab import guide

import os
class tkinterApp():
    def __init__(self):
        #setup giao dien
        self.root = tk.Tk()
        self.root.title("Main")
        self.form_size(320,480)
        
        #reset data
        self.reset_data()

        #setup frame
        self.container = tk.Frame(self.root) 
        self.container.pack(side = "top", fill = "both", expand = 1)
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)
        self.show_frame(tab_start.guide)

    def reset_data(self):
        self.link_data = "Font_app/data_app"
        self.listfile_data = os.listdir(self.link_data)
        for folder in self.listfile_data:
            try:
                if(folder.split('.')[1]):
                    None
            except:
                if(folder != "request_element"):
                    resetdata.reset_folder(self.link_data + "/" + folder)
                None
        
    def show_frame(self, cont):
        self.frame = cont(self.container, self)
        self.frame.grid(row = 0, column = 0, sticky ="nsew")
        self.frame.tkraise()

    def form_size(self,Tk_Width,Tk_Height):
        self.width = Tk_Width
        self.height = Tk_Height
        # self.root.maxsize(Tk_Width,Tk_Height)
        # self.root.minsize(Tk_Width,Tk_Height)
        x_Left = int(self.root.winfo_screenwidth()/2 - Tk_Width/2)
        y_Top = int(self.root.winfo_screenheight()/2 - Tk_Height/2)
        self.root.geometry("{}x{}+{}+{}".format(Tk_Width,Tk_Height,x_Left, y_Top))

    
    def move(self,event):
        self.root.geometry(f'+{event.x_root - self.deltax}+{event.y_root-self.deltay}')

    def delta(self,event):
        self.deltax = event.x_root - self.root.winfo_x()
        self.deltay = event.y_root - self.root.winfo_y()

    def close(self):  
        self.reset_data()
        self.root.destroy()
            
    def run(self):
        #self.root.wm_attributes('-fullscreen', 'True')
        self.root.overrideredirect(True); 
        #self.root.attributes("-topmost", True)              
        self.root.mainloop()

def show():
    app = tkinterApp()
    app.run()
    sys.exit()
