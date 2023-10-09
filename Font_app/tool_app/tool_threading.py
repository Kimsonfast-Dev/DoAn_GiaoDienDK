import time
import threading


class luong_timer():
    def __init__(self,time,func = None) -> None:
        self.time = time
        self.func = func
        self.info = 0

    def main(self):
        if(self.func != None):
            while 1: 
                self.func()
                time.sleep(self.time)
                if(self.info == 0): break
                
    def start(self):
        self.luong = threading.Thread(target=self.main)
        self.info = 1
        self.luong.start()

    def end(self):
        self.info = 0
        #self.luong.join()

class luong_basic():
    def __init__(self,func = None) -> None:
        self.func = func

    def main(self):
        if(self.func != None):
            self.func()
                
    def run(self):
        self.luong = threading.Thread(target=self.main)
        self.luong.start()

    def end(self):
        self.luong.join()
