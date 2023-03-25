#An program to create a button Tanvi using tkinter

from tkinter import*
def msg():
    print("Tanvi")
win=Tk()
win.title("TANVI")
#win.geometry("500*300")
btn=Button(win,text="Welcome",command=msg)
btn.pack()
win.mainloop()
