from tkinter import *
from turtle import clear

app = Tk()

app.geometry('200x200')
app.title()

def clicked():
    t = e.get()
    if len(e.get()) == 0: 
        button['bg'] = 'red'
    else:
        label['text']= e.get()
        button['text'] = 'Clear Text' # ... and text
        button['command'] = clear
def clear():
    e.set(" ")
    button['text'] = 'Copy Text'
    button['command'] = clicked
    
e = StringVar()
entry = Entry(app, textvariable= e)

button = Button(app,text ="Copy Text", command= clicked)

label = Label(app, text= "text will appear here")

button.pack(side="bottom")
entry.pack(side="bottom")
label.pack(side="bottom")

app.mainloop()