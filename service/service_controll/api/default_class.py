import sys
sys.path.append("./")

import service.service_CM.main as sv_CM

class cm_default():
    def __init__(self) -> None:
        self.list_leveling = []
        None
    def sethome(self):
        sv_CM.sendcnc("service/service_controll/data/data_command/set_home.txt")

    def block_drill(self,value):
        if(value == 1): sv_CM.sendcnc("service/service_controll/data/data_command/block_type1.txt")
        if(value == 2): sv_CM.sendcnc("service/service_controll/data/data_command/block_type2.txt")
        if(value == 3): sv_CM.sendcnc("service/service_controll/data/data_command/block_type3.txt")
        if(value == 4): sv_CM.sendcnc("service/service_controll/data/data_command/block_type4.txt")
        if(value == 5): sv_CM.sendcnc("service/service_controll/data/data_command/block_type5.txt")
        if(value == 6): sv_CM.sendcnc("service/service_controll/data/data_command/block_type6.txt")


    def open_drill(self,value):
        if(value == 1): sv_CM.sendcnc("service/service_controll/data/data_command/open_type1.txt")
        if(value == 2): sv_CM.sendcnc("service/service_controll/data/data_command/open_type2.txt")
        if(value == 3): sv_CM.sendcnc("service/service_controll/data/data_command/open_type3.txt")
        if(value == 4): sv_CM.sendcnc("service/service_controll/data/data_command/open_type4.txt")
        if(value == 5): sv_CM.sendcnc("service/service_controll/data/data_command/open_type5.txt")
        if(value == 6): sv_CM.sendcnc("service/service_controll/data/data_command/open_type6.txt")


    def delay_cnc(self):
        sv_CM.sendcnc("service/service_controll/data/data_command/delay_cnc.txt")

    def mono_leveling(self):
        sv_CM.sendcnc("service/service_controll/data/data_command/leveling.txt")

    def move_xy(self,x,y,mode,time):
        f = open("service/service_controll/data/data_command/move_xy.txt",'w')
        f.write("settime," + str(time) + ",0,0\n")
        f.write("setmode," + str(mode) + ",0,0\n")
        f.write("move_xy_cnc," + str(x) + "," + str(y) + "," +str(mode) + "\n")
        f.write("reset,0,0,0")
        f.close()
        sv_CM.sendcnc("service/service_controll/data/data_command/move_xy.txt")

    def move_ready(self):
        sv_CM.sendcnc("service/service_controll/data/data_command/move_ready.txt")
    
    def run_line(self,data):
        f = open("service/service_controll/data/data_command/file_send.txt",'w')
        f.write(data+"\n")
        f.write("reset,0,0,0\n")
        f.close()
        sv_CM.sendcnc("service/service_controll/data/data_command/file_send.txt")
    
        
