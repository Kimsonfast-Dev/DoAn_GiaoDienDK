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
        logo.place(x=10,y=40,width=300,height=400)
        data_logo = tab_element_data("tab_start","logo")
        data_logo.write("")

        
        point = tk.Label(self,text="", font=("Regular", 25, "bold"),bg='#BA0C0C',fg="#9BE5FB")
        point.place(x=10,y=50,width=10,height=10)

        data_x = tk.Label(self,text="0", font=("Regular", 13, "bold"),bg='#BA0C0C',fg="#9BE5FB")
        data_x.place(x=0,y=450,width=80,height=30)

        data_y = tk.Label(self,text="0", font=("Regular", 13, "bold"),bg='#BA0C0C',fg="#9BE5FB")
        data_y.place(x=90,y=450,width=80,height=30)
        # point_logo = tab_element_data("tab_start","logo")
        # point_logo.write("")


        # btn_print = tk.Button(self,text="print", font=("Regular", 25, "bold"),bg='#4C4C56',fg="#9BE5FB")
        # btn_print.place(x=60,y=120,width=200,height=60)
        # request_btn_print = tab_element_request("tab_start","btn_print")
        # btn_print.configure(command=request_btn_print.request)




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

        def change_point(event):
            if(0<event.x<300 and 0<event.y<400):
                point.place(x=event.x + logo.winfo_x() - point.winfo_width()/2,y=event.y + logo.winfo_y() - point.winfo_height()/2,width=10,height=10)
                data_x.configure(text=str(event.x/2))
                data_y.configure(text=str(event.y/2))
            # print(point.winfo_x()+point.winfo_width()/2-logo.winfo_x(),point.winfo_y()+point.winfo_height()/2-logo.winfo_y())

        def change_point2(event):
            if(0<event.x<300 and 0<event.y<400):
                point.place(x=event.x + logo.winfo_x() - point.winfo_width()/2,y=event.y + logo.winfo_y() - point.winfo_height()/2,width=10,height=10)
                data_x.configure(text=str(event.x/2))
                data_y.configure(text=str(event.y/2))

        logo.bind('<ButtonRelease-1>',change_point)
        logo.bind('<B1-Motion>',change_point2)
    
        #GUI DEFAULT
        ###################################################################################################
        def close_app():
            luong_interface.end()
            controller.close()

        #element default
        defaut.frame_environment(self,controller,"Start_page")
        defaut.button_close(self,controller).update_func(close_app)