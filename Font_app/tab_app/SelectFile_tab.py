#defaut
import tkinter as tk
from tkinter import ttk as ttk
from tkinter import PhotoImage
#get tool
import sys
sys.path.append("./")

import Font_app.tab_app.defaut as defaut
import Font_app.tab_app.Menu_tab as Menu
import Font_app.tab_app.SelectArea_tab as SelectArea

from Font_app.tool_app.tool_threading import *
from Font_app.tool_app.tool_ManagerData import *

class guide(tk.Frame): 
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent)

        #GUI EXTIONSION
        ##########################################################################################
        #element extension
        lb = tk.Listbox(self,yscrollcommand=True)
        lb.configure(highlightbackground="#4C4C56",highlightthickness=5,highlightcolor="#4C4C56",font=("Regular", 10,"bold"))
        lb.place(x=0,y=30,width=320,height=406)

        btn_selectfile = tk.Label(self,text="Select")
        btn_selectfile.configure(bg="#3980DC",fg="#FFFFFF",font=("Regular", 10,"bold"),highlightbackground="#FFFFFF",highlightcolor="#3980DC",highlightthickness=2)
        btn_selectfile.place(x=120,y=440,width=80,height=30)
        btn_selectfile_request = tab_element_request("SelectFile","btn_selectfile")
        sw_page = tab_element_data("SelectFile","sw_page")

        #ready
        import os
        global linkfolder
        linkfolder = "data/data_file"

        data = os.listdir(linkfolder)
        for filename in data:
            lb.insert("end",filename)

        #main loop
        def update_interface():
            None

        luong_interface= luong_timer(0.1,update_interface)
        luong_interface.start()

        #main request
        def btn_selectfile_rq(event):
            nameFile = ""
            for i in lb.curselection():
                nameFile = lb.get(i)
            None
            line = linkfolder + "/" + nameFile
            f = open("data/data_run/link_current_file.txt","w")
            f.write(line)
            f.close()
            btn_selectfile_request.request()

        def chuyentrang():
            if(sw_page.read() == "off"):
                luong_interface.end()
                luong_kt.end()
                controller.show_frame(SelectArea.guide)
                self.destroy()
            None

        luong_kt= luong_timer(1,chuyentrang)
        luong_kt.start()




        def extension2(event):
            None

        btn_selectfile.bind('<Button-1>',btn_selectfile_rq)

        #GUI DEFAULT
        ###################################################################################################
        def close_app(event):
            luong_interface.end()
            controller.close()
        
        def back_app(event):
            luong_interface.end()
            controller.show_frame(Menu.guide)
            self.destroy()

        #element default
        defaut.frame_environment(self,controller,"Select file")
        defaut.button_close(self,controller,close_app)
        
        defaut.button_back(self,controller,back_app)
        #defaut.button_next(self,controller,page2)