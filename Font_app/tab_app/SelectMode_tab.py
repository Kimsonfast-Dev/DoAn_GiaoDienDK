#defaut
import tkinter as tk
from tkinter import ttk as ttk
from tkinter import PhotoImage
#get tool
import sys
sys.path.append("./")

import Font_app.tab_app.defaut as defaut
import Font_app.tab_app.SelectArea_tab as SelectArea
import Font_app.tab_app.Runfile_tab as RunFile

from Font_app.tool_app.tool_threading import *
from Font_app.tool_app.tool_ManagerData import *

class guide(tk.Frame): 
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent)

        #GUI EXTIONSION
        ##########################################################################################
        #element extension
        global img1,img2,img3,img4,img5
        global tick_on,tick_off

        tick_on = PhotoImage(file="Font_app/tab_app/icon/tick_on.png")
        tick_off = PhotoImage(file="Font_app/tab_app/icon/tick_off.png")
        img1 = PhotoImage(file="Font_app/tab_app/icon/ck_icon_line_milling.png")
        img2 = PhotoImage(file="Font_app/tab_app/icon/ck_icon_face_milling.png")
        img3 = PhotoImage(file="Font_app/tab_app/icon/ck_icon_FPR_milling.png")
        img4 = PhotoImage(file="Font_app/tab_app/icon/ck_icon_hole_drilling.png")
        img5 = PhotoImage(file="Font_app/tab_app/icon/ck_icon_line_cutting.png")


        lb_1 = tk.Button(self, image=img1)
        lb_1.place(x=67,y=18+48,width=220,height=50)

        lb_2 = tk.Button(self, image=img2)
        lb_2.place(x=67,y=90+48,width=220,height=50)

        lb_3 = tk.Button(self, image=img3)
        lb_3.place(x=67,y=162+48,width=220,height=50)

        lb_4 = tk.Button(self, image=img4)
        lb_4.place(x=67,y=234+48,width=220,height=50)

        lb_5 = tk.Button(self, image=img5)
        lb_5.place(x=67,y=306+48,width=220,height=50)
        
        chb_1 = tk.Label(self,image = tick_on)
        chb_1.configure(bg="#D9D9D9")
        chb_1.place(x=23,y=74,width=33,height=33)

        chb_2 = tk.Label(self)
        chb_2.configure(bg="#D9D9D9")
        chb_2.place(x=23,y=146,width=33,height=33)

        chb_3 = tk.Label(self)
        chb_3.configure(bg="#D9D9D9")
        chb_3.place(x=23,y=218,width=33,height=33)

        chb_4 = tk.Label(self,image = tick_on)
        chb_4.configure(bg="#D9D9D9")
        chb_4.place(x=23,y=290,width=33,height=33)

        chb_5 = tk.Label(self,image = tick_on)
        chb_5.configure(bg="#D9D9D9")
        chb_5.place(x=23,y=362,width=33,height=33)


        btn_next = tk.Label(self,text="Run")
        btn_next.configure(bg="#3980DC",fg="#FFFFFF",font=("Regular", 10,"bold"),highlightbackground="#FFFFFF",highlightcolor="#3980DC",highlightthickness=2)
        btn_next.place(x=120,y=440,width=80,height=30)





        #main loop
        def update_interface():
            
            None

        luong_interface= luong_timer(0.1,update_interface)
        luong_interface.start()

        #main request
        def btn_next_rq(event):
            luong_interface.end()
            controller.show_frame(RunFile.guide)
            self.destroy()
            None

        def extension2(event):
            None

        btn_next.bind('<Button-1>',btn_next_rq)
    
        #GUI DEFAULT
        ###################################################################################################
        def close_app(event):
            luong_interface.end()
            controller.close()

        def back_app(event):
            luong_interface.end()
            tab_element_data("SelectFile","sw_page").write("on")
            controller.show_frame(SelectArea.guide)
            self.destroy()

        def next_app(event):
            luong_interface.end()
            controller.show_frame(RunFile.guide)
            self.destroy()

        #element default
        defaut.frame_environment(self,controller,"Select Mode")
        defaut.button_close(self,controller,close_app)

        defaut.button_back(self,controller,back_app)
        defaut.button_next(self,controller,next_app)