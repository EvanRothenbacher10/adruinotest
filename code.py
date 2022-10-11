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


from adafruit_circuitplayground import cp
import time
r = 0
g = 127
b = 254

def ChangeColor():
while True:
    while r < 255:
        r = r + 5
        time.sleep(0.1)
    if g == 255:
        while g != 0:
            g = g + 5
            time.sleep(0.1)
    while g < 255:
        g = g + 5
        time.sleep(0.1)
    while r != 0:
        r = r - 5
        time.sleep(0.1)
    while b < 255:
        b = b + 5
        time.sleep(0.1)
    while g < 255:
        g = g - 5
        time.sleep(0.1)    
