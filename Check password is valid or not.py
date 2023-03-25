from tkinter import*
def checkpwd():
    data=t1.get()
    if data=="admin":
        print("Valid user")
    else:
        print("Invalid user")
win=Tk()
win.geometry("300x200")
t1=Entry(win,show="*",justify=CENTER)
t1.pack()
b1=Button(win,text="check",command=checkpwd)
b1.pack()
win.mainloop()