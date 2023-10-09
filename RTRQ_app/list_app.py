import sys
sys.path.append("./")

from RTRQ_app.tool_RTRQ.tool_RTRQ_data import *
import RTRQ_app.manager_RTRQ.list_linkdata as listlink

import service.service_splitFile.main as sv_splitFile

def convertFile():
    f = open("data/data_run/link_current_file.txt","r")
    link = f.readline()
    f.close()
    sv_splitFile.convertFile(link)
    print("tach file thanh cong")

    f= open("service/service_splitFile/data/output/1,info_ct.txt")
    f_w = open("data/data_run/info_file.txt","w")
    for data in f:
        data = data.split("\n")[0]
        data = data.split(",")[1]
        data = data + ","
        f_w.write(data)

    f.close()
    f_w.close()
    obj_element_data(listlink.link_data_element,"SelectFile","sw_page").set("off")