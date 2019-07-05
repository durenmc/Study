#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#lianxi替换字符
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip().replace('3.14','8.88')
print(pi_string)
