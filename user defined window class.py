from tkinter import*
class Mywin(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.txt=Entry(self,show="*",justify=CENTER)
        self.txt.pack()
        self.btn=Button(self,text="check",command=self.checkpwd)
        self.btn.pack()
    def checkpwd(self):
        pwd=self.txt.get()
        if pwd=="admin":
            print("Valid user")
        else:
            print("Invalid user")
        self.txt.delete(0,last=END)
win=Mywin()
win.mainloop()