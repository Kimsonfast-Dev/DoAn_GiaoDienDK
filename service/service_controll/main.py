import sys
sys.path.append("./")

from service.service_controll.api.service_controll import sv_controll
main = sv_controll()

def leveling_map(): 
    main.leveling_map()

def leveling():
    main.leveling()

def runfile():
    main.running()
    
def test_dao(value):
    main.test_thaydao(value)
    
def run_cm(data):
    main.run_cm(data)

def sethome():
    main.sethome()