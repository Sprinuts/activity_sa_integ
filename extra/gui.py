from tkinter import *

#######
def btnClick(event):
    print("Whats up", txtMsg.get())
    myLblMsg.set(txtMsg.get())
    
def btnClear(event):
    #print("Whats up nigg", txtMsg.get())
    myLblMsg.set("")
    #txtMsg.set("")
    txtMsg.delete(0, "end")

wn = Tk()
wn.title("Hello World")
wn.geometry("500x400+300+300")

#######
myLblMsg = StringVar()


lblHead = Label(wn, text="Hello World", fg="red", font=("Arial", 20))
lblHead.place(x=170, y=20)
txtMsg = Entry(wn,text="Enter String Here")
txtMsg.place(x=10, y=50)


btn = Button(wn, text="Click ME")
btn.place(x=10,y=80)
btn.bind("<Button-1>", btnClick)

btnClr = Button(wn, text="Clear")
btnClr.place(x=100,y=80)
btnClr.bind("<Button-1>", btnClear)

lblMsg = Label(wn,textvariable=myLblMsg ,text="" ,fg="red", font=("Arial", 20))
lblMsg.place(x=170, y=110)

wn.mainloop()