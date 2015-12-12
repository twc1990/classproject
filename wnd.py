from tkinter import *
from tkinter.ttk import *
from gen import runGen as generate
from gen import setPass
from gen import cryptTest

def also(*fns):
    for fn in fns:
        if fn:
            fn()

def quit_and(w, *fns):
    also(*fns)
    w.destroy()

def dialog(string):
    wnd = Tk()
    frame = Frame(wnd)
    lbl = Label(frame, text=string)
    btn = Button(frame, text="Ok", command=lambda w=wnd: w.destroy())
    wnd.bind("<Return>", lambda e, b=btn: b.invoke())

    frame.grid(column=0, row=0, padx=6, pady=6)
    lbl.grid(column=0, row=0, padx=6, pady=6)
    btn.grid(column=0, row=1, padx=6, pady=6)
    
    wnd.mainloop()

def initial_password(submit):
    wnd = Tk()
    wnd.title("Initial Configuration")

    frame = Frame(wnd)

    pw = StringVar()

    lbl = Label (frame, text = "Please enter your password to encrypt/decrypt the passwords file.")
    inp = Entry (frame, textvariable = pw, show = "*")
    btn = Button(frame, text = "Confirm", default = "active", command = lambda w=wnd: quit_and(w, lambda: submit(pw.get())))

    frame.grid(column = 0, row = 0, padx=6, pady=6)

    lbl.grid(column = 1, row = 0, columnspan = 3, padx=6, pady=6)
    inp.grid(column = 1, row = 1, columnspan = 3, padx=6, pady=6)
    btn.grid(column = 2, row = 2, columnspan = 1, padx=6, pady=6)

    wnd.bind("<Return>", lambda e, b=btn: b.invoke())
    wnd.mainloop()

def view_pw(pwmap, key):
    if key == "":
        return

    wnd = Tk()
    wnd.title("Password")

    frame = Frame(wnd)

    pw = StringVar(value="123456")

    label = Label(frame, text=key + ": ")
    box = Entry(frame)
    box.insert(index=0, string=pwmap[key])
    box.config(state="readonly")
    btn = Button(frame, text="Close", command=lambda w=wnd: quit_and(w))

    frame.grid(column=0, row=0, padx=6, pady=6)
    label.grid(column=0, row=0, columnspan=1, padx=6, pady=6)
    box.grid(column=1, row=0, columnspan=1, padx=6, pady=6)
    btn.grid(column=0, row=1, columnspan=2, padx=6, pady=6)

    wnd.mainloop()

def edit_pw(pwmap, modify, key):
    if key == "":
        return

    wnd = Tk()
    wnd.title("Edit " + key + " Password")

    frame = Frame(wnd)
    edit = Entry(frame)
    edit.insert(index=0, string=pwmap[key])
    done = Button(frame, text="Confirm", command=lambda w=wnd, k=key, p=edit: quit_and(w, lambda: pwmap.update({k: p.get()}), lambda: modify(pwmap)))

    frame.grid(column=0, row=0, padx=6, pady=6)
    edit.grid(column=0, row=0, columnspan=2, padx=6, pady=6)
    done.grid(column=0, row=1, columnspan=2, padx=6, pady=6)

    wnd.mainloop()

def add_pw(pwmap, modify):
    wnd = Tk()
    wnd.title("Add Password")

    frame = Frame(wnd)

    newkey = StringVar()
    newpw = StringVar()

    keylbl = Label(frame, text="Name: ")
    pwlbl = Label(frame, text="Password: ")
    sizelbl = Label(frame, text="Password Size: ")
    
    pattern = Combobox(frame)
    pattern['values'] = ["Alphanumeric", "Restricted Special", "All Characters"]
    pattern.set("Alphanumeric")

    sizeBox = Combobox(frame)
    sizeBox['values'] = list(range(8, 26))
    sizeBox.set(15)
    
    editkey = Entry(frame)
    editpw = Entry(frame)
    gen = Button(frame, text="Generate", command=lambda: also(lambda: editpw.delete(0,END), lambda: editpw.insert(index=END, string=generate(int(sizeBox.get()),pattern.get(), 0))))
    done = Button(frame, text="Confirm", command=lambda w=wnd, k=editkey, p=editpw: quit_and(w, lambda: pwmap.update({k.get(): p.get()}), lambda: modify(pwmap)))

    frame.grid(column=0, row=0, padx=6, pady=6)
    keylbl.grid(column=0, row=0, padx=6, pady=6)
    pwlbl.grid(column=0, row=1, padx=6, pady=6)
    editkey.grid(column=1, row=0, padx=6, pady=6)
    editpw.grid(column=1, row=1, padx=6, pady=6)
    pattern.grid(column=2, row=1, padx=6, pady=6)
    gen.grid(column=2, row=2, columnspan=2, padx=6, pady=6)
    done.grid(column=0, row=2, columnspan=2, padx=6, pady=6)
    sizelbl.grid(column=4, row=0, padx=6, pady=6)
    sizeBox.grid(column=4,row=1, padx=6, pady=6)
    wnd.mainloop()

def delete_pw(pwmap, modify, key):
    if key == "":
        return

    wnd = Tk()
    wnd.title("Warning")
    frame = Frame(wnd)
    lbl = Label(frame, text="Password data for " + key + " will be lost permanently.\nAre you sure you want to delete " + key + " password?")
    yes = Button(frame, text="Confirm", command=lambda w=wnd: quit_and(w, lambda: pwmap.pop(key), lambda: modify(pwmap)))
    no = Button(frame, text="Cancel", command=lambda w=wnd: quit_and(w))

    frame.grid(column=0, row=0, padx=6, pady=6)
    lbl.grid(column=0, row=0, columnspan=2, padx=6, pady=6)
    yes.grid(column=0, row=1, padx=6, pady=6)
    no.grid(column=1, row=1, padx=6, pady=6)

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

    for key in table.get(0, END):
        try:
            for k in passwords.keys():
                if key == k:
                    raise(DeepBreak)
            table.delete(table.curselection())
        except:
            pass

    window.after(250, lambda: main_update(window, table, passwords))
    
def checkPass(pwmap, pas, confir):
    if len(pas)>0:
        if pas==confir:
            setPass(pas)
            cryptTest(pwmap)
            return "Password Set"
        else:
            return "Password and Confirmation must match"
    else:
        return "Password cannot be empty"

def options_menu(pwmap, pwmodify, options):
    wnd=Tk()
    wnd.title("Options Menu")
    frame = Frame(wnd)
    newMaster=Label(frame, text="Change Master Password: ")
    confirmMaster=Label(frame, text="Confirm New Master Password: ")
    editpw = Entry(frame, show="*")
    confirmedpw = Entry(frame, show="*")
    done = Button(frame, text="Confirm", command = (lambda w=wnd, p=pwmap: also(lambda: dialog(checkPass(p, editpw.get(), confirmedpw.get())), lambda: w.destroy())))
    wnd.bind("<Return>", lambda e, b=done: b.invoke())
    
    frame.grid(column=0, row=0, padx=6, pady=6)
    newMaster.grid(column=1, row=1, padx=6, pady=6)
    confirmMaster.grid(column=1, row=2, padx=6, pady=6)
    editpw.grid(column=2, row=1, padx=6, pady=6)
    confirmedpw.grid(column=2, row=2, padx=6, pady=6)
    done.grid(column=2, row=3, padx=6, pady=6)
    
    wnd.mainloop()

def main_view(pwmap, pwmodify, options):
    wnd = Tk()
    wnd.title("Password Manager")

    frame = Frame(wnd)

    tbl = Listbox(frame)

    scl = Scrollbar(frame, orient=VERTICAL, command=tbl.yview)
    tbl.configure(yscrollcommand=scl.set)

    view = Button(frame, text="View", default="active", command=lambda: view_pw(pwmap, tbl.get(ACTIVE)))
    edit = Button(frame, text="Edit", command=lambda: edit_pw(pwmap, pwmodify, tbl.get(ACTIVE)))
    add  = Button(frame, text="Add", command=lambda: add_pw(pwmap, pwmodify))
    delete = Button(frame, text="Delete", command=lambda: delete_pw(pwmap, pwmodify, tbl.get(ACTIVE)))
    options = Button(frame, text="Options", command=lambda: options_menu(pwmap, pwmodify, options))

    frame.grid(column=0, row=0, padx=6, pady=6)
    
    tbl.grid(column=1, row=1, columnspan=3, rowspan=5, padx=6, pady=6)
    scl.grid(column=4, row=1, columnspan=1, rowspan=5, sticky=(N,S), padx=6, pady=6)

    view.grid(column=5, row=1, columnspan=1, rowspan=1, padx=6, pady=6)
    edit.grid(column=5, row=2, columnspan=1, rowspan=1, padx=6, pady=6)
    add.grid(column=5, row=3, columnspan=1, rowspan=1, padx=6, pady=6)
    delete.grid(column=5, row=4, columnspan=1, rowspan=1, padx=6, pady=6)
    options.grid(column=5, row=5, columnspan=1, rowspan=1, padx=6, pady=6)

    wnd.after(250, lambda: main_update(wnd, tbl, pwmap))
    wnd.mainloop()

def password_error(func):
    wnd = Tk()
    wnd.title("Error!")
    f = Frame(wnd)
    Label(f, text="You have entered an incorrect password.").grid(column=0, row=0, columnspan=2, padx=6, pady=6)
    b = Button(f, text="Retry", command=lambda w=wnd: also(lambda: w.destroy(), func)).grid(column=0, row=1, padx=6, pady=6)
    q = Button(f, text="Quit", command=lambda w=wnd: w.destroy()).grid(column=1, row=1, padx=6, pady=6)
    f.grid(column=0, row=0, padx=6, pady=6)
    wnd.mainloop()
