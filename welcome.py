from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import datetime
from tkinter import messagebox

top=Tk()
top.title('Welcome')
top.geometry("1300x650")

def student():
    top.destroy()
    import student
def course():
    top.destroy()
    import Course
def teacher():
    top.destroy()
    import teacher  

def showteacher():
    tv = ttk.Treeview(top, height=20)
    tv["columns"]=("Name", "Lastname", "Contact", "Age", "DOB", "Qualification", "Gender", "City", "Subject", "Exp")
    tv.column("#0", width=0, stretch=NO)
    tv.column("Name", anchor=CENTER, width=120)
    tv.column("Lastname", anchor=CENTER, width=120)
    tv.column("Contact", anchor=CENTER, width=120)
    tv.column("Age", anchor=CENTER, width=120)
    tv.column("DOB", anchor=CENTER, width=120)
    tv.column("Qualification", anchor=CENTER, width=120)
    tv.column("Gender", anchor=CENTER, width=120)
    tv.column("City", anchor=CENTER, width=120)
    tv.column("Subject", anchor=CENTER, width=120)
    tv.column("Exp", anchor=CENTER, width=120)
    
    
    tv.heading("Name", text="Name", anchor=CENTER)
    tv.heading("Lastname", text="Lastname", anchor=CENTER)
    tv.heading("Contact", text="Contact", anchor=CENTER)
    tv.heading("Age", text="Age", anchor=CENTER)
    tv.heading("DOB", text="DOB", anchor=CENTER)
    tv.heading("Qualification", text="Qualification", anchor=CENTER)
    tv.heading("Gender", text="Gender", anchor=CENTER)
    tv.heading("City", text="City", anchor=CENTER)
    tv.heading("Subject", text="Subject", anchor=CENTER)
    tv.heading("Exp", text="Exp", anchor=CENTER)
    tv.place(x=80, y=250)

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
    s="select * from teacher"
    cur.execute(s)
    result=cur.fetchall()
    for col in result:
        name=col[0]
        lastname=col[1]
        contact=col[2]
        age=col[3]
        dob=col[4]
        qualification=col[5]
        gender=col[6]
        city=col[7]
        subject=col[8]
        exp=col[9]
        tv.insert("", "end", values=(name, lastname, contact, age, dob, qualification, gender, city, subject, exp))
 


    

def exit():
    top.destroy()  

def search():
    k=e1.get()
    tv = ttk.Treeview(top, height=20)
    tv["columns"]=("CourseName", "Fee", "Duration", "TeacherName", "Time", "CourseMode")
    tv.column("#0", width=0, stretch=NO)
    tv.column("CourseName", anchor=CENTER, width=150)
    tv.column("Fee", anchor=CENTER, width=150)
    tv.column("Duration", anchor=CENTER, width=150)
    tv.column("TeacherName", anchor=CENTER, width=150)
    tv.column("Time", anchor=CENTER, width=150)
    tv.column("CourseMode", anchor=CENTER, width=150)
    
    tv.heading("CourseName", text="CourseName", anchor=CENTER)
    tv.heading("Fee", text="Fee", anchor=CENTER)
    tv.heading("Duration", text="Duration", anchor=CENTER)
    tv.heading("TeacherName", text="TeacherName", anchor=CENTER)
    tv.heading("Time", text="Time", anchor=CENTER)
    tv.heading("CourseMode", text="CourseMode", anchor=CENTER)
    tv.place(x=200, y=250)

   
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
    s="select * from course where coursename = %s"
    cur.execute(s,k)
    result=cur.fetchall()
    if result:
        for col in result:
            coursename=col[0]
            coursefee=col[1]
            duration=col[2]
            teacher=col[3]
            time=col[4]
            coursemode=col[5]
            tv.insert("", "end", values=(coursename, coursefee, duration, teacher, time, coursemode))
    else:
        tv.place_forget()

    db.close()


    tv = ttk.Treeview(top, height=20)
    tv["columns"]=("Name", "Lastname", "Contact", "Age", "DOB", "Qualification", "Gender", "City", "Subject", "Exp")
    tv.column("#0", width=0, stretch=NO)
    tv.column("Name", anchor=CENTER, width=120)
    tv.column("Lastname", anchor=CENTER, width=120)
    tv.column("Contact", anchor=CENTER, width=120)
    tv.column("Age", anchor=CENTER, width=120)
    tv.column("DOB", anchor=CENTER, width=120)
    tv.column("Qualification", anchor=CENTER, width=120)
    tv.column("Gender", anchor=CENTER, width=120)
    tv.column("City", anchor=CENTER, width=120)
    tv.column("Subject", anchor=CENTER, width=120)
    tv.column("Exp", anchor=CENTER, width=120)
    
    
    tv.heading("Name", text="Name", anchor=CENTER)
    tv.heading("Lastname", text="Lastname", anchor=CENTER)
    tv.heading("Contact", text="Contact", anchor=CENTER)
    tv.heading("Age", text="Age", anchor=CENTER)
    tv.heading("DOB", text="DOB", anchor=CENTER)
    tv.heading("Qualification", text="Qualification", anchor=CENTER)
    tv.heading("Gender", text="Gender", anchor=CENTER)
    tv.heading("City", text="City", anchor=CENTER)
    tv.heading("Subject", text="Subject", anchor=CENTER)
    tv.heading("Exp", text="Exp", anchor=CENTER)
    tv.place(x=80, y=250)
    
    
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
    s="select * from teacher where name = %s"
    cur.execute(s,k)
    result=cur.fetchall()
    if result:
        for col in result:
            name=col[0]
            lastname=col[1]
            contact=col[2]
            age=col[3]
            dob=col[4]
            qualification=col[5]
            gender=col[6]
            city=col[7]
            subject=col[8]
            exp=col[9]
            tv.insert("", "end", values=(name, lastname, contact, age, dob, qualification, gender, city, subject, exp))
        
    else:
        tv.place_forget()
    db.close()    


    
def showcourse():
    tv = ttk.Treeview(top, height=20)
    tv["columns"]=("CourseName", "Fee", "Duration", "TeacherName", "Time", "CourseMode")
    tv.column("#0", width=0, stretch=NO)
    tv.column("CourseName", anchor=CENTER, width=200)
    tv.column("Fee", anchor=CENTER, width=200)
    tv.column("Duration", anchor=CENTER, width=200)
    tv.column("TeacherName", anchor=CENTER, width=200)
    tv.column("Time", anchor=CENTER, width=200)
    tv.column("CourseMode", anchor=CENTER, width=200)
    
    tv.heading("CourseName", text="CourseName", anchor=CENTER)
    tv.heading("Fee", text="Fee", anchor=CENTER)
    tv.heading("Duration", text="Duration", anchor=CENTER)
    tv.heading("TeacherName", text="TeacherName", anchor=CENTER)
    tv.heading("Time", text="Time", anchor=CENTER)
    tv.heading("CourseMode", text="CourseMode", anchor=CENTER)
    tv.place(x=80, y=250)
    
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
    s="select * from course"
    cur.execute(s)
    result=cur.fetchall()
    for col in result:
        coursename=col[0]
        coursefee=col[1]
        duration=col[2]
        teacher=col[3]
        time=col[4]
        coursemode=col[5]
        tv.insert("", "end", values=(coursename, coursefee, duration, teacher, time, coursemode))
 
    
path="C:\\Users\\Aditya\\Pictures\\aditya.jpg"
img=ImageTk.PhotoImage(Image.open(path).resize((1400, 700)))

L12=Label(top, image=img)
L12.pack()


L=Label(top, text="Welcome", bg="firebrick", fg="white", font=("Arial 30 bold"))
L.place(x=600, y=30)

L1=Label(top, text="SearchCourse&Teacher", bg="sea green", fg="white", font=("Arial 20 bold"))
L1.place(x=200, y=212)

e1=Entry(top, font=("Arial 20 bold"), width=10)
e1.place(x=520, y=212)

b6=Button(top, text="Search", fg="White", bg="dark slate gray", font=("Arial 18 bold"), command=search)
b6.place(x=670, y=200)

b7=Button(top, text="TeacherADD", fg="White", bg="dark slate gray", font=("Arial 18 bold"), command=teacher)
b7.place(x=100, y=100)

b8=Button(top, text="StudentRegistration", fg="White", bg="dark slate gray", font=("Arial 18 bold"), command=student)
b8.place(x=280, y=100)

b10=Button(top, text="ADDCourse", fg="White", bg="dark slate gray", font=("Arial 18 bold"), command=course)
b10.place(x=550, y=100)

b9=Button(top, text="ShowCourse", fg="White", bg="dark slate gray", font=("Arial 18 bold"), command=showcourse)
b9.place(x=720, y=100)

b12=Button(top, text="TeacherShow", fg="White", bg="dark slate gray", font=("Arial 18 bold"), command=showteacher)
b12.place(x=905, y=100)

b11=Button(top, text="Exit", fg="White", bg="dark slate gray", font=("Arial 18 bold"), command=exit)
b11.place(x=1100 , y=100)

top.mainloop()