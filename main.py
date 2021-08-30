from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox

root = Tk()
root.title('Vending Machines')

root.geometry("1100x500") # Set Size

# Create A Main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Create A Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

my_canvas_2 = Canvas(main_frame)
my_canvas_2.pack(side=RIGHT, fill=BOTH, expand=1)

# Add A Scrollbar To The Canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configure The Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))


# Create ANOTHER Frame INSIDE the Canvas
second_frame = Frame(my_canvas)

third_frame = Frame(my_canvas_2)
# Add that New frame To a Window In The Canvas
my_canvas.create_window((0,0), window=second_frame, anchor="nw")

my_canvas_2.create_window((0,1), window=third_frame, anchor="ne")
my_canvas.configure(bg='#FFE5B4')
second_frame.configure(bg='#FFE5B4')
third_frame.configure(bg='#FFE5B4')
my_canvas_2.configure(bg='#FFE5B4')
# i=0
# for thing in range(100):
# 	Button(second_frame, text=f'Button {thing} Yo!', command=lambda:show(i)).grid(row=thing, column=0, pady=10, padx=10)
# 	i+=1

# def show(number):
# 	return print (number)


# Frame 2
with sqlite3.connect("DBVending.db") as conn:
    c = conn.cursor()
    c.execute("SELECT * FROM Product ") 
    rows = c.fetchall()
    #print(rows)

pid = []
pdir = []
price = []
poutdir = []
quan = []
  
id = 0

my_img1 = ImageTk.PhotoImage(Image.open("images/dinosaur.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/lays.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/oreo.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images/birdy.png"))
my_img5 = ImageTk.PhotoImage(Image.open("images/fantagreen.png"))
my_img6 = ImageTk.PhotoImage(Image.open("images/fantared.png"))
my_img7 = ImageTk.PhotoImage(Image.open("images/fantaorange.png"))
my_img8 = ImageTk.PhotoImage(Image.open("images/coke.png"))
my_img9 = ImageTk.PhotoImage(Image.open("images/oishi.png"))
my_img10 = ImageTk.PhotoImage(Image.open("images/milk.png"))

my_label11 = Label(second_frame, image=my_img1).grid(row=0, column=0, pady=10, padx=10)
my_label12 = Label(second_frame, image=my_img2).grid(row=0, column=1, pady=10, padx=10)
my_label13 = Label(second_frame, image=my_img3).grid(row=2, column=0, pady=10, padx=10)
my_label14 = Label(second_frame, image=my_img4).grid(row=2, column=1, pady=10, padx=10)
my_label15 = Label(second_frame, image=my_img5).grid(row=4, column=0, pady=10, padx=10)
my_label16 = Label(second_frame, image=my_img6).grid(row=4, column=1, pady=10, padx=10)
my_label17 = Label(second_frame, image=my_img7).grid(row=6, column=0, pady=10, padx=10)
my_label18 = Label(second_frame, image=my_img8).grid(row=6, column=1, pady=10, padx=10)
my_label19 = Label(second_frame, image=my_img9).grid(row=8, column=0, pady=10, padx=10)
my_label20 = Label(second_frame, image=my_img10).grid(row=8, column=1, pady=10, padx=10)

for row in rows:
    pid.append(row[0])
    pdir.append(ImageTk.PhotoImage(Image.open('images/'+row[2])))
    price.append(row[3])
    quan.append(row[4])

def oop():
    if quan[0] >0: 
        Button(second_frame, text="Products stock " + str(quan[0]) + " item", state=DISABLED, bg='#C7EA46',font=("Arial", 15)).grid(row=1, column=0, pady=10, padx=5)
    else : Button(second_frame, text="Out of stock", state=DISABLED, bg='#FB607F',font=("Arial", 15)).grid(row=1, column=0, pady=10, padx=5)

    if quan[1] >0: 
        Button(second_frame, text="Products stock " + str(quan[1]) + " item", state=DISABLED, bg='#C7EA46',font=("Arial", 15)).grid(row=1, column=1, pady=10, padx=5)
    else : Button(second_frame, text="Out of stock", state=DISABLED, bg='#FB607F',font=("Arial", 15)).grid(row=1, column=1, pady=10, padx=5)

    if quan[2] >0:
        Button(second_frame, text="Products stock " + str(quan[2]) + " item", state=DISABLED, bg='#C7EA46',font=("Arial", 15)).grid(row=3, column=0, pady=10, padx=5)
    else : Button(second_frame, text="Out of stock", state=DISABLED, bg='#FB607F',font=("Arial", 15)).grid(row=3, column=0, pady=10, padx=5)

    if quan[3] >0:
        Button(second_frame, text="Products stock " + str(quan[3]) + " item", state=DISABLED, bg='#C7EA46',font=("Arial", 15)).grid(row=3, column=1, pady=10, padx=5)
    else : Button(second_frame, text="Out of stock", state=DISABLED, bg='#FB607F',font=("Arial", 15)).grid(row=3, column=0, pady=10, padx=5)

    if quan[4] >0:
        Button(second_frame, text="Products stock " + str(quan[4]) + " item", state=DISABLED, bg='#C7EA46',font=("Arial", 15)).grid(row=5, column=0, pady=10, padx=5)
    else : Button(second_frame, text="Out of stock", state=DISABLED, bg='#FB607F',font=("Arial", 15)).grid(row=5, column=0, pady=10, padx=5)

    if quan[5] >0:
        Button(second_frame, text="Products stock " + str(quan[5]) + " item", state=DISABLED, bg='#C7EA46',font=("Arial", 15)).grid(row=5, column=1, pady=10, padx=5)
    else : Button(second_frame, text="Out of stock", state=DISABLED, bg='#FB607F',font=("Arial", 15)).grid(row=5, column=1, pady=10, padx=5)

    if quan[6] >0:
        Button(second_frame, text="Products stock " + str(quan[6]) + " item", state=DISABLED, bg='#C7EA46',font=("Arial", 15)).grid(row=7, column=0, pady=10, padx=5)
    else : Button(second_frame, text="Out of stock", state=DISABLED, bg='#FB607F',font=("Arial", 15)).grid(row=7, column=0, pady=10, padx=5)

    if quan[7] >0:
        Button(second_frame, text="Products stock " + str(quan[7]) + " item", state=DISABLED, bg='#C7EA46',font=("Arial", 15)).grid(row=7, column=1, pady=10, padx=5)
    else : Button(second_frame, text="Out of stock", state=DISABLED, bg='#FB607F',font=("Arial", 15)).grid(row=7, column=1, pady=10, padx=5)
    if quan[8] >0:
        Button(second_frame, text="Products stock " + str(quan[8]) + " item", state=DISABLED, bg='#C7EA46',font=("Arial", 15)).grid(row=9, column=0, pady=10, padx=5)
    else : Button(second_frame, text="Out of stock", state=DISABLED, bg='#FB607F',font=("Arial", 15)).grid(row=9, column=0, pady=10, padx=5)

    if quan[9] >0:
        Button(second_frame, text="Products stock " + str(quan[9]) + " item", state=DISABLED, bg='#C7EA46',font=("Arial", 15)).grid(row=9, column=1, pady=10, padx=5)
    else : Button(second_frame, text="Out of stock", state=DISABLED, bg='#FB607F',font=("Arial", 15)).grid(row=9, column=1, pady=10, padx=5)



# Frame 3
# my_label11 = Label(my_canvas_2, image=my_img1).grid(row=0, column=0, pady=10, padx=10)

def select(image_number):
    if pid[0] == image_number:
        if quan[0] >0:
            # top = Toplevel()
            # top.title('My Second Window')
            Button(my_canvas_2, image=pdir[0])
            Button(my_canvas_2, text="SELECT", command=lambda: click(1)).grid(row=1, column=1, pady=10, padx=5)
        else : Button(my_canvas_2, text="   Out   ", state=DISABLED).grid(row=1, column=1)
    if pid[1] == image_number:    
        if quan[1] >0:
            # top = Toplevel()
            # top.title('My Second Window')
            Button(my_canvas_2, image=pdir[1])
            Button(my_canvas_2, text="SELECT", command=lambda: click(2)).grid(row=1, column=1, pady=10, padx=5)
        else : Button(my_canvas_2, text="   Out   ", state=DISABLED).grid(row=1, column=1)
    if pid[2] == image_number:    
        if quan[2] >0:
            # top = Toplevel()
            # top.title('My Second Window')
            Button(my_canvas_2, image=pdir[2])
            Button(my_canvas_2, text="SELECT", command=lambda: click(3)).grid(row=1, column=1, pady=10, padx=5)
        else : Button(my_canvas_2, text="   Out   ", state=DISABLED).grid(row=1, column=1)
    if pid[3] == image_number:    
        if quan[3] >0:
            # top = Toplevel()
            # top.title('My Second Window')
            Button(my_canvas_2, image=pdir[3])
            Button(my_canvas_2, text="SELECT", command=lambda: click(4)).grid(row=1, column=1, pady=10, padx=5)
        else : Button(my_canvas_2, text="   Out   ", state=DISABLED).grid(row=1, column=1)
    if pid[4] == image_number:    
        if quan[4] >0:
            # top = Toplevel()
            # top.title('My Second Window')
            Button(my_canvas_2, image=pdir[4])
            Button(my_canvas_2, text="SELECT", command=lambda: click(5)).grid(row=1, column=1, pady=10, padx=5)
        else : Button(my_canvas_2, text="   Out   ", state=DISABLED).grid(row=1, column=1)
    if pid[5] == image_number:    
        if quan[5] >0:
            # top = Toplevel()
            # top.title('My Second Window')
            Button(my_canvas_2, image=pdir[5])
            Button(my_canvas_2, text="SELECT", command=lambda: click(6)).grid(row=1, column=1, pady=10, padx=5)
        else : Button(my_canvas_2, text="   Out   ", state=DISABLED).grid(row=1, column=1)
    if pid[6] == image_number:    
        if quan[6] >0:
            # top = Toplevel()
            # top.title('My Second Window')
            Button(my_canvas_2, image=pdir[6])
            Button(my_canvas_2, text="SELECT", command=lambda: click(7)).grid(row=1, column=1, pady=10, padx=5)
        else : Button(my_canvas_2, text="   Out   ", state=DISABLED).grid(row=1, column=1)
    if pid[7] == image_number:    
        if quan[7] >0:
            # top = Toplevel()
            # top.title('My Second Window')
            Button(my_canvas_2, image=pdir[7])
            Button(my_canvas_2, text="SELECT", command=lambda: click(8)).grid(row=1, column=1, pady=10, padx=5)
        else : Button(my_canvas_2, text="   Out   ", state=DISABLED).grid(row=1, column=1)
    if pid[8] == image_number:    
        if quan[8] >0:
            # top = Toplevel()
            # top.title('My Second Window')
            Button(my_canvas_2, image=pdir[8])
            Button(my_canvas_2, text="SELECT", command=lambda: click(9)).grid(row=1, column=1, pady=10, padx=5)
        else : Button(my_canvas_2, text="   Out   ", state=DISABLED).grid(row=1, column=1)
    if pid[9] == image_number:    
        if quan[9] >0:
            # top = Toplevel()
            # top.title('My Second Window')
            Button(my_canvas_2, image=pdir[9])
            Button(my_canvas_2, text="SELECT", command=lambda: click(10)).grid(row=1, column=1, pady=10, padx=5)
        else : Button(my_canvas_2, text="   Out   ", state=DISABLED).grid(row=1, column=1)
    
def price_show(image_number):
    if pid[0] == image_number:
        Button(my_canvas_2, text="Price: " + str(price[0]) + " bath", state=DISABLED).grid(row=0, column=4, pady=10, padx=5)
    if pid[1] == image_number:
        Button(my_canvas_2, text="Price: " + str(price[1]) + " bath", state=DISABLED).grid(row=0, column=4, pady=10, padx=5)
    if pid[2] == image_number:
        Button(my_canvas_2, text="Price: " + str(price[2]) + " bath", state=DISABLED).grid(row=0, column=4, pady=10, padx=5)
    if pid[3] == image_number:
        Button(my_canvas_2, text="Price: " + str(price[3]) + " bath", state=DISABLED).grid(row=0, column=4, pady=10, padx=5)
    if pid[4] == image_number:
        Button(my_canvas_2, text="Price: " + str(price[4]) + " bath", state=DISABLED).grid(row=0, column=4, pady=10, padx=5)
    if pid[5] == image_number:
        Button(my_canvas_2, text="Price: " + str(price[5]) + " bath", state=DISABLED).grid(row=0, column=4, pady=10, padx=5)
    if pid[6] == image_number:
        Button(my_canvas_2, text="Price: " + str(price[6]) + " bath", state=DISABLED).grid(row=0, column=4, pady=10, padx=5)
    if pid[7] == image_number:
        Button(my_canvas_2, text="Price: " + str(price[7]) + " bath", state=DISABLED).grid(row=0, column=4, pady=10, padx=5)
    if pid[8] == image_number:
        Button(my_canvas_2, text="Price: " + str(price[8]) + " bath", state=DISABLED).grid(row=0, column=4, pady=10, padx=5)
    if pid[9] == image_number:
        Button(my_canvas_2, text="Price: " + str(price[9]) + " bath", state=DISABLED).grid(row=0, column=4, pady=10, padx=5)


cost = 0
def click(var):
    global id
    id = int(var)
    global pdir ,price
    #top heading 
    top = Toplevel()
    top.title('Payment')
    top.geometry('280x510')
    # heading = ImageTk.PhotoImage(Image.open('pic/Watar_font.png'))
    # my_label = Label(top,image=heading )
    # my_label.pack()
    #create canvas
    main_frame = Frame(top)
    main_frame.pack(fill=BOTH, expand=1)
    top_canvas = Canvas(main_frame)
    top_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    top_frame = Frame(top_canvas)
    top_canvas.create_window((0,0), window=top_frame, anchor="nw")
    
    main_frame.configure(bg='#FFE5B4')
    top_canvas.configure(bg='#FFE5B4')
    top_frame.configure(bg='#FFE5B4')

    #Back to main frame
    def comm(): 
        global cost
        cost = 0
        top.destroy()

    Button(top_frame,text='BACK',command=comm,font=("Arial", 15)).grid(row=0,column=0,padx=10,pady=10,sticky=NW)

    # Product Photo
    pro_label = Label(top_frame,image=pdir[var-1])
    pro_label.grid(row=1,column=0,padx=10,pady=10,)

    def message(var):
        item = Toplevel()
        item.title("Get your item")
        Label(item, image=pdir[var-1]).pack()

        Button(item,text='PICK UP',command=item.destroy,font=("Arial", 15)).pack()

    # Show value input money
    # budget = Label(top_frame,text='input money = 0',font=("Arial", 15))

    def option(var):
        global pdir ,price
        #spay heading 
        spay = Toplevel()
        spay.title('Select Payment')
        # spay.config(bg='#EBF5FB')
        spay.geometry('240x150')
        # heading = ImageTk.PhotoImage(Image.open('pic/Watar_font.png'))
        # my_label = Label(top,image=heading )
        # my_label.pack()
        #create canvas
        spay_frame = Frame(spay)
        spay_frame.pack(fill=BOTH, expand=1)
        spay_canvas = Canvas(spay_frame)
        spay_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        spay_frame = Frame(spay_canvas)
        spay_canvas.create_window((0,0), window=spay_frame, anchor="nw")
        
        spay_frame.configure(bg='#FFE5B4')
        spay_canvas.configure(bg='#FFE5B4')

        #Back to payment frame
        def comm2(): 
            global cost
            cost = 0
            spay.destroy()

        def pp(var):
            global Qr1, Qr2, Qr3, Qr4, Qr5, Qr6, Qr7, Qr8, Qr9, Qr10
            #top heading 
            qr = Toplevel()
            qr.title('QR code')
            qr.geometry('350x410')
            # my_label.pack()
            #create canvas
            qr_frame = Frame(qr)
            qr_frame.pack(fill=BOTH, expand=1)
            qr_canvas = Canvas(qr_frame)
            qr_canvas.pack(side=LEFT, fill=BOTH, expand=1)
            qr_frame = Frame(qr_canvas)
            qr_canvas.create_window((0,0), window=qr_frame, anchor="nw")

            qr_frame.configure(bg='#FFE5B4')
            qr_canvas.configure(bg='#FFE5B4')

            if var == 1:
                Qr1 = ImageTk.PhotoImage(Image.open("qrcode/dinosaur_qr.jpg"))
                Label(qr_frame,image=Qr1).grid(row=1,column=0,padx=10,pady=10,)
            if var == 2:
                Qr2 = ImageTk.PhotoImage(Image.open("qrcode/lays_qr.png"))
                Label(qr_frame,image=Qr2).grid(row=1,column=0,padx=10,pady=10,)
            if var == 3:
                Qr3 = ImageTk.PhotoImage(Image.open("qrcode/oreo_qr.png"))
                Label(qr_frame,image=Qr3).grid(row=1,column=0,padx=10,pady=10,)
            if var == 4:
                Qr4 = ImageTk.PhotoImage(Image.open("qrcode/birdy_qr.png"))
                Label(qr_frame,image=Qr4).grid(row=1,column=0,padx=10,pady=10,)
            if var == 5:
                Qr5 = ImageTk.PhotoImage(Image.open("qrcode/fantagreen_qr.png"))
                Label(qr_frame,image=Qr5).grid(row=1,column=0,padx=10,pady=10,)
            if var == 6:
                Qr6 = ImageTk.PhotoImage(Image.open("qrcode/fantared_qr.png"))
                Label(qr_frame,image=Qr6).grid(row=1,column=0,padx=10,pady=10,)
            if var == 7:
                Qr7 = ImageTk.PhotoImage(Image.open("qrcode/fantaorange_qr.png"))
                Label(qr_frame,image=Qr7).grid(row=1,column=0,padx=10,pady=10,)
            if var == 8:
                Qr8 = ImageTk.PhotoImage(Image.open("qrcode/coke_qr.png"))
                Label(qr_frame,image=Qr8).grid(row=1,column=0,padx=10,pady=10,)
            if var == 9:
                Qr9 = ImageTk.PhotoImage(Image.open("qrcode/oishi_qr.png"))
                Label(qr_frame,image=Qr9).grid(row=1,column=0,padx=10,pady=10,)
            if var == 10:
                Qr10 = ImageTk.PhotoImage(Image.open("qrcode/milk_qr.png"))
                Label(qr_frame,image=Qr10).grid(row=1,column=0,padx=10,pady=10,)
            else :
                print("error on qrcode")

            def confirm():
                global id
                s = 'UPDATE product set pquan = '+ str(quan[id-1] - 1) + ' WHERE pid ='+ str(id)
                with sqlite3.connect("DBVending.db") as conn:
                    c = conn.cursor()
                    c.execute(s)
                    qr_p = messagebox.showinfo(title="Payment by QR code", message="Are you sure?")
                    if qr_p == "ok":
                        oop()
                        message(var)
            Button(qr_frame,text='CONFIRM',command=confirm,font=("Arial", 15)).grid(row=4,column=0,padx=10,pady=10,sticky=NW)


        def cash(var):
            global pdir ,price
            #top heading 
            cash = Toplevel()
            cash.title('Cash')
            # top.config(bg='#EBF5FB')
            cash.geometry('500x600')
            # my_label.pack()
            #create canvas
            cash_frame = Frame(cash)
            cash_frame.pack(fill=BOTH, expand=1)
            cash_canvas = Canvas(cash_frame)
            cash_canvas.pack(side=LEFT, fill=BOTH, expand=1)
            cash_frame = Frame(cash_canvas)
            cash_canvas.create_window((0,0), window=cash_frame, anchor="nw")

            cash_frame.configure(bg='#FFE5B4')
            cash_canvas.configure(bg='#FFE5B4')

            #Back to main frame
            def commc(): 
                global cost
                cost = 0
                cash.destroy()

            Button(cash_frame,text='BACK',command=commc,font=("Arial", 15)).grid(row=0,column=0,padx=10,pady=10,sticky=NW)

            # Product Photo
            pro_label = Label(cash_frame,image=pdir[var-1])
            pro_label.grid(row=1,column=0,padx=10,pady=10,)

            # Show value input money
            budget = Label(cash_frame,text='input money = 0',font=("Arial", 15))
    
            def inputmoney():
                #make finish fungtion
        
                in_money = Toplevel()
                in_money.title('Input money')
                in_money.config(bg='#FFE5B4')
                in_money.geometry('180x180')
        
                Button(in_money,text='1 baht', command=lambda:calculate(1)).place(x=50, y=30)
                Button(in_money,text='2 baht', command=lambda:calculate(2)).place(x=50 , y=60)
                Button(in_money,text='5 baht', command=lambda:calculate(5)).place(x=50 , y=90)
                Button(in_money,text='10 baht', command=lambda:calculate(10)).place(x=50 , y=120)
                Button(in_money,text='20 baht', command=lambda:calculate(20)).place(x=100 , y=30)
                Button(in_money,text='50 baht', command=lambda:calculate(50)).place(x=100 , y=60)
                Button(in_money,text='100 baht', command=lambda:calculate(100)).place(x=100 , y=30)
                # Button(in_money,text='input',command=lambda:calculate(money.get())).pack(padx=5,pady=5)
                Button(in_money,text='back', command=in_money.destroy).place(x=5, y=5)
                def calculate(money):
                    global cost
                    cost += int(money)
                    p =  price[var-1]
                    if(cost>=p):
                        paid = 'You change is \n'
                        change = cost - p
                        print(str(cost)+","+str(p)+","+str(change))
                        if change >= 10:
                            paid += '10 baht x '+str(int(change/10))+'\n'
                            change = change % 10
                        if change >= 5:
                            paid += '5 baht x '+str(int(change/5))+'\n'
                            change = change % 5
                        if change >= 2:
                            paid += '2 baht x '+str(int(change/2))+'\n'
                            change = change % 2
                        if change >= 1:
                            paid += '1 baht x '+str(int(change/1))+'\n'
                            change = change % 1
                        budget.configure(text='input money ='+str(cost))
                        resp = messagebox.showinfo(title='info', message=paid+'Get your product below')
                        if resp == 'ok':
                            message(var)
                            cost = 0
                            budget.configure(text='input money ='+str(cost))
                            s = 'UPDATE product set pquan = '+ str(quan[var-1] - 1) + ' WHERE pid ='+ str(var)
                            quan[var -1] -= 1
                            with sqlite3.connect("DBVending.db") as conn:
                                c = conn.cursor()
                                c.execute(s) 
                            in_money.destroy()
                            cash.destroy()
                            top.destroy()
                            spay.destroy()
                    else:
                        budget.configure(text='input money ='+str(cost))

            Label(cash_frame,text='Price = '+str(price[var-1],),font=("Arial", 15)).grid(row=3,column=1,sticky=NW)
        
            budget.grid(row=4,column=1,sticky=NW)
            Button(cash_frame,text='inputmoney' ,command=inputmoney,font=("Arial", 15)).grid(row=6,column=1,sticky=NW) 


        Button(spay_frame,text='CANCEL',command=comm2,font=("Arial", 15)).grid(row=0,column=0,padx=10,pady=10,sticky=NW)

        Button(spay_frame,text='Prompt Pay',command=lambda: pp(var),font=("Arial", 15)).grid(row=2,column=0,padx=10,pady=10,sticky=NW)
        Button(spay_frame,text='Cash',command=lambda: cash(var),font=("Arial", 15)).grid(row=2,column=1,padx=10,pady=10,sticky=NW)

    # Select option for payment
    Button(top_frame, text='Please select a payment method for your order.', command=lambda: option(var)).grid(row=3,column=0,padx=10,pady=10)
    
    # budget.grid(row=4,column=3,sticky=NW)
    # Button(top_frame,text='inputmoney' ,command=inputmoney()).grid(row=5,column=3,sticky=NW) 
        #return print("success")
    
    # Label(top_frame,text='Price = '+str(price[var-1],),font=("Arial", 15)).grid(row=3,column=1,sticky=NW)
        
    # budget.grid(row=4,column=1,sticky=NW)
    # Button(top_frame,text='inputmoney' ,command=inputmoney,font=("Arial", 15)).grid(row=6,column=1,sticky=NW) 

    #Button(top_frame,text='Money' ,command=lambda:showMoney(var)).grid(row=1,column=3,padx=10,pady=10,sticky=NW)
    #Button(top_frame,text='Qrcode' ,command=lambda:showQrcode(var)).grid(row=2,column=3,padx=10,pady=10)
    #footer toplevel
    # footer = ImageTk.PhotoImage(Image.open('pic/my_footer.png'))
    # my_label2 = Label(top,image=footer )
    # my_label2.pack()

    

    

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7, my_img8, my_img9, my_img10]

status = Label(my_canvas_2, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E) # E = right

my_label = Label(my_canvas_2, image=my_img1)
my_label.grid(row=0, column=0, columnspan=3,  pady=10, padx=10)

image_number = 1
select(image_number)

price_show(image_number)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(my_canvas_2, image=image_list[image_number-1])
    button_forward = Button(my_canvas_2, text=">>", command= lambda: forward(image_number+1))
    button_back = Button(my_canvas_2, text="<<", command= lambda: back(image_number-1))
    
    if image_number == 10:
        button_forward = Button(my_canvas_2, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3, pady=10, padx=10)
    button_back.grid(row=1, column=0, pady=10, padx=10)
    button_forward.grid(row=1, column=2, pady=10, padx=10)

    status = Label(my_canvas_2, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    
    select(image_number)

    price_show(image_number)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(my_canvas_2, image=image_list[image_number-1])
    button_forward = Button(my_canvas_2, text=">>", command= lambda: forward(image_number+1))
    button_back = Button(my_canvas_2, text="<<", command= lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(my_canvas_2, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3, pady=10, padx=10)
    button_back.grid(row=1, column=0, pady=10, padx=10)
    button_forward.grid(row=1, column=2, pady=10, padx=10)
    
    #Update Status Bar
    status = Label(my_canvas_2, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    
    select(image_number)

    price_show(image_number)


button_back = Button(my_canvas_2, text="<<", command=back, state=DISABLED)
button_forward = Button(my_canvas_2, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

# <script type="text/javascript">     
#       var qr_dom = document.getElementById('qrcode');
#       function render_qr(x){
#         var acc_id = '0610545641';
#         var amount = x;
#         var txt = PromptPayQR.gen_text(acc_id, amount);
#         qr_dom.innerHTML = "";
#         if(txt){
#           new QRCode(qr_dom, txt);
#         }
#       }
#       document.getElementById('amount').addEventListener('click', render_qr, true);
#       console.log("Complete");
# </script>
oop()

root.mainloop()