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
text_0="Welcome to the Vending Machine!"

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
    main.title(text_0)

def label():
    frame_0=tkinter.Frame()
    frame_0.pack(side=tkinter.TOP)
    label_0=tkinter.Label(frame_0, text=text_0, font=("Segoe UI",20))
    label_0.pack(side=tkinter.LEFT)

def body():
    frame_1=tkinter.Frame()
    frame_1.pack(side=tkinter.TOP)
    text_1="Welcome customer! We here are selling following items:"
    label_1=tkinter.Label(frame_1, text=text_1, font=("Segoe UI",12))
    label_1.grid(row=0, column=0)

def items_chart():
    global ITEM_NAMES
    global ITEM_PRICES
    global frame_2
    frame_2=tkinter.Frame()
    frame_2.pack(side=tkinter.TOP, pady=10)
    item_s_no=tkinter.Label(frame_2, text="S. No.", font=("Segoe UI",11))
    item_s_no.grid(row=0, column=0, padx=20)
    item_label0=tkinter.Label(frame_2, text="Item Name", font=("Segoe UI",11))
    item_label0.grid(row=0, column=1, padx=20)
    item_price=tkinter.Label(frame_2, text="Item Price", font=("Segoe UI",11))
    item_price.grid(row=0, column=2, padx=20)
    item_amt=tkinter.Label(frame_2, text="Enter Amount:", font=("Segoe UI",11))
    item_amt.grid(row=0, column=3, padx=20)
    for index in range(len(ITEM_NAMES)):
        s_no=tkinter.Label(frame_2, text=str(index), font=("Segoe UI",10))
        s_no.grid(row=index+1, column=0, padx=20)
    for index in range(len(ITEM_NAMES)):
        item_label=tkinter.Label(frame_2, text=ITEM_NAMES[index], font=("Segoe UI",10))
        item_label.grid(row=index+1, column=1, padx=20)
    for index in range(len(ITEM_PRICES)):
        item_label=tkinter.Label(frame_2, text=ITEM_PRICES[index], font=("Segoe UI",10))
        item_label.grid(row=index+1, column=2, padx=20)

def set_entries():
    length=len(ITEM_NAMES)
    for index in range(length):
        exec(("global entry_%d" %(index)))
        execute_0=("entry_%d=tkinter.Entry(frame_2, width=4)" %(index))
        execute_1=("entry_%d.grid(row=%d+1, column=3, padx=20)" %(index,index))
        print("Executed:", execute_0)
        exec(execute_0,globals())
        exec(execute_1,globals())

def bills():
    global frame_3
    global string_0
    global string_1
    frame_3=tkinter.Frame()
    frame_3.pack(side=tkinter.TOP, pady=10)
    final_bill=tkinter.Label(frame_3, text="After entering the required amount of items, click on below button to generate bill.")
    final_bill.pack(side=tkinter.TOP)
    string_0=tkinter.StringVar()
    string_1=tkinter.StringVar()

    def generate():
        
        global recipt
        global frame_3
        global TOTAL_AMOUNT
        global string_0
        global string_1
        global current_quantity

        TOTAL_AMOUNT=0
        recipt=open("receipt.txt","w")
        recipt.write("Thanks for shopping at us! You purchased following items:\n")

        for i in range(len(ITEM_NAMES)):
            exec("item_quantity_%d=entry_%d.get()" %(i,i), globals())
            exec("TOTAL_AMOUNT+=(int(ITEM_PRICES[%d])*int(item_quantity_%d))" %(i,i), globals())
            exec("current_quantity=(entry_%d.get())" %(i), globals())
            exec("recipt.write('PURCHASED ITEM=%s,ITEM PRICE=%d, ITEM QUANTITY=%d')" %(ITEM_NAMES[i],int(ITEM_PRICES[i]),int(current_quantity)), globals())
            recipt.write("\n")
        print("Total Amount is: %d" %TOTAL_AMOUNT)
        recipt.write("\n Total cash to be paid : %d" %TOTAL_AMOUNT)
        recipt.close()
        string_0.set("Your total bill amount is Rs.%d" %TOTAL_AMOUNT)
        string_1.set("Thankyou for shopping! Your bill is saved as receipt.txt.")
    
    final_button=tkinter.Button(frame_3, text="Generate Bill/Recipt for payment.", command=generate)
    final_button.pack(side=tkinter.TOP, ipadx=10, pady=10)
    final_message=tkinter.Label(frame_3, textvariable=string_0, font=("Segoe UI", 12))
    final_message.pack(side=tkinter.TOP, pady=20)
    tkinter.Label(frame_3, textvariable=string_1, font=("Segoe UI", 12)).pack(side=tkinter.TOP, pady=10)

main_window()
label()
body()
items_chart()
set_entries()
bills()

main.mainloop()

