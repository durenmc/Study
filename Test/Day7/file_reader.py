#!/usr/bin/env python 
# -*- coding:utf-8 -*-
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())#删除空行

file_path = 'E:/PycharmProject/Test/testfile.txt'
with open(file_path,'r', encoding='UTF-8') as file_object:
    contents = file_object.read()
    print(contents)

#逐行读取
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

#创建一个包含文件各行的列表
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())