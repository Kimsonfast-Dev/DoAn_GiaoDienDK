import sys
sys.path.append("./")

import serial
class sv_serial():
    def __init__(self) -> None:
        self.root = serial.Serial()

    def init(self,portname,baudrate):
        self.portname = portname
        self.baudrate = baudrate
        self.root.port = self.portname
        self.root.baudrate = self.baudrate

    def connect(self):
        if(self.root.is_open == 0):
            self.root.open()

    def disconnect(self):
       if(self.root.is_open == 1):
                self.root.close()

    def write(self,data):
        self.root.write(data.encode())

    def read(self):
        data = self.root.readline()
        data = data.decode()
        return data
    

# import time
# hello = sv_serial()
# hello.init("COM8",9600)
# hello.connect()
# while 1:
#     hello.write("hello")


        
