from tkinter import *

root = Tk()
root.title("Maddox's Auto Clicker")
root.geometry("290x290")
root.attributes('-alpha', 0.8)
root.resizable(False, False)


def getentry():
    string = buttons1.entry.get()
    return string


class buttons1:
    ONOFF = IntVar()
    switch = Checkbutton(root, text='Enable AutoClicker (time in s)', variable=ONOFF, onvalue=1, offvalue=0)
    switch.select()
    ONOFF.set(0)

    entry = Entry(root, width=30, bg="lightgray")



def placeb():
    buttons1.switch.place(x=15, y=10)
    buttons1.entry.place(x=15, y=30)


def update():
    root.update()


def tkinterloop():
    placeb()
    root.mainloop()
