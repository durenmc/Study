#!/usr/bin/env python 
# -*- coding:utf-8 -*-
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())#删除空行

file_path = 'E:/PycharmProject/Test/testfile.txt'
with open(file_path,'r', encoding='UTF-8') as file_object:
    contents = file_object.read()
    print(contents)