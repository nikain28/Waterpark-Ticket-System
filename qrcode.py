from tkinter import *
from tkinter import messagebox
import pyqrcode
import webbrowser

def QRwindow():
    root = Tk()
    root.title("QR CODE & PAYMENT")
    root.geometry("400x600")
    root.config(bg='#CFECEC')

    def generate_QR():

        def jpay():
            webbrowser.open_new("https://billercentre.jompay.prod.inet.paynet.my/login.aspx")

        def tng():
            webbrowser.open_new("https://tngportal.touchngo.com.my/tngPortal/login")
        def exit():
            op = messagebox.askyesno("Exit", "Your ticket has successfully booked.\nThank you for using our online ticket booking!\n\nDo you really want to exit?")
            if op > 0:
                root.destroy()

        if len(user_input.get()) != 0:
            global qr, img
            qr = pyqrcode.create(user_input.get())
            img = BitmapImage(data=qr.xbm(scale=8))
        else:
            messagebox.showwarning('warning', 'All Fields are Required!')
        try:
            display_code()
        except:
            pass

        msg = Label(root, font=("Times", "10"),
                    text='Please screenshot this QR Code for entry purpose.\n\nProceed payment with:',
                    bg="#CFECEC", fg="black")
        msg.pack()
        msg.place(x=70, y=400)
        payOption = StringVar()
        opt1 = Radiobutton(root, text="Online Banking JomPAY", variable=payOption, value="Online Banking JomPAY",
                           tristatevalue=0, command=jpay, bg="#CFECEC")
        opt1.place(x=130, y=460)
        opt2 = Radiobutton(root, text="Touch n Go eWallet", variable=payOption, value="Touch n Go eWallet",
                           tristatevalue=0, command=tng, bg="#CFECEC")
        opt2.place(x=130, y=480)
        btnreturn = Button(text='EXIT', width=15, height=1, command=exit, bg="#36454F", fg="#CFECEC")
        btnreturn.place(x=140, y=550)

    def display_code():
        img_lbl.config(image=img)
        output.config(text="QR code of " + user_input.get(), bg="#CFECEC",fg = "black")

    lbl = Label(root, text="Enter name as in receipt:",bg="#CFECEC",fg = "black")
    lbl.pack()

    user_input = StringVar()
    entry = Entry(root, textvariable=user_input)
    entry.pack(padx=10)

    button = Button(root, text="generate_QR", width=15, command=generate_QR, bg="#36454F",fg = "#CFECEC")
    button.pack(pady=10)
    img_lbl = Label(root, bg="#CFECEC")
    img_lbl.pack()
    output = Label(root, text="")
    output.pack()

    root.mainloop()

QRwindow()