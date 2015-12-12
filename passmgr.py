#!/bin/python

import gen
import wnd

def start():
    p = gen.MASTERPASS
    wnd.initial_password(gen.setPass)
    if p == gen.MASTERPASS:
        exit()
    passwords = gen.decrTest()
    if passwords is not None:
        wnd.main_view(passwords, gen.cryptTest, None)
    else:
        wnd.password_error(start)

start()
