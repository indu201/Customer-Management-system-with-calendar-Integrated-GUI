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

def Login():
    top.destroy()
    import LOG

def exit():
    top.destroy()

def show():
    if e7.cget("show")=="*":
        e7.config(show="")
    else:
        e7.config(show="*")

def show2():
    for i in tv.get_children():
        tv.delete(i)

    import pymysql as sql
    db=sql.connect(
        host="localhost",
        user="root",
        password="king123@#",
        db="student_db"
    )
    cur=db.cursor()
    s="select * from customer"
    cur.execute(s)
    result=cur.fetchall()
    for col in result:
        name=col[0]
        lastname=col[1]
        contact=col[2]
        age=col[3]
        Dob=col[4]
        password=col[5]
        gender=col[6]
        city=col[7]
        tv.insert("", "end", values=(name, lastname, contact, age, Dob, password, gender, city))


def search():
    k=e1.get()
    for i in tv.get_children():
        tv.delete(i)

    import pymysql as sql
    db=sql.connect(
        host="localhost",
        user="root",
        password="king123@#",
        db="student_db"
    )
    cur=db.cursor()
    s="select * from customer where name = %s"
    cur.execute(s,k)
    result=cur.fetchall()
    for col in result:
        name=col[0]
        lastname=col[1]
        contact=col[2]
        age=col[3]
        Dob=col[4]
        password=col[5]
        gender=col[6]
        city=col[7]
        tv.insert("", "end", values=(name, lastname, contact, age, Dob, password, gender, city))


def update():
    k=e1.get()
    k2=e2.get()
    k3=int(e3.get())
    k4=int(e4.get())
    format = '%m/%d/%y'
    k5 = cal.get()
    date = datetime.datetime.strptime(k5, format)
    n = date.strftime('%y-%m-%d')
    k6 = e7.get()
    k7 = var.get()
    k8 = c.get()

    import pymysql as sql
    db=sql.connect(
        host="localhost",
        user="root",
        password="king123@#",
        db="student_db"
    )
    cur = db.cursor()
    if e2.get()=="" or int(e3.get())=="" or int(e4.get())=="" or date.strftime("%y-%m-%d")=="" or e7.get()=="" or var.get()=="" or c.get()=="" :
        messagebox.showinfo("Result", "Please update all records")
    else:
        t=(k2, k3, k4, n, k6, k7, k8, k)
        s="update customer set lastname=%s, contact=%s, age=%s, dob=%s, password=%s, gender=%s, city=%s where name=%s"
        result=cur.execute(s,t)
        if(result>0):
            messagebox.showinfo("Result", "Record update successfully")
        else:
            messagebox.showinfo("Result", "Record not updated")
        db.commit()             

def delete():
    k=e1.get()
    import pymysql as sql
    db=sql.connect(
        host="localhost",
        user="root",
        password="king123@#",
        db="student_db"
    )
    cur=db.cursor()
    s="delete from customer where name=%s"
    result=cur.execute(s,k)
    if(result>0):
        messagebox.showinfo("Result", "Your Delete successfully")
    else:
        messagebox.showinfo("Result", "Record not found")  
    db.commit()   


def insert():
    k=e1.get()
    k2=e2.get()
    k3=int(e3.get())
    k4=int(e4.get())
    format = '%m/%d/%y'
    k5 = cal.get()
    date = datetime.datetime.strptime(k5, format)
    n = date.strftime('%y-%m-%d')
    k6 = e7.get()
    k7 = var.get()
    k8 = c.get()

    import pymysql as sql
    db=sql.connect(
        host="localhost",
        user="root",
        password="king123@#",
        db="student_db"
    )
    cur = db.cursor()
    s = "insert into customer values('%s','%s','%s','%s','%s','%s','%s','%s')"%(k, k2, k3, k4, n, k6, k7, k8)
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
    e7.delete(0, "end")
    
var = StringVar()

path="C:\\Users\\Aditya\\Pictures\\aditya.jpg"
img=ImageTk.PhotoImage(Image.open(path).resize((1400, 700)))

L12=Label(top, image=img)
L12.pack()

tv = ttk.Treeview(top)
tv["columns"]=("Name", "Lastname", "Contact", "Age", "DOB", "Password", "Gender", "City")
tv.column("#0", width=0, stretch=NO)
tv.column("Name", anchor=CENTER, width=90)
tv.column("Lastname", anchor=CENTER, width=90)
tv.column("Contact", anchor=CENTER, width=90)
tv.column("Age", anchor=CENTER, width=90)
tv.column("DOB", anchor=CENTER, width=90)
tv.column("Password", anchor=CENTER, width=90)
tv.column("Gender", anchor=CENTER, width=90)
tv.column("City", anchor=CENTER, width=90)

tv.heading("Name", text="Name", anchor=CENTER)
tv.heading("Lastname", text="Lastname", anchor=CENTER)
tv.heading("Contact", text="Contact", anchor=CENTER)
tv.heading("Age", text="Age", anchor=CENTER)
tv.heading("DOB", text="DOB", anchor=CENTER)
tv.heading("Password", text="Password", anchor=CENTER)
tv.heading("Gender", text="Gender", anchor=CENTER)
tv.heading("City", text="City", anchor=CENTER)
tv.place(x=620, y=150)


L=Label(top, text="Registration", bg="salmon", fg="white", font=("Arial 30 bold"))
L.place(x=600, y=30)

L2=Label(top, text="Name", bg="gray", fg="white", font=("Arial 20 bold"))
L2.place(x=150, y=150)

e1=Entry(top, font=("Arial 20 bold"))
e1.place(x=300, y=150)

L3=Label(top, text="Lastname", bg="gray", fg="white", font=("Arial 20 bold"))
L3.place(x=150, y=200)

e2=Entry(top, font=("Arial 20 bold"))
e2.place(x=300, y=200)

L4=Label(top, text="Contact", bg="gray", fg="white", font=("Arial 20 bold"))
L4.place(x=150, y=250)

e3=Entry(top, font=("Arial 20 bold"))
e3.place(x=300, y=250)

L5=Label(top, text="Age", bg="gray", fg="white", font=("Arial 20 bold"))
L5.place(x=150, y=300)

e4=Entry(top, font=("Arial 20 bold"))
e4.place(x=300, y=300)

L6=Label(top, text="DOB", bg="gray", fg="white", font=("Arial 20 bold"))
L6.place(x=150, y=350)

cal = DateEntry(top, width=18, bg="gray", fg="white", font=("Arial 20 bold"), year=2020)
cal.place(x=300, y=350)

L7=Label(top, text="Password", bg="gray", fg="white", font=("Arial 20 bold"))
L7.place(x=150, y=400)

e7=Entry(top, font=("Arial 20 bold"), show="*")
e7.place(x=300, y=400)

L8=Label(top, text="Gender", bg="gray", fg="white", font=("Arial 20 bold"))
L8.place(x=150, y=450)

L9=Label(top, text="City", bg="gray", fg="white", font=("Arial 20 bold"))
L9.place(x=150, y=500)

k=["Select City", "Meerut", "Jaipur", "Delhi", "Noida", "Kanpur"]

c=ttk.Combobox(top, value=k, font=("Arial 19 bold"))
c.place(x=300, y=500)
c.current(0)

r=Radiobutton(top, text="Male", value="Male", variable=var, font=("Arial 15 bold"))
r.place(x=300, y=450)

r2=Radiobutton(top, text="FeMale", value="FeMale", variable=var, font=("Arial 15 bold"))
r2.place(x=390, y=450)

r3=Radiobutton(top, text="Other", value="OTHER", variable=var, font=("Arial 15 bold"))
r3.place(x=500, y=450)

r.select()

b=Button(top, text="Submit", font=("Arial 18 bold"), command=insert)
b.place(x=300, y=550)

b2=Button(top, text="Delete", font=("Arial 18 bold"), command=delete)
b2.place(x=420, y=550)

b3=Button(top, text="Show", font=("Arial 18 bold"), command=show2)
b3.place(x=530, y=550)

b4=Button(top, text="Search", font=("Arial 18 bold"), command=search)
b4.place(x=640, y=550)

b5=Button(top, text="Update", font=("Arial 18 bold"), command=update)
b5.place(x=760, y=550)

b6=Button(top, text="Exit", font=("Arial 18 bold"), command=exit)
b6.place(x=885, y=550)

b7=Button(top, text="Login", font=("Arial 18 bold"), command=Login)
b7.place(x=885, y=550)


ch=Checkbutton(top, command=show)
ch.place(x=570, y=400)

top.mainloop()