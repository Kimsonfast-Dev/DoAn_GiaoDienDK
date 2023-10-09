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

import Font_app.tab_app.SelectFile_tab as slfile
import Font_app.tab_app.Setting_tab as setting

class guide(tk.Frame): 
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent)

        #GUI EXTIONSION
        ##########################################################################################
        #element extension

        global img1,img2,img3,img4,img5 
        logo = tk.Label(self,text="ADL CNC", font=("Regular", 25, "bold"),bg='#4C4C56',fg="#9BE5FB")
        logo.place(x=60,y=43,width=200,height=60)

        img1 = PhotoImage(file="Font_app/tab_app/icon/cnc_icon.png")
        btn_phay = tk.Button(self, image = img1)
        btn_phay.place(x=36,y=118,width=110,height=110)

        img2 = PhotoImage(file="Font_app/tab_app/icon/setting_icon.png")
        btn_setting = tk.Button(self, image=img2)
        btn_setting.place(x=174,y=118,width=110,height=110)

        img3 = PhotoImage(file="Font_app/tab_app/icon/info_icon.png")
        btn_info = tk.Button(self, image=img3)
        btn_info.place(x=36,y=244,width=110,height=110)

        img4 = PhotoImage(file="Font_app/tab_app/icon/leveling_icon.png")
        btn_leveling = tk.Button(self,image=img4)
        btn_leveling.place(x=174,y=244,width=110,height=110)


        label_status = tk.Label(self,text="ADL CNC V1 Ready",bg="#4C4C56",fg="#FFFFFF")
        label_status.place(x=0,y=360,width=320,height=30)

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
        def extention1(event):
            None

        def extension2(event):
            None
        
        def btn_phay_rq():
            luong_interface.end()
            controller.show_frame(slfile.guide)
            self.destroy()
            None

        def btn_setting_rq():
            luong_interface.end()
            controller.show_frame(setting.guide)
            self.destroy()
            None

        def btn_info_rq():
            luong_interface.end()
            controller.show_frame(slfile.guide)
            self.destroy()
            None

        def btn_leveling_rq():
            lb_ValueSpindle_data.write("0")
            lb_ValueTime_data.write("0")
            lb_ValueMode_data.write("0")
            lb_ValueX_data.write("0")
            lb_ValueY_data.write("0")
            lb_ValueZ_data.write("0")
            None

        btn_phay.configure(command=btn_phay_rq)
        btn_setting.configure(command=btn_setting_rq)
        btn_info.configure(command=btn_info_rq)
        btn_leveling.configure(command=btn_leveling_rq)
    
        #GUI DEFAULT
        ###################################################################################################
        def close_app(event):
            luong_interface.end()
            controller.close()

        #element default
        defaut.frame_environment(self,controller,"Main menu")
        defaut.button_close(self,controller,close_app)
