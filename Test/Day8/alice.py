#!/usr/bin/env python 
# -*- coding:utf-8 -*-

filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    #pass 有异常什么也不显示
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)