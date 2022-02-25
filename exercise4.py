
from tkinter import *
import random

app = Tk() 


lFrame = Frame(app, bd=5)
rFrame = Frame(app, bd=5)
lFrame.pack(side='left',fill=BOTH, expand=1)
rFrame.pack(side='right',fill=BOTH, expand=1)



boxA = Label(lFrame, text="A", bg='blue', width=5)
boxB = Label(lFrame, text="B", bg='white', width=5)
boxC = Label(rFrame, text="C", bg='white', width=5)
boxD = Label(rFrame, text="D", bg='blue', width=5)


boxA.pack(side='top', fill=BOTH, expand=1)
boxB.pack(side='bottom', fill=BOTH, expand=1)
boxC.pack(side='top', fill=BOTH, expand=1)
boxD.pack(side='bottom', fill=BOTH, expand=1)


app.mainloop() 
