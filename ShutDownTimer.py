from cgitb import text
import os
from socket import socket
from tkinter import *
import time as tm
import datetime
import threading
import math
from pynput.keyboard import Key, Listener
import threading
import sys

root = Tk()

#text fields
Label(root, text="Enter time to shut down in minutes: ").grid(row=0, column=0)

global v
v = StringVar()
Label(root, textvariable=v).grid(row=1, column=1)

#timeentry
ehours=Entry(root, width=2, borderwidth=1)
ehours.grid(row=0, column=1)
Label(root, text="H").grid(row=0, column=2)
eminutes=Entry(root, width=2, borderwidth=1)
eminutes.grid(row=0, column=3)
Label(root, text="M").grid(row=0, column=4)
eseconds=Entry(root, width=2, borderwidth=1)
eseconds.grid(row=0, column=5)
Label(root, text="S").grid(row=0, column=6)

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
        eseconds.delete(0, END)
        eminutes.delete(0, END)
        ehours.delete(0, END)
        eseconds.insert(0, str(Seconds))
        eminutes.insert(0, str(minutes))
        ehours.insert(0, str(hours))
        
        
        


        

def OK():
    cancel()
    tm.sleep(1)
    global time
    seconds=int(eseconds.get())
    minutes=int(eminutes.get())
    hours=int(ehours.get())
    time=(hours * 3600)+(minutes*60)+seconds
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





Button(root, text="OK", command=OK).grid(row=0, column=7)
Button(root, text="Cancel", command=cancel).grid(row=0, column=8)

def keylisten():
    def on_release(key):
        print('{0} release'.format(
            key))
        if key == Key.enter:
            # Stop listener
            OK()

    # Collect events until released
    with Listener(
            on_release=on_release) as listener:
        listener.join()
        
t1 = threading.Thread(target=keylisten)
t1.start()

def killself():
    root.destroy()
    sys.exit()
    


root.protocol("WM_DELETE_WINDOW",  killself)

root.mainloop()


