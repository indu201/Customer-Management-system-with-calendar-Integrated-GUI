from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import datetime
from tkinter import messagebox

top=Tk()
top.title('Welcome')
top.geometry("1300x650")

def show():
    if e2.cget("show")=="*":
        e2.config(show="")
    else:
        e2.config(show="*")

def login():
    import pymysql as sql
    db=sql.connect(
        host="localhost",
        user="root",
        password="king123@#",
        db="student_db"
    )
    cur = db.cursor()
    cur.execute("select * from customer where name = %s and password = %s", (e1.get(), e2.get()))
    row = cur.fetchone()

    if row == None:
        messagebox.showerror("Error", "Invalid User Name And Password")

    else:
        top.destroy()
        import welcome



path="C:\\Users\\Aditya\\Pictures\\aditya.jpg"
img=ImageTk.PhotoImage(Image.open(path).resize((1400, 700)))

L12=Label(top, image=img)
L12.pack()


L=Label(top, text="Welcome", bg="salmon", fg="white", font=("Arial 30 bold"))
L.place(x=600, y=30)

L2=Label(top, text="Name", bg="gray", fg="white", font=("Arial 20 bold"))
L2.place(x=150, y=150)

e1=Entry(top, font=("Arial 20 bold"))
e1.place(x=300, y=150)

L3=Label(top, text="Password", bg="gray", fg="white", font=("Arial 20 bold"))
L3.place(x=150, y=200)

e2=Entry(top, font=("Arial 20 bold"), show="*")
e2.place(x=300, y=200)

b7=Button(top, text="Login", font=("Arial 20 bold"), command=login)
b7.place(x=885, y=550)

ch=Checkbutton(top, command=show)
ch.place(x=570, y=204)

top.mainloop()