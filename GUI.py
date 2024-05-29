from tkinter import *
import numpy as nm
import matplotlib.pyplot as mtp
import pandas as pd
from tkinter import *
from tkinter import messagebox
import time
import classify
import PIL.Image
# import mysql.connector
import sqlite3
import warnings

warnings.filterwarnings("ignore")


# %matplotlib inline
# plt.rcParams.update({'figure.figsize':(7,5), 'figure.dpi':100})


def sigup():
    R1.withdraw()
    R2 = Toplevel()
    # R2.geometry('900x600')
    R2.title('SigUp Now')
    width = R2.winfo_screenwidth()
    height = R2.winfo_screenheight()
    R2.geometry("%dx%d" % (width, height))
    reg = PhotoImage(file="reg.png")
    my_label = Label(R2, image=reg)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)


    def Sigups():
        usernames = username.get()
        passwords = password.get()
        phonenos = phoneno.get()
        Address = address.get()
        conn = sqlite3.connect('w1.db')
        with conn:
            cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS wt1 (Username TEXT,Password TEXT,Phoneno TEXT,Address TEXT)')
        cursor.execute('INSERT INTO wt1 (Username,Password ,Phoneno,Address) VALUES(?,?,?,?)',
                       (usernames, passwords, phonenos, Address,))
        conn.commit()
        if username.get() == "" or password.get() == "":
            messagebox.showinfo("sorry", "Pease fill the required information")
            # login()
        else:
            messagebox.showinfo("Welcome to %s" % usernames, "Let Login")
            login()

    lblInfo = Label(R2, text="Username", fg="black", font=("bold", 15))
    lblInfo.place(x=520, y=140)

    lblInfo = Label(R2, text="Password", fg="black", font=("bold", 15))
    lblInfo.place(x=520, y=190)

    lblInfo = Label(R2, text="Phone-no", fg="black", font=("bold", 15))
    lblInfo.place(x=520, y=240)

    lblInfo = Label(R2, text="Address", fg="black", font=("bold", 15))
    lblInfo.place(x=520, y=290)

    username = Entry(R2, width=20, font=("bold", 15), highlightthickness=2)
    username.place(x=700, y=140)

    password = Entry(R2, show="**", width=20, font=("bold", 15), highlightthickness=2)
    password.place(x=700, y=190)

    phoneno = Entry(R2, width=20, font=("bold", 15), highlightthickness=2)
    phoneno.place(x=700, y=240)

    address = Entry(R2, width=20, font=("bold", 15), highlightthickness=2)
    address.place(x=700, y=290)

    signUpbt = Button(R2, text="SignUp", width=10, height=2, fg="black", font=('algerian', 15, 'bold'),
                      justify='center', bg="light blue", command=lambda: [Sigups(), R1.withdraw()])
    signUpbt.place(x=680, y=490)

    R2.mainloop()


# info@sunsys.co.in

def login():
    def logininto():
        usernames = e1.get()
        passwords = e2.get()
        conn = sqlite3.connect('w1.db')
        with conn:
            cursor = conn.cursor()
        ('CREATE TABLE IF NOT EXISTS wt1 (Username TEXT,Password TEXT,Phoneno TEXT)')
        conn.commit()
        if usernames == "" and passwords == "":
            messagebox.showinfo("sorry", "Please complete the required field")
        else:
            cursor.execute('SELECT * FROM wt1 WHERE Username = "%s" and Password = "%s"' % (usernames, passwords))
            for i in usernames:
                if cursor.fetchall():
                    messagebox.showinfo("Welcome %s" % usernames, "Logged in successfully")
                    quest()

                else:
                    messagebox.showinfo("Sorry", "Wrong Password")
                    return

    R3 = Toplevel()
    # R3.geometry('900x600')
    R3.title("LOGIN NOW")
    width = R3.winfo_screenwidth()
    height = R3.winfo_screenheight()
    R3.geometry("%dx%d" % (width, height))
    log = PhotoImage(file="reg.png")
    my_label = Label(R3, image=log)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)

    lblInfo = Label(R3, text="Username", fg="black", font=("bold", 15))
    lblInfo.place(x=520, y=200)

    lblInfo = Label(R3, text="Password", fg="black", font=("bold", 15))
    lblInfo.place(x=520, y=300)

    e1 = Entry(R3, width=15, font=("bold", 17), highlightthickness=2, bg="WHITE", relief=SUNKEN)
    e1.place(x=700, y=200)

    e2 = Entry(R3, width=15, font=("bold", 17), show="*", highlightthickness=2, bg="WHITE", relief=SUNKEN)
    e2.place(x=700, y=300)

    btn = Button(R3, text="LOGIN", width=10, height=2, fg="black", font=('algerian', 15, 'bold'), justify='center',
                 bg="light blue", command=logininto)
    btn.place(x=680, y=400)

    R3.mainloop()


sum = 0


def quest():
    # from tkinter import *
    sum = 0
    ws = Tk()
    ws.title('PythonGuides')
    width = ws.winfo_screenwidth()
    height = ws.winfo_screenheight()
    ws.geometry("%dx%d" % (width, height))


    def display_selected(choice):
        choice = variable.get()
        print(type(choice))

        global sum
        if choice == "Not at all":
            choice1 = 0
        elif choice == "Several days":
            choice1 = 1
        elif choice == "More than half the days":
            choice1 = 2
        else:
            choice1 = 3

        # choice = variable.get()
        sum += int(choice1)

    def sums():
        global sum
        print(sum)
        selection1 = sum / 27
        # print(selection1)
        if (sum <= 4):
            message1.config(text="Normal")
            # time.sleep(5)
        elif (sum <= 9):
            message1.config(text="Mild")

            classify.detect_emotio(sum)
        elif (sum <= 14):
            message1.config(text="Moderate")

            classify.detect_emotio(sum)
        elif (sum <= 19):
            message1.config(text="Moderately Severe")

            classify.detect_emotio(sum)
        elif (sum <= 27):
            message1.config(text="Severe")

            classify.detect_emotio(sum)

        sum = 0

    countries = ['Not at all', 'Several days', 'More than half the days', 'Nearly every day']
    la = Label(ws, text="Over the last two weeks, how often have you been bothered by any of the following problems?",
               font=('bold', 21),pady=8).pack()


    la1 = Label(ws, text="1.Little interest or pleasure in doing things?", fg="green", font=('bold', 16),padx=35)
    la1.place(x=0, y=100)

    la1 = Label(ws, text="2.Feeling down, depressed, or hopeless?", fg="green", font=('bold', 16),padx=35)
    la1.place(x=0, y=150)

    la1 = Label(ws, text="3.Trouble falling or staying asleep, or sleeping too much?", fg="green", font=('bold', 16),padx=35)
    la1.place(x=0, y=200)
    la1 = Label(ws, text="4.Feeling tired or having little energy?", fg="green", font=('bold', 16),padx=35)
    la1.place(x=0, y=250)
    la1 = Label(ws, text="5.Poor appetite or overeating?", fg="green", font=('bold', 16),padx=35)
    la1.place(x=0, y=300)
    la1 = Label(ws,
                text="6.Feeling bad about yourself - or that you are a failure or have let yourself or your family down?",
                fg="green", font=('bold', 16),padx=35)
    la1.place(x=0, y=350)
    la1 = Label(ws, text="7.Trouble concentrating on things, such as reading the newspaper or watching television?",
                fg="green", font=('bold', 16),padx=35)
    la1.place(x=0, y=400)
    la1 = Label(ws, text="8.Moving or speaking so slowly that other people could have noticed?"
                         'Or the opposite - being so fidgety or restless that you have been moving around a lot more than usual?',
                fg="green", font=('bold', 16),padx=35)
    la1.place(x=0, y=450)
    la1 = Label(ws, text="9.Thoughts that you would be better off dead, or of hurting yourself in some way?", fg="green",
                font=('bold', 16),padx=35)
    la1.place(x=0, y=500)
    # setting variable for Integers
    variable = StringVar(ws)
    variable.set(countries[0])
    variable1 = StringVar(ws)
    variable1.set(countries[0])
    variable2 = StringVar(ws)
    variable2.set(countries[0])
    variable3 = StringVar(ws)
    variable3.set(countries[0])
    variable4 = StringVar(ws)
    variable4.set(countries[0])
    variable5 = StringVar(ws)
    variable5.set(countries[0])
    variable6 = StringVar(ws)
    variable6.set(countries[0])
    variable7 = StringVar(ws)
    variable7.set(countries[0])
    variable8 = StringVar(ws)
    variable8.set(countries[0])


    # creating widget
    dropdown1 = OptionMenu(
        ws,
        variable,
        *countries

    )
    dropdown1.pack()
    dropdown2 = OptionMenu(
        ws,
        variable1,
        *countries,
        command=display_selected
    )
    dropdown3 = OptionMenu(ws, variable2, *countries, command=display_selected)
    dropdown4 = OptionMenu(ws, variable3, *countries, command=display_selected)
    dropdown5 = OptionMenu(ws, variable4, *countries, command=display_selected)
    dropdown6 = OptionMenu(ws, variable5, *countries, command=display_selected)
    dropdown7 = OptionMenu(ws, variable6, *countries, command=display_selected)
    dropdown8 = OptionMenu(ws, variable7, *countries, command=display_selected)
    dropdown9 = OptionMenu(ws, variable8, *countries, command=display_selected)
    # positioning widget
    dropdown1.place(x=1200, y=100)
    dropdown2.place(x=1200, y=150)
    dropdown3.place(x=1200, y=200)
    dropdown4.place(x=1200, y=250)
    dropdown5.place(x=1200, y=300)
    dropdown6.place(x=1200, y=350)
    dropdown7.place(x=1200, y=400)
    dropdown8.place(x=1200, y=450)
    dropdown9.place(x=1200, y=500)
    b1 = Button(ws, text="Submit", bg='green', fg='yellow', command=sums, font=('Times', 16))
    b1.place(x=50, y=690)
    message1 = Label(ws, text="", bg="yellow", fg="red", width=30, height=2, activebackground="yellow",
                     font=('times', 15, ' bold '))
    message1.place(x=200, y=680)
    # infinite loop
    ws.mainloop()


R1 = Tk()

R1.title('SigUp Now')
width = R1.winfo_screenwidth()
height = R1.winfo_screenheight()
R1.geometry("%dx%d" % (width, height))
bg=PhotoImage(file="bg1.png")
my_label=Label(R1,image=bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1)
la = Label(R1, text="Mental Health prediction", font=('algerian', 15, 'bold'))
la.place(x=600, y=100)

Registerbt = Button(R1, text="REGISTER", width=17, height=2, font=('algerian', 15, 'bold'), justify='center',
                    bg="light blue", relief=SUNKEN, command=sigup)
loginbt = Button(R1, text="LOGIN", width=17, height=2, font=('algerian', 15, 'bold'), justify='center', bg="light blue",
                 relief=SUNKEN, command=login)
Registerbt.place(x=650, y=200)
loginbt.place(x=650, y=300)
R1.mainloop()
# quest()
