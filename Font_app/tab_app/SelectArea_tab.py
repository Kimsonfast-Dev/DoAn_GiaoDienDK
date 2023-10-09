#defaut
import tkinter as tk
from tkinter import ttk as ttk
from tkinter import PhotoImage
#get tool
import sys
sys.path.append("./")

import Font_app.tab_app.defaut as defaut
import Font_app.tab_app.Menu_tab as Menu
import Font_app.tab_app.SelectMode_tab as SelectMode

from Font_app.tool_app.tool_threading import *
from Font_app.tool_app.tool_ManagerData import *

class guide(tk.Frame): 
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent)

        #GUI EXTIONSION
        ##########################################################################################
        #element extension
        lb_areaWork = tk.Label(self,bg="#ECA353")
        lb_areaWork.place(x=30,y=60,width=260,height=360)

        f=open("data/data_run/info_file.txt","r")
        data = f.readline()
        f.close()
        
        data = data.split(",")
        mode = int(data[0])
        ps = int(data[1])
        pcb_width = float(data[2])*8*ps/200/mode*2
        pcb_Height = float(data[3])*8*ps/200/mode*2

        lb_pcb = tk.Label(self,bg="#75A76F")
        lb_pcb.place(x=30,y=60,width=pcb_width,height=pcb_Height)


        data_x = tk.Label(self,text="X:0.0")
        data_x.configure(font=("Regular", 13, "bold"),bg='#4C4C56',fg="#FFFFFF")
        data_x.place(x=15,y=440,w=60,height=25)

        data_y = tk.Label(self,text="y:0.0")
        data_y.configure(font=("Regular", 13, "bold"),bg='#4C4C56',fg="#FFFFFF")
        data_y.place(x=75,y=440,w=60,height=25)

        btn_next = tk.Label(self,text="Next")
        btn_next.configure(bg="#3980DC",fg="#FFFFFF",font=("Regular", 10,"bold"),highlightbackground="#FFFFFF",highlightcolor="#3980DC",highlightthickness=2)
        btn_next.place(x=223,y=438,width=80,height=30)

        #main loop
        def update_interface():
            None

        luong_interface= luong_timer(0.1,update_interface)
        luong_interface.start()

        #main request
        def btn_next_rq(event):
            luong_interface.end()
            controller.show_frame(SelectMode.guide)
            self.destroy()

        def extension2(event):
            None

        def change_lb_pcb(event):
            if(0<event.x<lb_areaWork.winfo_width() and 0<event.y<lb_areaWork.winfo_height()):
                lb_pcb.place(x=event.x + lb_areaWork.winfo_x(),y=event.y + lb_areaWork.winfo_y(),width=pcb_width,height=pcb_Height)
                data_x.configure(text="X:" + str(event.x/2))
                data_y.configure(text="Y:" + str(event.y/2))

        def change_lb_pcb2(event):
            if(0<event.x<lb_areaWork.winfo_width() and 0<event.y<lb_areaWork.winfo_height()):
                lb_pcb.place(x=event.x + lb_areaWork.winfo_x(),y=event.y + lb_areaWork.winfo_y(),width=pcb_width,height=pcb_Height)
                data_x.configure(text="X:" + str(event.x/2))
                data_y.configure(text="Y:" + str(event.y/2))



        lb_areaWork.bind('<ButtonRelease-1>',change_lb_pcb)
        lb_areaWork.bind('<B1-Motion>',change_lb_pcb2)
        btn_next.bind('<Button-1>',btn_next_rq)
    
        #GUI DEFAULT
        ###################################################################################################
        def close_app(event):
            luong_interface.end()
            controller.close()


        def back_app(event):
            luong_interface.end()
            tab_element_data("SelectFile","sw_page").write("on")
            controller.show_frame(Menu.guide)
            self.destroy()

        def next_app(event):
            luong_interface.end()
            controller.show_frame(SelectMode.guide)
            self.destroy()


        #element default
        defaut.frame_environment(self,controller,"Select Area")
        defaut.button_close(self,controller,close_app)

        defaut.button_back(self,controller,back_app)
        defaut.button_next(self,controller,next_app)