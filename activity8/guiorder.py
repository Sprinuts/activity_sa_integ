from tkinter import *
from tkinter.ttk import Combobox

def doOrder(event):
    item = varItem.get()
    size = ""
    if optVar.get() == 1:
        size = "Small"
    elif optVar.get() == 2:
        size = "Medium"
    elif optVar.get() == 3:
        size = "Large"
    else:
        size = ""
    
    addons = []
    if cb1Var.get() == 1:
        addons.append("Ketchup")
    if cb2Var.get() == 1:
        addons.append("Mayonnaise")
    if cb3Var.get() == 1:
        addons.append("Mustard")
    if cb4Var.get() == 1:
        addons.append("Tomato")
    if cb5Var.get() == 1:
        addons.append("Lettuce")
    
    price = calculatePrice(item, size, addons)
    printOrderSummary(item, size, addons, price)
    updateOrderSummary(item, size, addons, price)

def calculatePrice(item, size, addons):
    item_prices = {
        "Beef Burger": 65,
        "Chicken Burger": 50,
        "Fries": 25
    }
    size_prices = {
        "Small": 0,
        "Medium": 10,
        "Large": 20
    }
    addon_prices = {
        "Ketchup": 3,
        "Mayonnaise": 3,
        "Mustard": 3,
        "Tomato": 10,
        "Lettuce": 10
    }
    
    total_price = item_prices[item] + size_prices[size]
    for addon in addons:
        total_price += addon_prices[addon]
    
    return total_price

def printOrderSummary(item, size, addons, price):
    print("Order Summary:")
    print("Item:", item)
    print("Size:", size)
    print("Add-ons:", ", ".join(addons))
    print("Price: Php", price)

def updateOrderSummary(item, size, addons, price):
    summary = "Your Order:\n"
    summary += "Item: " + item + "\n"
    summary += "Size: " + size + "\n"
    summary += "Add-ons: " + ", ".join(addons) + "\n"
    summary += "Price: Php " + str(price)
    lblSummary.config(text=summary, anchor="w")

wn = Tk()
wn.title("Budget Meal")
wn.geometry("900x400+400+250")
lblHeader = Label(wn, text="SELECT YOUR ORDER", fg="black", font=("Arial", 20))
lblHeader.place(x=170, y=20)
myFont = ("Arial", 18)
varItem = StringVar()
item = ("Beef Burger", "Chicken Burger", "Fries")
cmbItem = Combobox(wn, textvariable=varItem, values=item, font="Arial 16", width=30)
cmbItem.place(x=50, y=60)
varItem.set("Beef Burger")
optVar = IntVar()
rb1 = Radiobutton(wn, text="Small", variable=optVar, value=1)
rb2 = Radiobutton(wn, text="Medium", variable=optVar, value=2)
rb3 = Radiobutton(wn, text="Large", variable=optVar, value=3)
rb1.place(x=50, y=90)
rb2.place(x=150, y=90)
rb3.place(x=250, y=90)
optVar.set(1)
cb1Var = IntVar()
cb2Var = IntVar()
cb3Var = IntVar()
cb4Var = IntVar()
cb5Var = IntVar()
cb1 = Checkbutton(wn, text="Ketchup", variable=cb1Var, onvalue=1, offvalue=0)
cb2 = Checkbutton(wn, text="Mayonnaise", variable=cb2Var, onvalue=1, offvalue=0)
cb3 = Checkbutton(wn, text="Mustard", variable=cb3Var, onvalue=1, offvalue=0)
cb4 = Checkbutton(wn, text="Tomato", variable=cb4Var, onvalue=1, offvalue=0)
cb5 = Checkbutton(wn, text="Lettuce", variable=cb5Var, onvalue=1, offvalue=0)
cb1.place(x=50, y=120)
cb2.place(x=150, y=120)
cb3.place(x=250, y=120)
cb4.place(x=350, y=120)
cb5.place(x=450, y=120)
btnSub = Button(wn, text="PLACE ORDER", bg="blue", fg="white")
btnSub.place(x=50, y=150)
btnSub.bind("<Button-1>", doOrder)
lblSummary = Label(wn, text="", font=("Arial", 14))
lblSummary.place(x=600, y=40)

priceList = Label(wn, text="Price List:", fg="black", font=("Arial", 16))
priceList.place(x=50, y=200)

item_prices = {
    "Beef Burger": 65,
    "Chicken Burger": 50,
    "Fries": 25
}
size_prices = {
    "Medium": 10,
    "Large": 20
}
addon_prices = {
    "Ketchup": 3,
    "Mayonnaise": 3,
    "Mustard": 3,
    "Tomato": 10,
    "Lettuce": 10
}

lblItemPrices = Label(wn, text="Menu Prices:", fg="black", font=("Arial", 14))
lblItemPrices.place(x=50, y=230)

lblSizePrices = Label(wn, text="Add Size:", fg="black", font=("Arial", 14))
lblSizePrices.place(x=250, y=230)

lblAddonPrices = Label(wn, text="Add-Ons:", fg="black", font=("Arial", 14))
lblAddonPrices.place(x=410, y=230)

row = 270
for item, price in item_prices.items():
    lblItem = Label(wn, text=item + ": Php " + str(price), font=("Arial", 12))
    lblItem.place(x=50, y=row)
    row += 20

row = 270
for size, price in size_prices.items():
    lblSize = Label(wn, text=size + ": Php " + str(price), font=("Arial", 12))
    lblSize.place(x=250, y=row)
    row += 20

row = 270
for addon, price in addon_prices.items():
    lblAddon = Label(wn, text=addon + ": Php " + str(price), font=("Arial", 12))
    lblAddon.place(x=410, y=row)
    row += 20
wn.mainloop()
