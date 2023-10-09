import tkinter as tk
from tkinter import *

#element
class button_back():
    def __init__(self,root,controller,func=None):
        global img1
        img1 = PhotoImage(file="Font_app/tab_app/icon/btn_back_icon.png")
        self.func=func
        self.btn = tk.Label(root, image=img1)
        self.btn.place(x=0,y=0,width=30,height=30)
        self.btn.bind('<Button-1>',self.func)

class button_next():
    def __init__(self,root,controller,func = None):
        global img2
        img2 = PhotoImage(file="Font_app/tab_app/icon/btn_next_icon.png")
        self.func=func
        self.btn = tk.Label(root, image=img2)
        self.btn.place(x=30,y=0,width=30,height=30)
        self.btn.bind('<Button-1>',self.func)
    

class button_close():
   def __init__(self,root,controller,func = None):
        global img3
        img3 = PhotoImage(file="Font_app/tab_app/icon/close_icon.png")
        self.func=func
        self.btn = tk.Label(root, image=img3)
        self.btn.place(x=controller.width - 35,y=0,width=30,height=30)
        self.btn.bind('<Button-1>',self.func)
        

class frame_environment():
    def __init__(self,root,controller,text):
        root.configure(bg='#4C4C56')
        #header
        lb_menu = tk.Label(root,text=text)
        lb_menu.configure(font=("Regular", 15, "bold"),bg='#3980DC',fg="#FFFFFF")
        lb_menu.place(x=0,y=0,width=controller.width ,height=30)
        lb_menu.bind('<Button-1>',controller.delta)
        lb_menu.bind('<B1-Motion>',controller.move)





