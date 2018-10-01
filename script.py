from tkinter import *

window = Tk() #creates a window

b1 = Button(window, text="run",bg="red",fg="blue") #creates a button
b1.grid(row=0,column=0) # places the button on the window

e1 = Entry(window) #creates an entry form
e1.grid(row=0,column=1) # places the entry space on the window

t1 = Text(window,height=1,width=20) #creates an text area of specified height and width.
t1.grid(row=0,column=2) # places the text area on the window

window.mainloop() #keeps the window open until user closes it, or else window will close soon.
