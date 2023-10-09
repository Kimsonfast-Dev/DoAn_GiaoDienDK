import sys
from Font_app.root import tkinterApp
from RTRQ_app.RTRQ import *

#Interface setup
app = tkinterApp()
#Interface main
RT = Runtime_request()
RT.run()
#Interface request
app.run()
#Intrerface close()
RT.exit()
sys.exit()

