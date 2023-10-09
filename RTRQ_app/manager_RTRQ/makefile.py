import sys
import os
sys.path.append("./")

def make(link):
    f = open("RTRQ_app/manager_RTRQ/list_element_request.py","w")
    list_file = os.listdir(link)
    for data in list_file:
        data = data.split(".")[0]
        f.write(data + "=" + '"' + data + '"'+ "\n")

    f.close()
