from tkinter import *
from tkinter.ttk import *

def submit_button(wnd, fn, val):
    fn(val)
    wnd.destroy()

def initial_password(submit):
    wnd = Tk()
    wnd.title("Initial Configuration")

    frame = Frame(wnd)

    pw = StringVar()

    lbl = Label (frame, text = "Please input a master password. This can be changed later.")
    inp = Entry (frame, textvariable = pw, show = "*")
    btn = Button(frame, text = "Confirm", default = "active", command = lambda: submit_button(wnd, submit, pw.get()))

    frame.grid(column = 0, row = 0)

    lbl.grid(column = 1, row = 0, columnspan = 3)
    inp.grid(column = 1, row = 1, columnspan = 3)
    btn.grid(column = 2, row = 2, columnspan = 1)

    wnd.bind("<Return>", lambda e, b=btn: b.invoke())
    wnd.mainloop()

def main_view():
    pass
