#defaut
import tkinter as tk
from tkinter import ttk as ttk
from tkinter import PhotoImage
#get tool
import sys
sys.path.append("./")

import Font_app.tab_app.defaut as defaut

from Font_app.tool_app.tool_threading import *
from Font_app.tool_app.tool_ManagerData import *

class guide(tk.Frame): 
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent)

        #GUI EXTIONSION
        ##########################################################################################
        #element extension

        logo = tk.Label(self,text="Hello world", font=("Regular", 25, "bold"),bg='#4C4C56',fg="#9BE5FB")
        logo.place(x=60,y=40,width=200,height=60)
        data_logo = tab_element_data("tab_start","logo")
        data_logo.write("Hello world")


        btn_print = tk.Button(self,text="print", font=("Regular", 25, "bold"),bg='#4C4C56',fg="#9BE5FB")
        btn_print.place(x=60,y=120,width=200,height=60)
        request_btn_print = tab_element_request("tab_start","btn_print")
        btn_print.configure(command=request_btn_print.request)




        #main loop
        def update_interface():
            logo.configure(text=data_logo.read())
            None

        luong_interface= luong_timer(0.1,update_interface)
        luong_interface.start()

        #main request
        def extention1(event):
            None

        def extension2(event):
            None

    
        #GUI DEFAULT
        ###################################################################################################
        def close_app():
            luong_interface.end()
            controller.close()

        #element default
        defaut.frame_environment(self,controller,"Start_page")
        defaut.button_close(self,controller).update_func(close_app)