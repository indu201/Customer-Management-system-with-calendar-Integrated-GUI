from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import datetime
from tkinter import messagebox




top=Tk()
top.title('Welcome')
top.geometry("1300x650")
# top.title("welcome")

def back():
    top.destroy()
    import welcome

def exit():
    top.destroy()


def insert():
    k=e1.get()
    k2=e2.get()
    k3=e3.get()
    k4=e4.get()
    k5=e5.get()
    k6=e6.get()

    import pymysql as sql
    db=sql.connect(
        host="localhost",
        user="root",
        password="king123@#",
        db="student_db"
    )
    cur = db.cursor()
    s = "insert into course values('%s','%s','%s','%s','%s','%s')"%(k, k2, k3, k4, k5, k6)
    result = cur.execute(s)
    if(result>0):
        messagebox.showinfo("Result", "Your record insert successfully")

    else:
        messagebox.showinfo("Result", "Record not insert successfully")
    db.commit()    

    e1.delete(0, "end")
    e2.delete(0, "end")
    e3.delete(0, "end")
    e4.delete(0, "end")
    e5.delete(0, "end")
    e6.delete(0, "end")
    
var = StringVar()

path="C:\\Users\\Aditya\\Pictures\\aditya.jpg"
img=ImageTk.PhotoImage(Image.open(path).resize((1400, 700)))

L12=Label(top, image=img)
L12.pack()

L=Label(top, text="CourseADD", bg="tomato", fg="white", font=("Arial 30 bold"))
L.place(x=600, y=30)

L2=Label(top, text="CourseName", bg="dark slate gray", fg="white", font=("Arial 20 bold"))
L2.place(x=150, y=150)

e1=Entry(top, font=("Arial 20 bold"))
e1.place(x=350, y=150)

L3=Label(top, text="Duration", bg="dark slate gray", fg="white", font=("Arial 20 bold"))
L3.place(x=150, y=250)

e2=Entry(top, font=("Arial 20 bold"))
e2.place(x=350, y=250)

L4=Label(top, text="CourseFee", bg="dark slate gray", fg="white", font=("Arial 20 bold"))
L4.place(x=150, y=200)

e3=Entry(top, font=("Arial 20 bold"))
e3.place(x=350, y=200)

L5=Label(top, text="Teacher", bg="dark slate gray", fg="white", font=("Arial 20 bold"))
L5.place(x=150, y=300)

e4=Entry(top, font=("Arial 20 bold"))
e4.place(x=350, y=300)

L6=Label(top, text="Time", bg="dark slate gray", fg="white", font=("Arial 20 bold"))
L6.place(x=150, y=350)

e5=Entry(top, font=("Arial 20 bold"))
e5.place(x=350, y=350)

L7=Label(top, text="CourseMode", bg="dark slate gray", fg="white", font=("Arial 20 bold"))
L7.place(x=150, y=400)

e6=Entry(top, font=("Arial 20 bold"))
e6.place(x=350, y=400)


b=Button(top, text="Submit", font=("Arial 18 bold"), command=insert)
b.place(x=350, y=550)

b6=Button(top, text="Exit", font=("Arial 18 bold"), command=exit)
b6.place(x=480, y=550)

b7=Button(top, text="Back", font=("Arial 18 bold"), command=back)
b7.place(x=570, y=550)

top.mainloop()