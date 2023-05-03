import time
from tk import getentry, buttons1, tkinterloop, update
import threading
import keyboard
import mouse

global_boolean = False  # will be changed to see if user input time is changed


def hotkey():
    while True:

        if keyboard.is_pressed(hot_key):
            if buttons1.ONOFF.get() == 1:
                buttons1.ONOFF.set(0)
                time.sleep(.5)
            else:
                buttons1.ONOFF.set(1)
                time.sleep(.5)
        else:
            time.sleep(.05)


def mainloop():
    global global_boolean
    while True:
        if buttons1.ONOFF.get() == 1:
            try:
                print(float(getentry()))
                if float(getentry()) > 5.0:
                    for i in range(int(getentry())):
                        print(i)
                        time.sleep(1)
                        if global_boolean:
                            global_boolean = False
                            break
                        else:
                            pass

                    mouse.click(button="left")
                    time.sleep(0.05)
                else:
                    time.sleep(float(getentry()))
                    mouse.click(button="left")
            except:
                update()
                time.sleep(.5)
                continue
        else:
            update()
            time.sleep(.5)


def time_change_checker():
    global global_boolean
    while True:
        current_sleep_time = getentry()
        time.sleep(3)
        if current_sleep_time != getentry():
            global_boolean = True


if __name__ == '__main__':
    file = open("config.txt")
    hot_key = file.read()
    file.close()

    thread1 = threading.Thread(target=mainloop)
    thread2 = threading.Thread(target=hotkey)
    thread3 = threading.Thread(target=time_change_checker)

    thread1.start()
    thread2.start()
    thread3.start()

    tkinterloop()
    # image sorter/ video sorter sorts by date or smth
