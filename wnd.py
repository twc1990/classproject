from tkinter import *
from tkinter.ttk import *

def quit_and(w, *fns):
    for fn in fns:
        if fn:
            fn()
    w.destroy()

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
    btn = Button(frame, text = "Confirm", default = "active", command = lambda w=wnd: quit_and(w, lambda: submit(pw.get())))

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
    btn = Button(frame, text="Close", command=lambda w=wnd: quit_and(w))

    frame.grid(column=0, row=0)
    label.grid(column=0, row=0, columnspan=1)
    box.grid(column=1, row=0, columnspan=1)
    btn.grid(column=0, row=1, columnspan=2)

    wnd.mainloop()

def edit_pw(pwmap, modify, key):
    wnd = Tk()
    wnd.title("Edit " + key + " Password")

    frame = Frame(wnd)
    edit = Entry(frame)
    done = Button(frame, text="Confirm", command=lambda w=wnd, k=key, p=edit: quit_and(w, modify(k, p.get()), lambda: pwmap.update({k: p.get()}), lambda: print({k: p.get()})))

    frame.grid(column=0, row=0)
    edit.grid(column=0, row=0, columnspan=2)
    done.grid(column=0, row=1, columnspan=2)

    wnd.mainloop()

def add_pw(pwmap, modify, key):
    wnd = Tk()
    wnd.title("Add Password")

    frame = Frame(wnd)

    newkey = StringVar()
    newpw = StringVar()

    keylbl = Label(frame, text="Name: ")
    pwlbl = Label(frame, text="Password: ")

    editkey = Entry(frame)
    editpw = Entry(frame)
    gen = Button(frame, text="Generate")
    done = Button(frame, text="Confirm", command=lambda w=wnd, k=editkey, p=editpw: quit_and(w, modify(k.get(), p.get()), lambda: pwmap.update({k.get(): p.get()}), lambda: print({k.get(): p.get()})))

    frame.grid(column=0, row=0)
    keylbl.grid(column=0, row=0)
    pwlbl.grid(column=0, row=1)
    editkey.grid(column=1, row=0)
    editpw.grid(column=1, row=1)
    gen.grid(column=2, row=1)
    done.grid(column=0, row=2, columnspan=2)

    wnd.mainloop()

def delete_pw(pwmap, modify, key):
    wnd = Tk()
    wnd.title("Warning")
    frame = Frame(wnd)
    lbl = Label(frame, text="Password data for " + key + " will be lost permanently. Are you sure you want to delete " + key + " password?")
    yes = Button(frame, text="Confirm", command=lambda: quit_and(lambda: modify(key, ""), lambda: pwmap.pop(key)))
    no = Button(frame, text="Cancel", command=lambda: quit_and())

    frame.grid(column=0, row=0)
    lbl.grid(column=0, row=0, columnspan=2)
    yes.grid(column=0, row=1)
    no.grid(column=1, row=1)

    wnd.mainloop()

def main_update(window, table, passwords):
    for key in passwords.keys():
        try:
            for k in table.get(0, END):
                if key == k:
                    raise(DeepBreak)
            table.insert(END, key)
        except:
            pass

    window.after(250, lambda: main_update(window, table, passwords))

def main_view(pwmap, pwmodify, options):
    wnd = Tk()
    wnd.title("Password Manager")

    frame = Frame(wnd)

    tbl = Listbox(frame)

    scl = Scrollbar(frame, orient=VERTICAL, command=tbl.yview)
    tbl.configure(yscrollcommand=scl.set)

    view = Button(frame, text="View", default="active", command=lambda: view_pw(pwmap, tbl.get(tbl.curselection())))
    edit = Button(frame, text="Edit", command=lambda: edit_pw(pwmap, pwmodify, tbl.get(tbl.curselection())))
    add  = Button(frame, text="Add", command=lambda: add_pw(pwmap, pwmodify, tbl.get(tbl.curselection())))
    delete = Button(frame, text="Delete", command=lambda: delete_pw(pwmap, pwmodify, tbl.get(tbl.curselection())))
    options = Button(frame, text="Options", command=lambda: options_menu(options))

    frame.grid(column=0, row=0)
    
    tbl.grid(column=1, row=1, columnspan=3, rowspan=4)
    scl.grid(column=4, row=1, columnspan=1, rowspan=4, sticky=(N,S))

    view.grid(column=5, row=1, columnspan=1, rowspan=1)
    edit.grid(column=5, row=2, columnspan=1, rowspan=1)
    add.grid(column=5, row=3, columnspan=1, rowspan=1)
    delete.grid(column=5, row=4, columnspan=1, rowspan=1)
    options.grid(column=5, row=5, columnspan=1, rowspan=1)

    wnd.after(250, lambda: main_update(wnd, tbl, pwmap))
    wnd.mainloop()

#initial_password(lambda x: print(str(x)))
main_view({"test":"test", "asdf":"jkl;", "qwerty":"uiop"}, lambda x,y: print(y + ": " + x[y]), lambda x: print("Options!"))
