import sys
sys.path.append("./")

import service.service_serial.main as sv_serial
import service.service_i2c.main as sv_i2c
from RTRQ_app.tool_RTRQ.tool_threading import luong_basic,luong_timer
import time

class sv_CM():
    def __init__(self) -> None:
        None

    def start(self):
        sv_serial.setup("/dev/ttyAMA0",115200)
        sv_serial.disconnect()
        sv_serial.connect()
        self.index_cnc = 0
        self.index_sys = 0
        self.sw_sendfile = 0
        luong1 = luong_timer(0.01,self.getCNC)
        luong1.start()
        self.dataupdate = ""
    
    def sendFile(self,linkfile):
        self.sw_sendfile = 1
        f = open(linkfile,'r')
        list_count = []
        list_line = []
        for count, line in enumerate(f):
            pass
            list_line.append(line)
            list_count.append(count)
        f.close()
        numberline = count
        self.index_sys = 0
        self.index_cnc = 0
        data = ""
        #send line
        while(self.index_cnc<=numberline):
            try:
                if(self.index_cnc == self.index_sys):
                    data = list_line[self.index_cnc]
                    data = str(data).split("\n")[0]
                    self.index_sys = self.index_sys + 1
                line = str(self.index_sys)+","+data
                sv_i2c.send(line)
                time.sleep(0.01)
                
                if(self.index_sys == numberline + 1):
                    self.index_cnc = 0
                    break
            except:
                None
        self.sw_sendfile = 0

    def sendCNC(self,link):
        if(self.sw_sendfile==0):
            self.sendFile(link)

    def getCNC(self):
        data = sv_serial.get()
        if(data != ""):
            data = data.split(",")
            if(data[0]=="setindex"):
                self.index_cnc = int(data[1])
            elif(data[0] == "update_data"):
                self.dataupdate = data
            else:
                print(data)
