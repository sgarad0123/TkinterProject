# import everything from tkinter module
from tkinter import *
from tkinter.ttk import *
# create a tkinter window
root = Tk()

# Open window having dimension 100x100
root.geometry('100x100')

# Create a Button
btn = Button(root, text = 'Click me !',
						command = root.destroy)

# Set the position of button on the top of window.
btn.pack(side = 'top')

root.mainloop()
