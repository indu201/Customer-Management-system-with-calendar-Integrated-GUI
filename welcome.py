from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import datetime
from tkinter import messagebox

top=Tk()
top.title('Welcome')
top.geometry("1300x650")

path="C:\\Users\\Aditya\\Pictures\\aditya.jpg"
img=ImageTk.PhotoImage(Image.open(path).resize((1400, 700)))

L12=Label(top, image=img)
L12.pack()

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



L=Label(top, text="Welcome", bg="firebrick", fg="white", font=("Arial 30 bold"))
L.place(x=600, y=30)

L1=Label(top, text="SearchCourse", bg="sea green", fg="white", font=("Arial 20 bold"))
L1.place(x=200, y=212)


b7=Button(top, text="TeacherADD", fg="White", bg="dark slate gray", font=("Arial 18 bold"))
b7.place(x=100, y=100)

b8=Button(top, text="StudentRegistration", fg="White", bg="dark slate gray", font=("Arial 18 bold"))
b8.place(x=300, y=100)

b9=Button(top, text="ShowCourse", fg="White", bg="dark slate gray", font=("Arial 18 bold"))
b9.place(x=590, y=100)

b10=Button(top, text="ADDCourse", fg="White", bg="dark slate gray", font=("Arial 18 bold"))
b10.place(x=800, y=100)

b11=Button(top, text="Exit", fg="White", bg="dark slate gray", font=("Arial 18 bold"))
b11.place(x=995, y=100)

top.mainloop()