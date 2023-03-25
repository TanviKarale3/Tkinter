from tkinter import*
class Mywin(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.a=StringVar()
        self.b=StringVar()
        self.t1=Entry(self,textVariable=self.a)
        self.t1.pack()
        self.btn=Button(self,text="Exchange",command=self.exg)
        self.btn.pack()
        self.t2=Entry(self,textVariable=self.b)
        self.t2.pack()
    def exg(self):
        s1=self.a.get()
        s2=self.b.get()
        self.a.set(s2)
        self.b.set(s1)
win=Mywin()
win.mainloop()