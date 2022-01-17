#import GUI module Tkinter and its sub classes
from tkinter import *
from tkinter import messagebox
from db import Database
db=Database("stock.db")
def populate_list():
    part_list.delete(0,END)
    for row in db.fetch():
        part_list.insert(END,row)

def select_item(event):
    try:
        global selected_item
        index=part_list.curselection()[0]
        selected_item=part_list.get(index)

        Item_entry.delete(0,END)
        Item_entry.insert(END,selected_item[1])
        Customer_entry.delete(0,END)
        Customer_entry.insert(END,selected_item[2])
        Vendor_entry.delete(0,END)
        Vendor_entry.insert(END,selected_item[3])
        Price_entry.delete(0,END)
        Price_entry.insert(END,selected_item[4])
    except IndexError:
        pass
def add_item():
    if Item_text.get()==""or Customer_text.get()=="" or Vendor_text.get()=="" or Price_text.get()=="":
       messagebox.showerror("Warning","Required data must be insert") 
       return
    
    db.insert(Item_text.get(),Customer_text.get(),Vendor_text.get(),Price_text.get())
    part_list.delete(0,END)
    part_list.insert(END,(Item_text.get(),Customer_text.get(),Vendor_text.get(),Price_text.get()))
    populate_list()

def remove_item():
    db.remove(selected_item[0]) 
    clear_Text()
    populate_list()

def update_item():
    try:
        db.update(selected_item[0],Item_text.get(),Customer_text.get(),Vendor_text.get(),Price_text.get())
        populate_list()
    except IndexError:
        pass

def clear_Text():
    Item_entry.delete(0,END)
    Customer_entry.delete(0,END)
    Vendor_entry.delete(0,END)
    Price_entry.delete(0,END)
#create window object
stock=Tk()
stock.title("Inventory System")
stock.iconbitmap("")
#Item
Item_text=StringVar()
Item_label=Label(stock,text="Item Name",font=('bold',10),pady=1)
Item_label.grid(column=0,row=0,sticky=W)
Item_entry=Entry(stock,textvariable=Item_text,bg="darkgreen",fg="white",font="lucida 12")
Item_entry.grid(column=1,row=0)

#Customer
Customer_text=StringVar()
Customer_label=Label(stock,text="Customer Name",font=('bold',10),pady=1)
Customer_label.grid(column=0,row=1,sticky=W)
Customer_entry=Entry(stock,textvariable=Customer_text,bg="darkgreen",fg="white",font="lucida 12")
Customer_entry.grid(column=1,row=1)
#Vendor
Vendor_text=StringVar()
Vendor_label=Label(stock,text="Vendor Name",font=('bold',10),pady=1)
Vendor_label.grid(column=0,row=2,sticky=W)
Vendor_entry=Entry(stock,textvariable=Vendor_text,bg="darkgreen",fg="white",font="lucida 12")
Vendor_entry.grid(column=1,row=2)
#Price
Price_text=StringVar()
Price_label=Label(stock,text="Price ",font=('bold',10),pady=3)
Price_label.grid(column=0,row=3,sticky=W)
Price_entry=Entry(stock,textvariable=Price_text,bg="darkgreen",fg="white",font="lucida 12")
Price_entry.grid(column=1,row=3)
#part List
part_list=Listbox(stock,height=8,width=60,font="lucida 10",bg="darkgreen" ,fg="white",border=10)
part_list.grid(column=0,row=4,columnspan=3)
#create Schroll bar
list_scroll=Scrollbar(stock,bg="grey",)
# list_scroll=Scrollbar(stock)
list_scroll.grid(row=4,column=3)
# list_scroll.pack(side=RIGHT,fill=Y)
#set scroll bar to listbox

part_list.config(yscrollcommand=list_scroll.set)
list_scroll.config(command=part_list.yview)
#bind list box select
part_list.bind('<<ListboxSelect>>',select_item)
#buttons
add_btn=Button(stock,text="Add Item",width=12,command=add_item,bg='blue',fg='white')
add_btn.grid(column=2,row=0)
Update_btn=Button(stock,text="Update Item",width=12,command=update_item,bg='blue',fg='white')
Update_btn.grid(column=2,row=1)
remove_btn=Button(stock,text="remove Item",width=12,command=remove_item,bg='blue',fg='white')
remove_btn.grid(column=2,row=2)
Clear_btn=Button(stock,text="Clear Item",width=12,command=clear_Text,bg='blue',fg='white')
Clear_btn.grid(column=2,row=3)

stock.geometry("480x280")

#populate list
populate_list()

#start Program
stock.mainloop()
