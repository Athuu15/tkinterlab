from tkinter import *

app = Tk()

app.geometry('500x500')  


w = Canvas(app, bg='white') 
w.pack(expand = 2, fill = BOTH)


shape = "s"
def sKey(event):
    global shape
    print("squares")
    shape = "s"
    
def cKey(event):
    global shape
    print("circles")
    shape = "c"


app.bind("<KeyPress-s>", sKey)
app.bind("<KeyPress-c>", cKey)


fillColor = None
color = "yellow"

def fKey(event):
    global fillColor
    print("Now drawing transparent shapes")
    fillColor = None

def FKey(event):
    global fillColor
    print("Now drawing filled shapes")
    fillColor = color

def changeColor(col):
    global fillColor, color
    print("Now drawing in", col)
    color = col
    if fillColor != None:
        fillColor = color

def rKey(event):
    changeColor("red")
    
def yKey(event):
    changeColor("yellow")

app.bind("<KeyPress-f>", fKey)
app.bind("<KeyPress-F>", FKey)
app.bind("<KeyPress-r>", rKey)
app.bind("<KeyPress-y>", yKey)


X = 40
Y = 40
def mouseClick(event):
    mx = event.x
    my = event.y
    if shape == "s":
        w.create_rectangle(mx, my, mx+X, my+Y, \
            width=5, outline=color, fill=fillColor)
    else:
        w.create_oval(mx, my, mx+X, my+Y, width=5, \
            outline=color, fill=fillColor)
    

w.bind("<Button-1>", mouseClick)


app.mainloop()
