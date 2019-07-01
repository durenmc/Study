#!/usr/bin/env python 
# -*- coding:utf-8 -*-
class Restaurant():
    def __init__(self,name,type,num):
        self.name = name
        self.type = type
        self.num = 0
    def set_num(self,a_num):
        self.num = a_num
    def ins_num(self,b_num):
        self.num += b_num

res=Restaurant('asd','234',100)
res.set_num(888)
res.ins_num(1000)
print(res.num)



