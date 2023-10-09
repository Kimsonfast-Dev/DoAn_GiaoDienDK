import sys
sys.path.append("./")

import os
from service.service_controll.api.default_class import cm_default as mg_command
from service.service_controll.api.default_class import sv_CM as svcm
import service.service_controll.tool.tool_convert_file as tool_cv


class sv_controll():
    def __init__(self) -> None:
        self.mg_command = mg_command()

    def runfile(self,filename):
        linkfoder = "service/service_controll/data/data_runfile/"
        if(filename == "2,millingline_ct.txt"):
            #self.sethome()
            #self.mg_command.block_drill(1)
            self.leveling()
            self.converfile()
            self.mg_command.run_line("move_ready,0,0,0")
            self.mg_command.run_line("delay_cnc,3000,0,0")
            self.mg_command.run_line("milling,120,0,0")
            linkfile = linkfoder + filename
            svcm.sendcnc(linkfile)
            self.mg_command.run_line("milling,0,0,0")
            self.mg_command.run_line("move_ready,0,0,0")
            #@self.sethome()
            #self.mg_command.open_drill(1)


        if(filename == "6,cuttingline_ct.txt"):
            self.sethome() 
            self.mg_command.block_drill(1)
            self.leveling()
            self.converfile()
            #self.mg_command.run_line("milling,250,0,0")
            self.mg_command.run_line("settime,20,0,0")
            self.mg_command.run_line("setmode,32,0,0")
            linkfile = linkfoder + filename
            svcm.sendcnc(linkfile)
            self.mg_command.run_line("milling,0,0,0")
            self.sethome()
            self.mg_command.open_drill(1)

        elif(filename == "5,drillhole_ct.txt"):
            linkfile = linkfoder + filename
            f = open(linkfile,"r")
            for data in f:
                data = data.split(",")
                if(data[0] == "block"):
                    type = int(data[1])
                    self.mg_command.block_drill(type)
                    self.mg_command.sethome()
                    self.mg_command.mono_leveling()
                elif(data[0] == "open"):
                    type = int(data[1])
                    self.mg_command.open_drill(type)
                else:
                    mg_command.run_line(data)

    def running(self):
        #self.runfile("2,millingline_ct.txt")
        #self.runfile("6,cuttingline_ct.txt")
        None
    
    def test_thaydao(self,value):
        self.mg_command.block_drill(value)
        self.mg_command.open_drill(value)

    def converfile(self):
        link_folder = "service/service_splitFile/data/output"
        listfile = os.listdir(link_folder)
        for filename in listfile:
            linkfile = link_folder + "/" + filename
            if(filename.split(",")[0] != "1" and filename.split(",")[0] != "3" and filename.split(",")[0] != "4"):
                tool_cv.update_mapping()
                tool_cv.convert_file(linkfile,4)
            else:
                if(filename.split(",")[0]):
                    None
    
    def leveling_map(self):
        f = open("service/service_controll/data/data_cnc/list_xy_leveling.txt",'r')
        f_file = open("service/service_controll/data/data_cnc/list_leveling.txt",'w')
        self.sethome()
        #self.mg_command.block_drill(1)
        for data in f:
            x = float(data.split(",")[1])
            y = float(data.split(",")[2])
            self.move_xy(x,y,32,20)
            self.mg_command.mono_leveling()
            data = svcm.getcnc()
            self.mg_command.move_ready()
            data = str(data).split(",")
            z = data[3].split("'")[1]
            line = str(x) + "," + str(y) + "," + z + '\n'
            print(line)
            f_file.write(line)
        f_file.close()
        f.close()

        f_file = open("service/service_controll/data/data_cnc/value_lv_mapping.txt",'w')
        f = open("service/service_controll/data/data_cnc/list_leveling.txt",'r')
        f_file.write(f.readline().split(",")[2])
        f.close()
        f_file.close()
        
        self.sethome()
        #self.mg_command.open_drill(1)
        

    def leveling(self):
        self.sethome()
        self.mg_command.mono_leveling()
        f_file = open("service/service_controll/data/data_cnc/value_lv_current.txt",'w')
        data = svcm.getcnc()
        z = data[3]
        f_file.write(z)
        f_file.close()
        None

    def sethome(self):
        self.mg_command.sethome()
    
    def open_drill(self,value):
        self.mg_command.open_drill(value)

    def block_drill(self,value):
        self.mg_command.block_drill(value)

    def move_xy(self,x,y,mode,settime):
        self.mg_command.move_xy(x,y,mode,settime)
    def run_cm(self,data):
        self.mg_command.run_line(data)

