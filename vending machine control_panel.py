import tkinter
file1=open("items.txt","r")

def search_items():
    global file1
    script=file1.read()
    exec(script,globals())

def arrange_items():
    global file1
    global items
    global ITEM_NAMES
    global ITEM_PRICES
    ITEM_NAMES=[]
    ITEM_PRICES=[]
    length=len(items)
    for item in range(length):
        current_item=items[item]
        ITEM_NAMES.append(current_item[0])
        ITEM_PRICES.append(current_item[1])

search_items()
arrange_items()

print("Found items are: \n", ITEM_NAMES)
print("Found prices are: \n", ITEM_PRICES)

def main_window():
    global main
    main=tkinter.Tk()
    height=main.winfo_screenheight()
    width=main.winfo_screenwidth()
    x=int((width-640)/2)
    y=int((height-480)/2)
    main.geometry("640x480+%d+%d" %(x,y))
    main.maxsize(640,480)
    main.resizable(0,0)
    main.focus_force()
    main.title("Vending Machine: Control Panel")

def labels():
    text_0="Welcome to Vending Machine Control Panel..."
    text_1="Following items are currently present at your Vending Machine:"
    frame_0=tkinter.Frame()
    frame_0.pack(side=tkinter.TOP)
    label_0=tkinter.Label(frame_0, text=text_0, font=("Segoe UI",18))
    label_0.pack(side=tkinter.TOP)
    frame_1=tkinter.Frame()
    frame_1.pack(side=tkinter.TOP)
    label_1=tkinter.Label(frame_0, text=text_1, font=("Segoe UI",12))
    label_1.pack(side=tkinter.TOP)

def main_frame():
    global frame_2
    frame_2=tkinter.Frame()
    frame_2.pack(side=tkinter.TOP)

def current_items():
    global frame_2
    global items
    total_items=len(ITEM_NAMES)
    font_0=("Segoe UI",10)
    font_1=("Segoe UI",11)
    tkinter.Label(frame_2, text="S.No.", font=font_1).grid(row=0, column=0, padx=20)
    tkinter.Label(frame_2, text="Item Name", font=font_1).grid(row=0, column=1, padx=20)
    tkinter.Label(frame_2, text="Item Price", font=font_1).grid(row=0, column=2, padx=20)
    for index in range(total_items):
        tkinter.Label(frame_2, text=str(index+1), font=font_0).grid(row=index+1, column=0, padx=20)
        tkinter.Label(frame_2, text=ITEM_NAMES[index], font=font_0).grid(row=index+1, column=1, padx=20)
        tkinter.Label(frame_2, text=ITEM_PRICES[index], font=font_0).grid(row=index+1, column=2, padx=20)

def modify():
    font_0=("Segoe UI",12)
    frame_3=tkinter.Frame()
    frame_3.pack(side=tkinter.TOP)
    tkinter.Label(frame_3, text="For modifying the selling items:", font=font_0).pack(side=tkinter.TOP, pady=30)

def new_input():
    global new_items_entry
    global new_prices_entry
    font_0=("Segoe UI",10)
    font_1=("Segoe UI",10)
    frame_4=tkinter.Frame()
    frame_4.pack()
    label_1=tkinter.Label(frame_4, text="Enter the names of items to add:", font=font_1)
    label_1.grid(row=0, column=0)
    label_2=tkinter.Label(frame_4, text="Enter the prices  of items to add:", font=font_1)
    label_2.grid(row=1, column=0)
    new_items_entry=tkinter.Entry(frame_4, width=60, font=font_0)
    new_prices_entry=tkinter.Entry(frame_4, width=60, font=font_0)
    new_items_entry.grid(row=0,column=1)
    new_prices_entry.grid(row=1, column=1)

def edit_items_file():
    global frame_2
    global items
    for element in frame_2.winfo_children():
        element.destroy()
    file_1=open("items.txt","w")
    file_1.write("items=%s" %str(items))
    file_1.flush()
    file_1.close()
    search_items()
    arrange_items()
    current_items()
    tkinter.Label(text="Success! Stocks are modified", font=("Segoe UI",11)).pack(side=tkinter.TOP,pady=5)

def finalize():
    global NEW_ITEM_NAMES
    global NEW_ITEM_PRICES
    global items
    items=[]
    total_items=len(NEW_ITEM_NAMES)
    for i in range(total_items):
        name=NEW_ITEM_NAMES[i]
        price=NEW_ITEM_PRICES[i]
        items.append([name,price])
    print("Final items list:\n", items)
    edit_items_file()

def sort_input():
    global NEW_ITEM_NAMES
    global NEW_ITEM_PRICES
    new_items_string=new_items_entry.get()
    new_prices_string=new_prices_entry.get()
    NEW_ITEM_NAMES=eval(new_items_string)
    NEW_ITEM_PRICES=eval(new_prices_string)
    if len(NEW_ITEM_NAMES)!=len(NEW_ITEM_PRICES):
        print("ERROR! Enter the prices for all the items.")
    else:
        finalize()

def finalize_button():
    font_0=("Segoe UI",10)
    frame_5=tkinter.Frame()
    frame_5.pack()
    button_0=tkinter.Button(frame_5, text="Finalize! (Press button twice)", command=sort_input)
    button_0.pack(side=tkinter.TOP, pady=20)

main_window()
labels()
main_frame()
current_items()
modify()
new_input()
finalize_button()

main.mainloop()

