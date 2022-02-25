from distutils import command
from tkinter import *
app = Tk()

def clicked():
    print("Get Clicked")

button = Button(text ="Clicked", command= clicked)
button.pack(side="bottom")
app.geometry('200x200')
app.mainloop()