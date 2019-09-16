from tkinter import Tk, Scale, mainloop


class Joystick:
    def __init__(self, ser):
        self.master = Tk()
        self.ser = ser

        master = Tk()
        w1 = Scale(master, from_=100, to=-100)
        w1.set(0)
        w1.pack()
        w2 = Scale(master, from_=-100, to=100, orient=HORIZONTAL)
        w2.set(0)
        w2.pack()

        master.after(100, run)

    def run(self):
        self.ser.write(str(w1.get()).encode() + b"\n")
        self.ser.write(str(w2.get()).encode() + b"\n")
        self.master.after(100, run)

    def block(self):
        self.master.mainloop()
