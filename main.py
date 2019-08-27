from tkinter import *

from time import sleep
from serial import Serial

ser = Serial("COM4")


def run():
    ser.write(str(w1.get()).encode() + b"\n")
    ser.write(str(w2.get()).encode() + b"\n")
    master.after(100, run)


master = Tk()
w1 = Scale(master, from_=100, to=-100)
w1.set(0)
w1.pack()
w2 = Scale(master, from_=-100, to=100,  orient=HORIZONTAL)
w2.set(0)
w2.pack()

master.after(100, run)

mainloop()
