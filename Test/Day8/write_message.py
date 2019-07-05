#!/usr/bin/env python 
# -*- coding:utf-8 -*-
filename = 'programming.txt'
#写入文件，覆盖原来的内容
with open(filename,'w') as file_object:
    file_object.write('I love peogramming.\n')
    file_object.write('I love creating new games.\n')

#附加不覆盖
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

#practice
while True:
    message = input('What do you like?')
    with open('practice.txt','a') as file_object:
        file_object.write(message)
    if message == '':
        break