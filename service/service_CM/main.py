import sys
sys.path.append("./")
from service.service_CM.api.service_CM import sv_CM

main = sv_CM()
main.start()

def sendcnc(linkfile):
    main.sendCNC(linkfile)

def getcnc():
    return main.dataupdate