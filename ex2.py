from tkinter import *
from tkinter.ttk import *
top=Tk()

top.geometry('450x300')

user_name=Label(top, text="UserName").place(x=30,y=60)

user_password=Label(top, text="Password").place(x=30,y=100)

submit_button=Button(top, text="Submit").place(x=30,y=130)

user_name_input_area=Entry(top, width=30).place(x=110,y=60)
user_password_input_area=Entry(top, width=30).place(x=110,y=100)

top.mainloop()