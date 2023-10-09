import sys
sys.path.append("./")


class request_data():
    def __init__(self,link) -> None:
        self.link = link

    def get(self):
        f = open(self.link,"r")
        command = f.readline()
        f.close()
        f = open(self.link,"w")
        f.close()
        return command
    
class obj_element_data():
    def __init__(self,link_element,tab_name,element_name) -> None:
        self.link = link_element + tab_name + "," + element_name + ".txt"
        f=open(self.link,"a")
        f.close()

    def set(self,data):
        f = open(self.link,"w")
        f.write(data)
        f.close()

    def setlist(self,list):
        f = open(self.link,"w")
        for data in list:
            f.write(data+"\n")
        f.close()


    def get(self):
        f=open(self.link,"r")
        data = f.readline()
        f.close()
        return data

    def getlist(self):
        data_list = []
        f=open(self.link,"r")
        for data in f:
            data_list.append(data)
        f.close()
        return data_list

        

    