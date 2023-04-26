import win32api
import win32con
import time
from tk import getentry, buttons1, tkinterloop, update
import threading
import keyboard


def OperatingSystem():
    # get what os u are on (unfinished
    return "what os im on"  # MacOS or Windows


def gethotkey():
    # get ur hotkey
    return "7+8+9"


class windowslp:
    def __init__(self, hotkey):

        self.hotkey = hotkey

    def mainloop(self):
        while True:
            if buttons1.ONOFF.get() == 1:
                try:
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                    time.sleep(float(getentry()))
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                    print(float(getentry()))
                    time.sleep(.01)
                    update()
                except:
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

    # is on windows? then do this.
    if OperatingSystem() == "Windows":
        new = windowslp(gethotkey())
        thread1 = threading.Thread(target=new.mainloop)
        thread2 = threading.Thread(target=new.hotkey)
        thread1.start()
        thread2.start()
        tkinterloop()
    elif OperatingSystem() == "MacOS":
        # macos is unfinished
        new = maclp(gethotkey())

        thread1 = threading.Thread(target=new.macloop)
        thread2 = threading.Thread(target=new.hotkey)
        thread1.start()
        thread2.start()
        tkinterloop()
    else:
        print("err")
