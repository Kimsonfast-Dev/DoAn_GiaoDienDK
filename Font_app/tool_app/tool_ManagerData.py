import sys 
import os
sys.path.append("./")

class tab_element_data():
    def __init__(self,tab_name,element_name) -> None:
        self.link = "Font_app/data_app/data_element/" + tab_name + "," + element_name + ".txt"
        f=open(self.link,"a")
        f.close()

    def write(self,data):
        f = open(self.link,"w")
        f.write(data)
        f.close()

    def read(self):
        f = open(self.link,"r")
        data = f.readline()
        f.close()
        return data

class tab_element_request():
    def __init__(self,tab_name,element_name) -> None:
        self.element_name = element_name
        self.tab_name = tab_name
        self.link = "Font_app/data_app/request_element/" + self.tab_name + "_" + self.element_name + ".txt"
        f=open(self.link,"a")
        f.close()

    def write(self,data):
        f = open(self.link,"w")
        f.write(data)
        f.close()

    def read(self):
        f = open(self.link,"r")
        data = f.readline()
        f.close()
        return data
    
    def remove(self):
        os.remove(self.link)

    def request(self):
        self.link = "Font_app/data_app/data_request.txt"
        f=open(self.link,"w")
        f.write(self.tab_name + "_" + self.element_name)
        f.close()

class tab_element_value():
    def __init__(self,tab_name,element_name) -> None:
        self.element_name = element_name
        self.tab_name = tab_name
        self.link = "Font_app/data_app/value_element/" + self.tab_name + "," + self.element_name + ".txt"
        f=open(self.link,"a")
        f.close()

    def write(self,datas):
        f = open(self.link,"w")
        for data in datas:
            f.write(data)
        f.close()

    def read(self):
        f = open(self.link,"r")
        datas = []
        for data in f:
            datas.append(data)
        f.close()
        return datas



    



