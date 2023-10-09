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

import Font_app.tab_app.Setting_tab as setting_tab

class guide(tk.Frame): 
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent)

        #GUI EXTIONSION
        ##########################################################################################
        #element extension
        global img,img2,img3,img4,img5,img9,img10

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

        img3 = PhotoImage(file="Font_app/tab_app/icon/fr_movex.png")
        fr_move_x = tk.Label(self,image=img3)
        fr_move_x.place(x=0,y=60,width=320,height=30)

        img4 = PhotoImage(file="Font_app/tab_app/icon/fr_movey.png")
        fr_move_y = tk.Label(self,image=img4)
        fr_move_y.place(x=0,y=90,width=320,height=30)

        img5 = PhotoImage(file="Font_app/tab_app/icon/fr_movez.png")
        fr_move_z = tk.Label(self,image=img5)
        fr_move_z.place(x=0,y=120,width=320,height=30)

        img9 = PhotoImage(file="Font_app/tab_app/icon/btn_down.png")
        img10 = PhotoImage(file="Font_app/tab_app/icon/btn_up.png")

        btn_downX = tk.Label(self,image=img9)
        btn_downX.place(x=196,y=60,width=29,height=29)

        btn_upX = tk.Label(self,image=img10)
        btn_upX.place(x=279,y=60,width=29,height=29)

        btn_downY = tk.Label(self,image=img9)
        btn_downY.place(x=196,y=90,width=29,height=29)

        btn_upY = tk.Label(self,image=img10)
        btn_upY.place(x=279,y=90,width=29,height=29)

        btn_downZ= tk.Label(self,image=img9)
        btn_downZ.place(x=196,y=120,width=29,height=29)

        btn_upZ = tk.Label(self,image=img10)
        btn_upZ.place(x=279,y=120,width=29,height=29)

        lb_X = tk.Label(self)
        lb_X.configure(font=("Regular", 15, "bold"),bg='#50555b',fg="#FFFFFF")
        lb_X.place(x=228,y=63,width=48,height=25)

        lb_Y = tk.Label(self)
        lb_Y.configure(font=("Regular", 15, "bold"),bg='#50555b',fg="#FFFFFF")
        lb_Y.place(x=228,y=93,width=48,height=25)

        lb_Z = tk.Label(self)
        lb_Z.configure(font=("Regular", 15, "bold"),bg='#50555b',fg="#FFFFFF")
        lb_Z.place(x=228,y=123,width=48,height=25)



        #main loop
        def update_interface():
            lb_ValueSpindle.configure(text=lb_ValueSpindle_data.read())
            lb_ValueTime.configure(text=lb_ValueTime_data.read())
            lb_ValueMode.configure(text=lb_ValueMode_data.read())
            lb_ValueX.configure(text=lb_ValueX_data.read())
            lb_ValueY.configure(text=lb_ValueY_data.read())
            lb_ValueZ.configure(text=lb_ValueZ_data.read())
            lb_X.configure(text=lb_ValueX_data.read())
            lb_Y.configure(text=lb_ValueY_data.read())
            lb_Z.configure(text=lb_ValueZ_data.read())
            None

        luong_interface= luong_timer(0.01,update_interface)
        luong_interface.start()

        #main request
        def btn_back_rq(event):
            luong_interface.end()
            controller.show_frame(setting_tab.guide)
            self.destroy()
            None

        def btn_upx_rq(event):
            data = lb_ValueX_data.read()
            if(data != ""):
                x = float(data)
                x = x + 0.1
                x = round(x,1)
                if(x>218): x = 218
                lb_ValueX_data.write(str(x))
                None

        def btn_downx_rq(event):
            data = lb_ValueX_data.read()
            if(data != ""):
                x = float(data)
                x = x - 0.1
                x = round(x,1)
                if(x<0): x=0
                lb_ValueX_data.write(str(x))
                None


        def btn_upy_rq(event):
            data = lb_ValueY_data.read()
            if(data != ""):
                x = float(data)
                x = x + 0.1
                x = round(x,1)
                if(x>235): x = 235
                lb_ValueY_data.write(str(x))
                None
            None

        def btn_downy_rq(event):
            data = lb_ValueY_data.read()
            if(data != ""):
                x = float(data)
                x = x - 0.1
                x = round(x,1)
                if(x<0): x = 0
                lb_ValueY_data.write(str(x))
                None
            None

        def btn_upz_rq(event):
            data = lb_ValueZ_data.read()
            if(data != ""):
                x = float(data)
                x = x + 0.1
                x = round(x,1)
                if(x>50): x = 50
                lb_ValueZ_data.write(str(x))
                None
            None

        def btn_downz_rq(event):
            data = lb_ValueZ_data.read()
            if(data != ""):
                x = float(data)
                x = x - 0.1
                x = round(x,1)
                if(x<0): x = 0
                lb_ValueZ_data.write(str(x))
                None
            None

        btn_back.bind('<Button-1>',btn_back_rq)
        btn_upX.bind('<Button-1>',btn_upx_rq)
        btn_downX.bind('<Button-1>',btn_downx_rq)
        btn_upY.bind('<Button-1>',btn_upy_rq)
        btn_downY.bind('<Button-1>',btn_downy_rq)
        btn_upZ.bind('<Button-1>',btn_upz_rq)
        btn_downZ.bind('<Button-1>',btn_downz_rq)

        
    
        #GUI DEFAULT
        ###################################################################################################
        def close_app(event):
            luong_interface.end()
            controller.close()

        #element default
        defaut.frame_environment(self,controller,"Move")
        defaut.button_close(self,controller,close_app)