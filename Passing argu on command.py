#Passing argument on command
from tkinter import*
from functools import partial
def show(data):
    print(data)
win=Tk()
btn=Button(win,text="OK",command=partial(show,"Hello"))
win.mainloop()