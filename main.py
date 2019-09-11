from tkinter import *
from serial import Serial
from grip import GripPipeline
import numpy as np
import cv2

# INITIALIZATION
cap = cv2.VideoCapture(0)
grip = GripPipeline()


def maps(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


# VISION LOOP
while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here

    # Grip Pipeline
    points = []
    points = grip.process(frame)
    if (points):
        if (points[0][0] > 300):
            print(maps(points[0][0], 0, 300, 90, 180))
            print("Left")
        else:
            print(maps(points[0][0] - 300, 0, 300, 0, 90))
            print("Right")

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Press q to break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
ser = Serial("COM4")


def run():
    ser.write(str(w1.get()).encode() + b"\n")
    ser.write(str(w2.get()).encode() + b"\n")
    master.after(100, run)


# Joystick Code
master = Tk()
w1 = Scale(master, from_=100, to=-100)
w1.set(0)
w1.pack()
w2 = Scale(master, from_=-100, to=100, orient=HORIZONTAL)
w2.set(0)
w2.pack()

master.after(100, run)

mainloop()
