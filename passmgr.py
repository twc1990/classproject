#!/bin/python

import gen
import wnd

while(True):
    wnd.initial_password(gen.setPass)
    passwords = gen.decrTest()
    if passwords:
        break
    wnd.password_error()

wnd.main_view(passwords, lambda key, pw: print("Database entry: " + key + " => " + pw), None)
