#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#使用文件的内容
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()#删除空格

print(pi_string)
print(len(pi_string))

#大型文件
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string[:52] + "...")
print(len(pi_string))

birthday = input('enter your birthday:')
if birthday in pi_string:
    print('yes')
else:
    print('no')


