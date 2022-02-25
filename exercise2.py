from tkinter import *

app = Tk()

app.geometry('200x200')
app.title()

def clicked():
    if label['text'] == "Hi":
        label['text'] = "Bye"
    else:
        label['text'] = "Hi"

    if button['bg'] == 'red':
        button['bg'] = 'green'
    elif button['bg'] == 'green':
        button['bg'] = 'blue'
    elif button['bg'] == 'blue':
        button['bg'] = 'red'
    


button = Button(app,text ="Wave", command= clicked, bg ="red")

label = Label(app, text="Hi")

label.pack(side="bottom")
button.pack(side="bottom")


app.mainloop()