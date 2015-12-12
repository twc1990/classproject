#!/bin/python

import gen
import wnd

def start():
    p = gen.MASTERPASS
    wnd.initial_password(gen.setPass)
    if p == gen.MASTERPASS:
        exit()
    passwords = gen.decrTest()
    if passwords:
        wnd.main_view(passwords, lambda key, pw: print("Database entry: " + key + " => " + pw), None)
    else:
        wnd.password_error(start)

start()
