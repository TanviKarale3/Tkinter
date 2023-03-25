from tkinter import*
class Mywin(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.t1=Entry(self)
        self.t1.pack()
        self.btn=Button(self,text="Exchange",command=self.exg)
        self.btn.pack()
        self.t2=Entry(self)
        self.t2.pack()
    def exg(self):
        s1=self.t1.get()
        s2=self.t2.get()
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.t1.insert(0,s2)
        self.t2.insert(0,s1)
win=Mywin()
win.mainloop()