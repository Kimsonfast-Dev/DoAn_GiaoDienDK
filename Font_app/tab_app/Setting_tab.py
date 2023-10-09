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
import Font_app.tab_app.Move_tab as move_tab
import Font_app.tab_app.UnitControl_tab as unit_tab
import Font_app.tab_app.Menu_tab as menu_tab

class guide(tk.Frame): 
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent)

        #GUI EXTIONSION
        ##########################################################################################
        #element extension
        global img1,img2,img3,img4,img5,img6
        img1 = PhotoImage(file="Font_app/tab_app/icon/fr_panel.png")
        fr_panel = tk.Label(self,image=img1)
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

        img2 = PhotoImage(file="Font_app/tab_app/icon/btn_back.png")
        btn_back = tk.Label(self,image=img2)
        btn_back.place(x=0,y=30,width=320,height=30)

        img3 = PhotoImage(file="Font_app/tab_app/icon/btn_sethome.png")
        btn_sethome = tk.Label(self,image=img3)
        btn_sethome.place(x=0,y=60,width=320,height=30)

        img4 = PhotoImage(file="Font_app/tab_app/icon/btn_disablestepper.png")
        btn_disablestepper = tk.Label(self,image=img4)
        btn_disablestepper.place(x=0,y=90,width=320,height=30)

        img5 = PhotoImage(file="Font_app/tab_app/icon/btn_move.png")
        btn_move = tk.Label(self,image=img5)
        btn_move.place(x=0,y=120,width=320,height=30)

        img6 = PhotoImage(file="Font_app/tab_app/icon/btn_unitcontroll.png")
        btn_unitcontroll = tk.Label(self,image=img6)
        btn_unitcontroll.place(x=0,y=150,width=320,height=30)

        #main loop
        def update_interface():
            lb_ValueSpindle.configure(text=lb_ValueSpindle_data.read())
            lb_ValueTime.configure(text=lb_ValueTime_data.read())
            lb_ValueMode.configure(text=lb_ValueMode_data.read())
            lb_ValueX.configure(text=lb_ValueX_data.read())
            lb_ValueY.configure(text=lb_ValueY_data.read())
            lb_ValueZ.configure(text=lb_ValueZ_data.read())
            None

        luong_interface= luong_timer(0.1,update_interface)
        luong_interface.start()

        #main request
        def btn_move_rq(event):
            luong_interface.end()
            controller.show_frame(move_tab.guide)
            self.destroy()
            None

        def btn_unitcontroll_rq(event):
            luong_interface.end()
            controller.show_frame(unit_tab.guide)
            self.destroy()
            None

        def btn_back_rq(event):
            luong_interface.end()
            controller.show_frame(menu_tab.guide)
            self.destroy()
            None

        btn_move.bind('<Button-1>',btn_move_rq)
        btn_unitcontroll.bind('<Button-1>',btn_unitcontroll_rq)
        btn_back.bind('<Button-1>',btn_back_rq)
    
        #GUI DEFAULT
        ###################################################################################################
        def close_app(event):
            luong_interface.end()
            controller.close()

        #element default
        defaut.frame_environment(self,controller,"Setting")
        defaut.button_close(self,controller,close_app)