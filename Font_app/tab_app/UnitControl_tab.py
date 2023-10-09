#defaut
import tkinter as tk
from tkinter import ttk as ttk
from tkinter import PhotoImage
#get tool
import sys
sys.path.append("./")

import Font_app.tab_app.defaut as defaut
import Font_app.tab_app.Setting_tab as setting_tab

from Font_app.tool_app.tool_threading import *
from Font_app.tool_app.tool_ManagerData import *


class guide(tk.Frame): 
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent)

        #GUI EXTIONSION
        ##########################################################################################
        #element extension

        global img,img2,img3,img4,img5,img6,img7,img8,img9,img10

        img = PhotoImage(file="Font_app/tab_app/icon/fr_panel.png")
        fr_panel = tk.Label(self,image=img)
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

        img5 = PhotoImage(file="Font_app/tab_app/icon/btn_enablestepper.png")
        btn_enablestepper = tk.Label(self,image=img5)
        btn_enablestepper.place(x=0,y=120,width=320,height=30)  

        img6 = PhotoImage(file="Font_app/tab_app/icon/btn_settime.png")
        fr_settime = tk.Label(self,image=img6)
        fr_settime.place(x=0,y=150,width=320,height=30)  

        img7 = PhotoImage(file="Font_app/tab_app/icon/btn_setmode.png")
        fr_setmode = tk.Label(self,image=img7)
        fr_setmode.place(x=0,y=180,width=320,height=30)  

        img8 = PhotoImage(file="Font_app/tab_app/icon/btn_setspindle.png")
        fr_setspindle = tk.Label(self,image=img8)
        fr_setspindle.place(x=0,y=210,width=320,height=30)  

        img9 = PhotoImage(file="Font_app/tab_app/icon/btn_down.png")
        img10 = PhotoImage(file="Font_app/tab_app/icon/btn_up.png")

        btn_downTime = tk.Label(self,image=img9)
        btn_downTime.place(x=196,y=150,width=29,height=29)

        btn_upTime = tk.Label(self,image=img10)
        btn_upTime.place(x=279,y=150,width=29,height=29)

        btn_downMode = tk.Label(self,image=img9)
        btn_downMode.place(x=196,y=180,width=29,height=29)

        btn_upMode = tk.Label(self,image=img10)
        btn_upMode.place(x=279,y=180,width=29,height=29)

        btn_downspindle = tk.Label(self,image=img9)
        btn_downspindle.place(x=196,y=210,width=29,height=29)

        btn_upspindle = tk.Label(self,image=img10)
        btn_upspindle.place(x=279,y=210,width=29,height=29)

        lb_Time = tk.Label(self)
        lb_Time.configure(font=("Regular", 15, "bold"),bg='#50555b',fg="#FFFFFF")
        lb_Time.place(x=228,y=153,width=48,height=25)

        lb_mode = tk.Label(self)
        lb_mode.configure(font=("Regular", 15, "bold"),bg='#50555b',fg="#FFFFFF")
        lb_mode.place(x=228,y=183,width=48,height=25)

        lb_spindle = tk.Label(self)
        lb_spindle.configure(font=("Regular", 15, "bold"),bg='#50555b',fg="#FFFFFF")
        lb_spindle.place(x=228,y=213,width=48,height=25)



        #main loop
        def update_interface():
            lb_ValueSpindle.configure(text=lb_ValueSpindle_data.read())
            lb_ValueTime.configure(text=lb_ValueTime_data.read())
            lb_ValueMode.configure(text=lb_ValueMode_data.read())
            lb_Time.configure(text=lb_ValueTime_data.read())
            lb_mode.configure(text=lb_ValueMode_data.read())
            lb_spindle.configure(text=lb_ValueSpindle_data.read())
            lb_ValueX.configure(text=lb_ValueX_data.read())
            lb_ValueY.configure(text=lb_ValueY_data.read())
            lb_ValueZ.configure(text=lb_ValueZ_data.read())
            None

        luong_interface= luong_timer(0.1,update_interface)
        luong_interface.start()

        global index_mode
        index_mode = 0
        list_mode = [1,2,4,8,16,32]

        #main request
        def btn_back_rq(event):
            luong_interface.end()
            controller.show_frame(setting_tab.guide)
            self.destroy()
            None

        btn_back.bind('<Button-1>',btn_back_rq)

        def btn_back_rq(event):
            luong_interface.end()
            controller.show_frame(setting_tab.guide)
            self.destroy()
            None

        def btn_uptime_rq(event):
            data = lb_ValueTime_data.read()
            if(data != ""):
                x = int(data)
                x = x + 100
                if(x>3000): x = 3000
                lb_ValueTime_data.write(str(x))
                None

        def btn_downtime_rq(event):
            data = lb_ValueTime_data.read()
            if(data != ""):
                x = int(data)
                x = x - 100
                if(x<0): x=0
                lb_ValueTime_data.write(str(x))
                None


        def btn_upmode_rq(event):
            global index_mode
            index_mode = index_mode + 1
            if(index_mode > 5): index_mode = 5
            lb_ValueMode_data.write(str(list_mode[index_mode]))

        def btn_downmode_rq(event):
            global index_mode
            index_mode = index_mode - 1
            if(index_mode < 0): index_mode = 0
            lb_ValueMode_data.write(str(list_mode[index_mode]))

        def btn_upspindle_rq(event):
            data = lb_ValueSpindle_data.read()
            if(data != ""):
                x = float(data)
                x = x + 1
                x = round(x)
                if(x>255): x = 255
                lb_ValueSpindle_data.write(str(x))
                None
            None

        def btn_downspindle_rq(event):
            data = lb_ValueSpindle_data.read()
            if(data != ""):
                x = float(data)
                x = x - 1
                x = round(x)
                if(x<0): x = 0
                lb_ValueSpindle_data.write(str(x))
                None
            None

        btn_back.bind('<Button-1>',btn_back_rq)
        btn_upTime.bind('<Button-1>',btn_uptime_rq)
        btn_downTime.bind('<Button-1>',btn_downtime_rq)
        btn_upMode.bind('<Button-1>',btn_upmode_rq)
        btn_downMode.bind('<Button-1>',btn_downmode_rq)
        btn_upspindle.bind('<Button-1>',btn_upspindle_rq)
        btn_downspindle.bind('<Button-1>',btn_downspindle_rq)

    
        #GUI DEFAULT
        ###################################################################################################
        def close_app(event):
            luong_interface.end()
            controller.close()

        #element default
        defaut.frame_environment(self,controller,"Unit controll")
        defaut.button_close(self,controller,close_app)