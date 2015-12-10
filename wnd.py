from tkinter import *
from tkinter.ttk import *

def initial_password(submit):
    wnd = Tk()
    wnd.title("Initial Configuration")

    frame = Frame(wnd)

    pw = StringVar()

    lbl = Label (frame, text = "Please input a master password. This can be changed later.")
    inp = Entry (frame, textvariable = pw, show = "*")
    btn = Button(frame, text = "Confirm", default = "active", command = lambda: submit(pw))

    frame.grid(column = 0, row = 0)

    lbl.grid(column = 1, row = 0, columnspan = 3)
    inp.grid(column = 1, row = 1, columnspan = 3)
    btn.grid(column = 2, row = 2, columnspan = 1)

initial_password(lambda x: x)
