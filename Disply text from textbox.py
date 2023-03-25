from tkinter import*
def showdata():
    data=t1.get()
    print(data)
win=Tk()
win.geometry("500x300")
t1=Entry(win)
t1.pack()
b1=Button(win,text="show",command=showdata)
b1.pack()
win.mainloop()