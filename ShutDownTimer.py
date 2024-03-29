from cgitb import text
import os
from socket import socket
from tkinter import *
import time as tm
import datetime
import threading
import math
from pynput.keyboard import Key, Listener
import sys

#Create root
root = Tk(screenName="ShutDownTimer")
#Set size
root.geometry("393x52")
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
eseconds.bind("<Return>", (lambda event: OK())) #listen for enter
Label(root, text="S").grid(row=0, column=6)

global time 
time = 0

global secondsleft
#Countdown
def countdown(ShutdownType):
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
        if seconds == 1:
             print(ShutdownType)
             if ShutdownType == "Sleep":
                StringFinal = "timeout /t 0&&rundll32.exe powrprof.dll,SetSuspendState Sleep"
                print(StringFinal)   
                os.system(StringFinal)
        
        
#DropdownMenu 
options_list = ["Shut Down","Restart", "Sleep"]
Selected = StringVar(root)
Selected.set("Shut Down")

drop = OptionMenu(root, Selected, *options_list)     
drop.grid(row=0, column=7)


    

def OK(ShutdownType):
    cancel()
    tm.sleep(1)
    global time
    seconds=int(eseconds.get())
    minutes=int(eminutes.get())
    hours=int(ehours.get())
    time=(hours * 3600)+(minutes*60)+seconds
    print(ShutdownType)
    stringOne ="shutdown /s /t " if ShutdownType == "Shut Down" else ("shutdown /r /t " if ShutdownType == "Restart" else ("psshutdown -d -t " if ShutdownType == "Sleep" else "shutdown /s /t "))
    if ShutdownType == "Sleep":       
        threading.Thread(target= lambda: countdown(ShutdownType)).start()
        

    else:
        StringTwo = str(time)
        StringFinal = stringOne + StringTwo
        print(StringFinal)
        os.system(StringFinal)
        threading.Thread(target= lambda: countdown(ShutdownType)).start()

def cancel():
    os.system('shutdown -a')
    global secondsleft
    secondsleft=0



container = Frame(root)
container.place(relx=0.5, rely=0.75, anchor=CENTER)
Button(container, text="OK", command= lambda: OK(ShutdownType=Selected.get())).grid(row=0, column=0)
Button(container, text="Cancel", command=cancel).grid(row=0, column=1)



def killself():
    root.destroy()
    sys.exit()
    


root.protocol("WM_DELETE_WINDOW",  killself)

root.mainloop()


