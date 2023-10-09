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
        global img5

        f = open("data/data_run/link_current_file.txt")
        data = f.readline().split("/")[-1]
        f.close()

        percen = tk.Label(self)
        percen.configure(bg="#D9D9D9")
        percen.place(x=15,y=165,w=280,height=20)

        btn_next = tk.Label(self,text="Run")
        btn_next.configure(bg="#3980DC",fg="#FFFFFF",font=("Regular", 10,"bold"),highlightbackground="#FFFFFF",highlightcolor="#3980DC",highlightthickness=2)
        btn_next.place(x=121,y=190,width=80,height=30)

        label_title = tk.Label(self,text=data)
        label_title.configure(bg="#4C4C56",fg="#FFFFFF")
        label_title.place(x=0,y=134,w=320,h=30)

        img5 = PhotoImage(file="Font_app/tab_app/icon/fr_panel.png")
        fr_panel = tk.Label(self,image=img5)
        fr_panel.place(x=0,y=420,width=320,height=60)

        lb_ValueSpindle = tk.Label(self,text="200")
        lb_ValueSpindle.configure(font=("Regular", 15, "bold"),bg='#4C4C56',fg="#FFFFFF")
        lb_ValueSpindle.place(x=41,y=428,width=48,height=25)
        lb_ValueSpindle_data = tab_element_data("panel","v_spindle")

        lb_ValueTime = tk.Label(self,text="2000")
        lb_ValueTime.configure(font=("Regular", 15, "bold"),bg='#4C4C56',fg="#FFFFFF")
        lb_ValueTime.place(x=153,y=428,width=48,height=25)
        lb_ValueTime_data = tab_element_data("panel","v_time")

        lb_ValueMode = tk.Label(self,text="32")
        lb_ValueMode.configure(font=("Regular", 15, "bold"),bg='#4C4C56',fg="#FFFFFF")
        lb_ValueMode.place(x=260,y=428,width=48,height=25)
        lb_ValueMode_data = tab_element_data("panel","v_mode")

        lb_ValueX = tk.Label(self,text="10.3")
        lb_ValueX.configure(font=("Regular", 15, "bold"),bg='#4C4C56',fg="#FFFFFF")
        lb_ValueX.place(x=41,y=452,width=48,height=25)
        lb_ValueX_data = tab_element_data("panel","v_x")

        lb_ValueY = tk.Label(self,text="20.3")
        lb_ValueY.configure(font=("Regular", 15, "bold"),bg='#4C4C56',fg="#FFFFFF")
        lb_ValueY.place(x=153,y=452,width=48,height=25)
        lb_ValueY_data = tab_element_data("panel","v_y")

        lb_ValueZ= tk.Label(self,text="45.53")
        lb_ValueZ.configure(font=("Regular", 15, "bold"),bg='#4C4C56',fg="#FFFFFF")
        lb_ValueZ.place(x=260,y=452,width=48,height=25)
        lb_ValueZ_data = tab_element_data("panel","v_z")

        global sw_bt
        sw_bt = 0
        def btn_next_rq(event):
            global sw_bt
            sw_bt = 1-sw_bt
            if(sw_bt==1):
                btn_next.configure(text="Pause")
                label_title.configure(text="Running..........")
            else:
                f = open("data/data_run/link_current_file.txt")
                data = f.readline().split("/")[-1]
                f.close()
                btn_next.configure(text="Run")
                label_title.configure(text=data)



        btn_next.bind('<Button-1>',btn_next_rq)



        #main loop
        def update_interface():
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
        def close_app(event):
            luong_interface.end()
            controller.close()

        #element default
        defaut.frame_environment(self,controller,"Run File")
        defaut.button_close(self,controller,close_app)