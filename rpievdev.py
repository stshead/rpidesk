import evdev
import threading
import time

class TDEV():
    def __init__(self):
        self.slot=0
        self.max_n=10
        self.activearray = [0 for i in range(self.max_n)]
        self.posx = [0 for i in range(self.max_n)]
        self.posy = [0 for i in range(self.max_n)]
        self.abort=False
        self.thread = threading.Thread(target=self.tsthread)
        self.thread.start()

    def tsthread(self):
        dev = evdev.InputDevice("/dev/input/event0")
        print("[Touch thread] start")
        for event in dev.read_loop():
            #print(event)
            if(event.code==47):
                self.slot=event.value
            elif(event.code==57):
                if(event.value>0):
                    self.activearray[self.slot]=1
                else:
                    self.activearray[self.slot]=0
            elif(event.code==53):
                self.posx[self.slot]=(800-event.value)
            elif(event.code==54):
                self.posy[self.slot]=(480-event.value)

            if(self.abort):
                dev.close()
                break
        print("[Touch thread] end")

