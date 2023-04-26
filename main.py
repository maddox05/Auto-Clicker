import win32api
import win32con
import time
from tk import getentry, buttons1, tkinterloop, update
import threading
import keyboard
import mouse




def gethotkey():
    # get ur hotkey
    return "7+8+9"


class autoclick:
    def __init__(self, hotkey):

        self.hotkey = hotkey

    def mainloop(self):
        while True:
            if buttons1.ONOFF.get() == 1:
                print("on")
                try:
                    print(float(getentry()))
                    time.sleep(float(getentry()))

                    mouse.click(button="left")
                    time.sleep(0.05)
                    mouse.click(button="left")
                except:
                    print("except")
                    update()
                    time.sleep(.5)
                    continue
            else:
                update()
                time.sleep(.5)

    def hotkey(self, hotkey):  # ill add custom hotkeys later
        while True:
            if keyboard.is_pressed(hotkey):
                if buttons1.ONOFF.get() == 1:
                    buttons1.ONOFF.set(0)
                    time.sleep(.5)
                else:
                    buttons1.ONOFF.set(1)
                    time.sleep(.5)
            else:
                time.sleep(.05)


if __name__ == '__main__':
    new = autoclick(gethotkey())
    thread1 = threading.Thread(target=new.mainloop)
    thread2 = threading.Thread(target=gethotkey)
    thread1.start()
    thread2.start()
    tkinterloop()


