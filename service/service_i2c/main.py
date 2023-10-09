import sys
sys.path.append("./")

from service.service_i2c.api.service_i2c import sv_i2c

main = sv_i2c(1)
def send(data):
    main.send_string(0x08,data)