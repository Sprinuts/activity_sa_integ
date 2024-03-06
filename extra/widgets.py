from tkinter import *
from tkinter.ttk import Combobox


class Window():
    def __init__(self, win):
        self.lblHead = Label(wn, text="Hello World", fg="red", font=("Arial", 20))
        
        self.lblHead.place(x=150, y=20)
        
        self.item = StringVar()
        self.item.set("Select Item")
        self.data = ("hamburger" , "footlong" , "fries")
        self.cb = Combobox(win,textvariable=self.item ,values = self.data)
        self.cb.place(x=10, y=60)
        
        self.rbVar = IntVar()
        self.rbVar.set(0)
        
        self.r1 = Radiobutton(win, text="Small", variable=self.rbVar, value=1)
        self.r2 = Radiobutton(win, text="Medium", variable=self.rbVar, value=2)
        self.r3 = Radiobutton(win, text="Large", variable=self.rbVar, value=3)
        self.r1.place(x=10, y=100, anchor= W)
        self.r2.place(x=10, y=120, anchor= W)
        self.r3.place(x=10, y=140, anchor= W)
        
        self.cbkVar1 = IntVar()
        self.cbkVar2 = IntVar()
        self.cbkVar3 = IntVar()
        self.ck1 = Checkbutton(win , onvalue = 1, offvalue = 0, text="Ketchup", variable=self.cbkVar1)
        self.ck2 = Checkbutton(win , onvalue = 1, offvalue = 0, text="Mayonaise", variable=self.cbkVar2)
        self.ck3 = Checkbutton(win , onvalue = 1, offvalue = 0, text="Mustard", variable=self.cbkVar3)
        self.ck1.place(x=10, y=180)
        self.ck2.place(x=10, y=200)
        self.ck3.place(x=10, y=220)
        
        self.btnMsg = Button(wn, text="Order")
        self.btnMsg.place(x=10,y=80)
        self.btnMsg.bind("<Button-1>", self.btnOrder)
        self.btnMsg.place(x=10, y=250)
        
    def btnOrder(self, event):
        print("Order:", self.item.get())
        if self.rbVar.get() == 1:
            print("Size: Small")
        elif self.rbVar.get() == 2:
            print("Size: Medium")
        elif self.rbVar.get() == 3:
            print("Size: Large")
        else:
            print("Size: Not Selected")
        
        ###
        if self.cbkVar1.get() == 1:
            print("Ketchup")
            if self.cbkVar2.get() == 1:
                print("Mayonaise")
                if self.cbkVar3.get() == 1:
                    print("Mustard")
            elif self.cbkVar3.get() == 1:
                print("Mustard")
        ####3
        elif self.cbkVar2.get() == 1:
            print("Mayonaise")
            if self.cbkVar3.get() == 1:
                print("Mustard")
        ####
        elif self.cbkVar3.get() == 1:
            print("Mustard")
        else:
            print("No Condiments")



wn = Tk()
wn.title("Hello World")
wn.geometry("500x400+300+300")
myApp = Window(wn)
wn.mainloop()