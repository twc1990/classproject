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

def view_pw(pwmap, key):
    wnd = Tk()
    wnd.title("Password")

    frame = Frame(wnd)

    pw = StringVar(value="123456")

    label = Label(frame, text=key + ": ")
    box = Label(frame, text=pwmap[key])
    btn = Button(frame, text="Close", command=lambda w=wnd: w.destroy())

    frame.grid(column=0, row=0)
    label.grid(column=0, row=0, columnspan=1)
    box.grid(column=1, row=0, columnspan=1)
    btn.grid(column=0, row=1, columnspan=2)

    wnd.mainloop()

def edit_pw(pwmap, modify, key):
    modify(pwmap, key)

def add_pw(pwmap, modify, key):
    modify(pwmap, key)

def main_view(pwmap, pwmodify, options):
    wnd = Tk()
    wnd.title("Password Manager")

    frame = Frame(wnd)

    tbl = Listbox(frame)

    for key in pwmap.keys():
        tbl.insert(END, key)

    scl = Scrollbar(frame, orient=VERTICAL, command=tbl.yview)
    tbl.configure(yscrollcommand=scl.set)

    view = Button(frame, text="View", default="active", command=lambda: view_pw(pwmap, tbl.get(tbl.curselection())))
    edit = Button(frame, text="Edit", command=lambda: edit_pw(pwmap, pwmodify, tbl.get(tbl.curselection())))
    add  = Button(frame, text="Add", command=lambda: add_pw(pwmap, pwmodify, tbl.get(tbl.curselection())))
    options = Button(frame, text="Options", command=lambda: options_menu(options))

    frame.grid(column=0, row=0)
    
    tbl.grid(column=1, row=1, columnspan=3, rowspan=4)
    scl.grid(column=4, row=1, columnspan=1, rowspan=4, sticky=(N,S))

    view.grid(column=5, row=1, columnspan=1, rowspan=1)
    edit.grid(column=5, row=2, columnspan=1, rowspan=1)
    add.grid(column=5, row=3, columnspan=1, rowspan=1)
    options.grid(column=5, row=4, columnspan=1, rowspan=1)

    wnd.mainloop()

#initial_password(lambda x: print(str(x)))
main_view({"test":"test", "asdf":"jkl;", "qwerty":"uiop"}, lambda x,y: print(y + ": " + x[y]), lambda x: print("Options!"))
