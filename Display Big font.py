from tkinter import*
class Mywin(Tk):
    def __init__(self):
        super().__init__()
        data="Intelligence= TANVI"
        fnt="TimesRoman 40 bold"
        self.Lbl=Label(self,text=data,font=fnt)
        self.Lbl.pack()
win=Mywin()
win.configure(background="Red",cursor="cross")
win.geometry("500x300")
win.mainloop()