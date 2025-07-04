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
    k1=int(e.get())
    k=e1.get()
    k2=e2.get()
    k3=int(e3.get())
    k4=int(e4.get())
    format = '%m/%d/%y'
    k5 = cal.get()
    date = datetime.datetime.strptime(k5, format)
    n = date.strftime('%y-%m-%d')
    k6 = c2.get()
    k7 = var.get()
    k8 = c.get()
    k9 = c3.get()
    k10 = int(e10.get())

    import pymysql as sql
    db=sql.connect(
        host="localhost",
        user="root",
        password="king123@#",
        db="student_db"
    )
    cur = db.cursor()
    s = "insert into students values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(k1, k, k2, k3, k4, n, k6, k7, k8, k9, k10)
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
    
var = StringVar()

path="C:\\Users\\Aditya\\Pictures\\aditya.jpg"
img=ImageTk.PhotoImage(Image.open(path).resize((1400, 700)))

L12=Label(top, image=img)
L12.pack()

L=Label(top, text="StudentRegistration", bg="tomato", fg="white", font=("Arial 30 bold"))
L.place(x=600, y=30)

L1=Label(top, text="RegID", bg="gray", fg="white", font=("Arial 20 bold"))
L1.place(x=150, y=100)

e=Entry(top, font=("Arial 20 bold"))
e.place(x=300, y=100)

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

L7=Label(top, text="Qualification", bg="gray", fg="white", font=("Arial 20 bold"))
L7.place(x=150, y=400)

k=["Select", "BA", "BTech", "MTech", "Bsc", "Msc"]

c2=ttk.Combobox(top, value=k, font=("Arial 19 bold"))
c2.place(x=300, y=400)
c2.current(0)

L8=Label(top, text="Gender", bg="gray", fg="white", font=("Arial 20 bold"))
L8.place(x=150, y=450)

L9=Label(top, text="City", bg="gray", fg="white", font=("Arial 20 bold"))
L9.place(x=150, y=500)

k=["Select City", "Meerut", "Jaipur", "Delhi", "Noida", "Kanpur"]

c=ttk.Combobox(top, value=k, font=("Arial 19 bold"))
c.place(x=300, y=500)
c.current(0)

L10=Label(top, text="Course", bg="gray", fg="white", font=("Arial 20 bold"))
L10.place(x=150, y=550)

k=["Select", "ML", "Data Structure", "Tableu", "Python", "Excel"]

c3=ttk.Combobox(top, value=k, font=("Arial 19 bold"))
c3.place(x=300, y=550)
c3.current(0)

L11=Label(top, text="Fees", bg="gray", fg="white", font=("Arial 20 bold"))
L11.place(x=150, y=600)

e10=Entry(top, font=("Arial 20 bold"))
e10.place(x=300, y=600)

r=Radiobutton(top, text="Male", value="Male", variable=var, font=("Arial 15 bold"))
r.place(x=300, y=450)

r2=Radiobutton(top, text="FeMale", value="FeMale", variable=var, font=("Arial 15 bold"))
r2.place(x=390, y=450)

r3=Radiobutton(top, text="Other", value="OTHER", variable=var, font=("Arial 15 bold"))
r3.place(x=500, y=450)

r.select()

b=Button(top, text="Submit", font=("Arial 18 bold"), command=insert)
b.place(x=300, y=650)

b6=Button(top, text="Exit", font=("Arial 18 bold"), command=exit)
b6.place(x=450, y=650)

b7=Button(top, text="Back", font=("Arial 18 bold"), command=back)
b7.place(x=560, y=650)

top.mainloop()