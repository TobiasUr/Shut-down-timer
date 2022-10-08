from cgitb import text
import os
from socket import socket
from tkinter import *
import time as tm
import datetime
import threading
import math

root = Tk()

Label(root, text="Enter time to shut down in minutes: ").grid(row=0, column=0)
Label(root, text="Time left until shutdown: ").grid(row=1, column=0)

global v
v = StringVar()
Label(root, textvariable=v).grid(row=1, column=1)

e=Entry(root, width=10, borderwidth=5)
e.grid(row=0, column=1)

global time 
time = 0

global secondsleft

def countdown():
    global time
    global secondsleft
    secondsleft = time
    seconds = time
    while seconds > 0:
        root.update
        timer = datetime.timedelta(seconds= seconds)
        tm.sleep(1)
        seconds -= 1
        secondsleft -= 1
        global v
        if secondsleft < 1:
            v.set("")
            break
        
        hours = math.floor(seconds/3600)
        minutes = math.floor(seconds/60-hours*60)
        Seconds = math.floor(seconds-hours*3600-minutes*60)
        timeStr = "{}H {}M {}S".format(hours, minutes, Seconds)
        v.set(str(timeStr))
        
        


        

def OK():
    cancel()
    tm.sleep(1)
    global time
    time=int(e.get())
    time=time * 60
    stringOne="shutdown /s /t "
    StringTwo = str(time)
    StringFinal = stringOne + StringTwo
    print(StringFinal)
    os.system(StringFinal)
    threading.Thread(target=countdown).start()

def cancel():
    os.system('shutdown -a')
    global secondsleft
    secondsleft=0

Button(root, text="OK", command=OK).grid(row=0, column=2)
Button(root, text="Cancel", command=cancel).grid(row=0, column=3)

root.mainloop()
