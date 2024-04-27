from tkinter import *
# from tkinter.ttk import *
top=Tk()

top.geometry('450x300')

v=StringVar(top, "1")

# style = Style(top)
# style.configure("TRadiobutton", background = "light green",
#                 foreground = "red", font = ("arial", 10, "bold"))

values={
    "RadioButton 1" : "1",
    "RadioButton 2": "2",
    "RadioButton 3": "3",
    "RadioButton 4": "4",
    "RadioButton 5": "5"
}

for(text, value) in values.items():
    Radiobutton(top, text=text, variable=v, value=value,indicatoron=0, background="light blue").pack(fill=X,ipady=5)

top.mainloop()