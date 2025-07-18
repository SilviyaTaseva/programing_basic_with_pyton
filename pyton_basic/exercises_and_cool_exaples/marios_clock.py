from cProfile import label
from time import strftime
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Mario's Clock")


def clock():
    tick = strftime("%H:%M:%S %p")
    label.config(text=tick)
    label.after(1000, clock)

label = Label(root, front=("sans", 100),background="black",foreground="red" )
label.pack(anchor="center")
clock()
mainloop()