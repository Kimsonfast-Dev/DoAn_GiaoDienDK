import sys
sys.path.append("./")
import smbus


class sv_i2c():
    def __init__(self,dcm):
        self.bus = smbus.SMBus(dcm)

    def send_string(self,dcs,val):
        #convert String to byte
        data=[]
        for c in val:
            data.append(ord(c))
            
        #send_data
        self.bus.write_i2c_block_data(dcs,0x00,data)
