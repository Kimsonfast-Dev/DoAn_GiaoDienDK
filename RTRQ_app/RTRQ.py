import sys
sys.path.append("./")

import RTRQ_app.manager_RTRQ.makefile                 as makefile
import RTRQ_app.manager_RTRQ.list_element_request     as list_element_request
import RTRQ_app.manager_RTRQ.list_linkdata            as list_linkdata
import RTRQ_app.list_app                              as list_app 

from RTRQ_app.tool_RTRQ.tool_threading import *
from RTRQ_app.tool_RTRQ.tool_RTRQ_data import *



class Runtime_request():
    def __init__(self) -> None:
        #link du lieu
        self.link_data_request         =  list_linkdata.link_data_request
        self.link_data_element         =  list_linkdata.link_data_element
        self.link_data_element_request =  list_linkdata.link_data_element_request

        makefile.make(list_linkdata.link_data_element_request)
        #app func
        self.app = list_app




    def run(self):
        self.luong_main = luong_timer(0.01,self.run_command)
        self.luong_main.start()


    def run_command(self):
        #main xu li 
        self.command = request_data(self.link_data_request).get()

        #command request #1
        try:
            if(self.command == list_element_request.SelectFile_btn_selectfile) : 
                luong_basic(self.app.convertFile).run()
        except:
            None





    def exit(self):
        self.luong_main.end()



