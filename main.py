from tkinter import *
from serial import Serial
from grip import GripPipeline
import numpy as np
import cv2

# INITIALIZATION
cap = cv2.VideoCapture(1)
grip = GripPipeline()

ser = Serial("COM4")


def maps(old_value, old_min, old_max, new_min, new_max):
    return ((old_value - old_min) / (old_max - old_min)) * (new_max - new_min) + new_min


def myround(x, base=5):
    return base * round(x/base)


# VISION LOOP
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # print(frame.shape) 480 x 640
    # Our operations on the frame come here

    # Grip Pipeline
    points = grip.process(frame)
    motorInput = 0
    if points:
        if points[0][0] > 320:
            temp = (maps(points[0][0] - 320, 0, 320, 0, 100))
            if temp > 10:
                motorInput = myround(temp) * 2
        else:
            temp = (maps(points[0][0], 0, 320, -100, 0))
            if temp < -10:
                motorInput = myround(temp) * 2
        print(motorInput)

        ser.write(str(70).encode() + b"\n")
        ser.write(str(motorInput).encode() + b"\n")
    else:
        ser.write(str(0).encode() + b"\n")
        ser.write(str(0).encode() + b"\n")

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Press q to break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
