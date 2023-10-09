import sys
sys.path.append("./")

from service.service_serial.api.service_serial import sv_serial
main = sv_serial()

def setup(portname,baudrate):
    main.init(portname,baudrate)

def connect():
    main.connect()

def disconnect():
    main.disconnect()

def send(data):
    main.write(data+"\n")

def get():
    data = main.read()
    return data

