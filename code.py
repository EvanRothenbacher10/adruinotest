from adafruit_circuitplayground import cp
import time
import copy
import threading
r = 0
g = 127
b = 254

def changeColor():
    global r, g, b
    while True:
        r = r + 1
        time.sleep(0.5)
        g = g + 1
        time.sleep(0.5)
        b = b + 1
        if r == 255:
            r = 0
        elif g == 255:
            g = 0
        elif b == 255:
            b = 255
        time.sleep(0.5)

def setColor():
    cp.pixels[0] = (r, g, b)
    cp.pixels[1] = (copy.copy(r), copy.copy(g), copy.copy(b))

changeThread = threading.thread(target= changeColor)
setThread = threading.thread(target= setColor)

changeThread.start()
setThread.start()

while True:
    print(r)
    time.sleep(0.5)
    print(g)
    print(b)
