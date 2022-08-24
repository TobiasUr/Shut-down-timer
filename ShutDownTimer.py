import os
from tkinter import *
root = Tk()
Label(root, text="Enter time to shut down in minutes: ").grid(row=0, column=0)
e=Entry(root, width=10, borderwidth=5)
e.grid(row=0, column=1)
time=e.get()
def OK():
    time=int(e.get())
    time=time * 60
    stringOne="shutdown /s /t "
    StringTwo = str(time)
    StringFinal = stringOne + StringTwo
    print(StringFinal)
    os.system(StringFinal)

def cancel():
    os.system('shutdown -a')

Button(root, text="OK", command=OK).grid(row=0, column=2)
Button(root, text="Cancel", command=cancel).grid(row=0, column=3)

root.mainloop()