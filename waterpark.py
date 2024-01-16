import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime

waterpark=Tk()
waterpark.title("WATERPARKISTRE'S TICKET SYSTEM")
waterpark.geometry('500x600')
greeting=tk.Label(text="Welcome To Waterparkistre!",font=('ink free', 25,'bold'), bg="#CFECEC", fg="black")
greeting.pack(fill=X and Y)
waterpark.config(bg='#CFECEC')

img = PhotoImage(file="C:/Users/Huawei/Downloads/logo.png")
my_label=Label(waterpark, image=img, bg="#CFECEC", fg="black")
my_label.pack(fill=X and Y)

def NextPage():
    waterpark.destroy()
    pay = Tk()
    pay.geometry("1000x700")
    pay.title("WATERPARKISTRE'S TICKET SYSTEM")
    canvas = Canvas(pay, width=1000, height=700, bg="#CFECEC")
    canvas.pack()

    def NextPage2():
        pay.destroy()
        root = Tk()
        root.title("RECIEPT")
        root.geometry('690x600')
        bg_color = '#CFECEC'
        title = Label(text="WATERPAKISTRE", bd=12, bg="#36454F", fg="#CFECEC",
                      font=('times new roman', 25, 'bold'), relief=GROOVE, justify=CENTER)
        title.pack(fill=X)
        root.config(bg="#36454F")

        def reciept():
            if int(count_J_Kid.get()) > 0:
                junior_kidprice = 0
            else:
                junior_kidprice = 0
            if int(count_Kid.get()) > 0:
                Kidprice = int(count_Kid.get()) * 70.75
            else:
                Kidprice = 0
            if int(count_Teen.get()) > 0:
                Teenprice = int(count_Teen.get()) * 90.60
            else:
                Teenprice = 0
            if int(count_Adult.get()) > 0:
                Adultprice = int(count_Adult.get()) * 110.95
            else:
                Adultprice = 0
            if int(counter1.get()) > 0:
                kidprice = int(counter1.get()) * 16
            else:
                kidprice = 0
            if int(counter2.get()) > 0:
                singleprice = int(counter2.get()) * 25
            else:
                singleprice = 0
            if int(counter3.get()) > 0:
                dblprice = int(counter3.get()) * 30
            else:
                dblprice = 0

            total_payment = float(junior_kidprice + Kidprice + Teenprice + Adultprice + kidprice + singleprice + dblprice)
            print('Name\t\t\t: ' + str(name1.get()))
            print('Total Payment\t: RM' + str('{:.2f}'.format(total_payment)))
            messagebox.showinfo("RECEIPT",
                                "==============================\n          WATERPARKISTRE ONLINE BOOKING\n==============================" +
                                "\nName\t\t: " + str(name1.get()) +
                                "\nEmail\t\t: " + str(email1.get()) +
                                "\nPhone Number\t: " + str(phone1.get()) +
                                "\nDate\t\t: " + str(cal.get_date()) +
                                "\nJunior Kid (free)\t: " + str(count_J_Kid.get()) +
                                "\nKid (RM70.75)\t: " + str(count_Kid.get()) +
                                "\nTeen (RM90.60)\t: " + str(count_Teen.get()) +
                                "\nAdult (RM110.95)\t: " + str(count_Adult.get()) +
                                "\nFloater\t\t: " + str(counter1.get()) + " Kid," + str(
                                    counter2.get()) + " Single," + str(counter3.get()) + " Double" +
                                "\n==============================" +
                                "\n\nTotal Payment\t: RM" + str('{:.2f}'.format(total_payment)) +
                                "\nPlease enter your name in QR Code section and\nproceed with your payment.\n\nYou can screenshot this receipt for your reminder.\nThank you for your booking!")

        def QRwindow():
            root.destroy()
            import qrcode

        def exit():
            op = messagebox.askyesno("Warning!", "Please view your receipt and proceed with payment in QR Code section else your booking will be cancel.\n\nCancel booking?")
            if op > 0:
                root.destroy()

        F2 = LabelFrame(root, font=('times new roman', 18), fg='black', bg="#CFECEC")
        F2.place(x=20, y=75)#width=690, height=700

        btn1 = Button(F2, text='RECIEPT', font='arial 15 bold', command=reciept, padx=5, pady=10,bg="#36454F",
        fg = "#CFECEC",width=15)
        btn1.grid(row=1, column=1, padx=230, pady=40)
        btn2 = Button(F2, text='QR CODE', font='arial 15 bold', command=QRwindow, padx=5, pady=10,bg="#36454F",
        fg = "#CFECEC", width=15)
        btn2.grid(row=2, column=1, padx=230, pady=40)
        btn3 = Button(F2, text='EXIT', font='arial 15 bold', padx=5, pady=10, command=exit, bg="#36454F",
        fg = "#CFECEC", width=15)
        btn3.grid(row=3, column=1, padx=230, pady=40)

        root.mainloop()

    calinfo = Label(text="1. Choose Date", font=("Times", "12"), bg="#CFECEC", fg="black")
    calinfo.pack()
    calinfo.place(x=100, y=65)
    cal = Calendar(pay, selectmode='day',
                   mindate=datetime.now())
    cal.place(x=130, y=90)

    def getDate():
        dt.config(text="Selected Date is: " + cal.get_date())

    dt = Button(pay, text="Get Date", command=getDate, bg="#36454F", fg="#CFECEC")
    dt.place(x=230, y=280)
    dt = Label(pay, text="", fg='black', bg='#CFECEC')
    dt.place(x=195, y=310)

    count_Adult = IntVar()
    count_Teen = IntVar()
    count_Kid = IntVar()
    count_J_Kid = IntVar()
    counter1 = IntVar()
    counter2 = IntVar()
    counter3 = IntVar()

    def add_Adult(event=None):
        count_Adult.set(count_Adult.get() + 1)

    def dec_Adult(event=None):
        count_Adult.set(count_Adult.get() - 1)

    def AddTeen(event=None):
        count_Teen.set(count_Teen.get() + 1)

    def DecTeen(event=None):
        count_Teen.set(count_Teen.get() - 1)

    def AddKid(event=None):
        count_Kid.set(count_Kid.get() + 1)

    def DecKid(event=None):
        count_Kid.set(count_Kid.get() - 1)

    def AddJ_Kid(event=None):
        count_J_Kid.set(count_J_Kid.get() + 1)

    def DecJ_Kid(event=None):
        count_J_Kid.set(count_J_Kid.get() - 1)

    def onClick1(event=None):
        counter1.set(counter1.get() + 1)

    def offClick1(event=None):
        counter1.set(counter1.get() - 1)

    def onClick2(event=None):
        counter2.set(counter2.get() + 1)

    def offClick2(event=None):
        counter2.set(counter2.get() - 1)

    def onClick3(event=None):
        counter3.set(counter3.get() + 1)

    def offClick3(event=None):
        counter3.set(counter3.get() - 1)


    greeting = Label(
        text="Welcome To Waterparkistre's Online Ticket!",
        font=('ink free', 25,'bold'), bg="#CFECEC", fg="blue")
    greeting.pack()
    greeting.place(x=200, y=5)

    ticketinfo = Label(text="2. Choose Ticket", font=("Times", "12"), bg="#CFECEC", fg="black")
    ticketinfo.pack()
    ticketinfo.place(x=450, y=65)

    J_Kid = Label(
        text="Junior Kid\n(age 6 years old and below)  ",
        font=('Comic Sans MS', '10'),
        bg = "#36454F",
        fg = "#CFECEC")
    J_Kid.pack()
    J_Kid.place(x=450, y=100)
    J_Kidp = Label(
        text="Free",
        font=('Comic Sans MS', '10'),
        bg="#CFECEC",
        fg="black")
    J_Kidp.pack()
    J_Kidp.place(x=700, y=105)
    Jkidplus = Button(text="+", width=3, height=1, command=AddJ_Kid, bg="#36454F", fg="#CFECEC")
    Jkidplus.pack()
    Jkidplus.place(x=780, y=105)
    Jkidminus = Button(text="-", width=3, height=1, command=DecJ_Kid, bg="#36454F", fg="#CFECEC")
    Jkidminus.pack()
    Jkidminus.place(x=810, y=105)
    Jkidqty = Label(pay, textvariable=count_J_Kid, bg="#CFECEC", fg="black")
    Jkidqty.pack()
    Jkidqty.place(x=855, y=107)

    Kid = Label(
        text="Kid\n(age 7 - 12 years old)            ",
        font=('Comic Sans MS', '10'),
        bg= "#36454F",
        fg = "#CFECEC")
    Kid.pack()
    Kid.place(x=450, y=160)
    Kidp = Label(
        text="RM70.75",
        font=('Comic Sans MS', '10'),
        bg="#CFECEC",
        fg="black")
    Kidp.pack()
    Kidp.place(x=685, y=165)
    Kidplus = Button(text="+", width=3, height=1, command=AddKid, bg="#36454F", fg="#CFECEC")
    Kidplus.pack()
    Kidplus.place(x=780, y=165)
    Kidminus = Button(text="-", width=3, height=1, command=DecKid, bg="#36454F", fg="#CFECEC")
    Kidminus.pack()
    Kidminus.place(x=810, y=165)
    Kidqty = Label(pay, textvariable=count_Kid, bg="#CFECEC", fg="black")
    Kidqty.pack()
    Kidqty.place(x=855, y=167)

    Teen = Label(
        text="Teen\n(age 13 - 19 years old)          ",
        font=('Comic Sans MS', '10'),
        bg= "#36454F",
        fg = "#CFECEC")
    Teen.pack()
    Teen.place(x=450, y=220)
    Teenp = Label(
        text="RM90.60",
        font=('Comic Sans MS', '10'),
        bg="#CFECEC",
        fg="black")
    Teenp.pack()
    Teenp.place(x=685, y=225)
    teenplus = Button(text="+", width=3, height=1, command=AddTeen, bg="#36454F", fg="#CFECEC")
    teenplus.pack()
    teenplus.place(x=780, y=225)
    teenminus = Button(text="-", width=3, height=1, command=DecTeen, bg="#36454F", fg="#CFECEC")
    teenminus.pack()
    teenminus.place(x=810, y=225)
    teenqty = Label(pay, textvariable=count_Teen, bg="#CFECEC", fg="black")
    teenqty.pack()
    teenqty.place(x=855, y=227)

    Adult = Label(
        text="Adult\n(age 20 years old and above)",
        font=('Comic Sans MS', '10'),
        bg= "#36454F",
        fg = "#CFECEC")
    Adult.pack()
    Adult.place(x=450, y=280)
    Adult = Label(
        text="RM110.95",
        font=('Comic Sans MS', '10'),
        bg="#CFECEC",
        fg="black")
    Adult.pack()
    Adult.place(x=685, y=285)
    adultplus = Button(text="+", width=3, height=1, command=add_Adult, bg="#36454F", fg="#CFECEC")
    adultplus.pack()
    adultplus.place(x=780, y=285)
    adultminus = Button(text="-", width=3, height=1, command=dec_Adult(), bg="#36454F", fg="#CFECEC")
    adultminus.pack()
    adultminus.place(x=810, y=285)
    adultqty = Label(pay, textvariable=count_Adult, bg="#CFECEC", fg="black")
    adultqty.pack()
    adultqty.place(x=855, y=287)

    floaterinfo = Label(text="3. Floater Rental", font=("Times", "12"), bg="#CFECEC", fg="black")
    floaterinfo.pack()
    floaterinfo.place(x=100, y=370)

    kid1 = PhotoImage(file="C:/Users/Huawei/Downloads/kid.png")
    canvas.create_image(130, 400, anchor=NW, image=kid1)
    kid2 = Label(pay, font=("Times", "12"), text='Kid - RM16.00', bg="#CFECEC", fg="black")
    kid2.pack()
    kid2.place(x=150, y=550)
    kidplus = Button(text="+", width=3, height=1, command=onClick1, bg="#36454F", fg="#CFECEC")
    kidplus.pack()
    kidplus.place(x=160, y=575)
    kidminus = Button(text="-", width=3, height=1, command=offClick1, bg="#36454F", fg="#CFECEC")
    kidminus.pack()
    kidminus.place(x=190, y=575)
    kidqty = Label(pay, textvariable=counter1, bg="#CFECEC", fg="black")
    kidqty.pack()
    kidqty.place(x=235, y=577)

    single1 = PhotoImage(file="C:/Users/Huawei/Downloads/single.png")
    canvas.create_image(300, 400, anchor=NW, image=single1)
    single2 = Label(pay, font=("Times", "12"), text='Single - RM25.00', bg="#CFECEC", fg="black")
    single2.pack()
    single2.place(x=320, y=550)
    singleplus = Button(text="+", width=3, height=1, command=onClick2, bg="#36454F", fg="#CFECEC")
    singleplus.pack()
    singleplus.place(x=330, y=575)
    singleminus = Button(text="-", width=3, height=1, command=offClick2, bg="#36454F", fg="#CFECEC")
    singleminus.pack()
    singleminus.place(x=360, y=575)
    singleqty = Label(pay, textvariable=counter2, bg="#CFECEC", fg="black")
    singleqty.pack()
    singleqty.place(x=405, y=577)

    dbl1 = PhotoImage(file="C:/Users/Huawei/Downloads/double.png")
    canvas.create_image(470, 400, anchor=NW, image=dbl1)
    dbl2 = Label(pay, font=("Times", "12"), text='Double - RM30.00', bg="#CFECEC", fg="black")
    dbl2.pack()
    dbl2.place(x=490, y=550)
    dblplus = Button(text="+", width=3, height=1, command=onClick3, bg="#36454F", fg="#CFECEC")
    dblplus.pack()
    dblplus.place(x=500, y=575)
    dblminus = Button(text="-", width=3, height=1, command=offClick3, bg="#36454F", fg="#CFECEC")
    dblminus.pack()
    dblminus.place(x=530, y=575)
    dblqty = Label(pay, textvariable=counter3, bg="#CFECEC", fg="black")
    dblqty.pack()
    dblqty.place(x=575, y=577)

    btnNext2 = Button(text='Submit Booking', width=15, height=1, command=NextPage2)
    btnNext2.place(x=500, y=650)

    pay.mainloop()

btnNext=Button(text="Next Page", width=10, height=1, command=NextPage)
btnNext.place(x=380, y=560)

name = Label(waterpark,font=("Times", "12"),text='Name:',bg="#CFECEC")
name.pack()
name1 =StringVar()
entry1 = Entry(waterpark, fg='black', bg='light blue', width=50 ,textvariable=name1)
entry1.pack(ipadx=20)
email= Label(waterpark,font=("Times", "12"), text='Email: ',bg="#CFECEC")
email.pack()
email1=StringVar()
entry2 = Entry(waterpark, fg='black', bg='light blue', width=50,textvariable=email1)
entry2.pack(ipadx=20)
phone = Label(waterpark, font=("Times", "12"), text='Phone number:',bg="#CFECEC")
phone.pack()
phone1 = StringVar()
entry3 = Entry(waterpark, fg='black', bg='light blue', width=50, textvariable=phone1)
entry3.pack(ipadx=20)

waterpark.mainloop()
