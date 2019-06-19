#!/usr/bin/env python 
# -*- coding:utf-8 -*-
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#dimensions[0]=250  TypeError: 'tuple' object does not support item assignment
for dimension in dimensions:
    print(dimension)
#重新赋值
dimensions = (400,100)
for dimension in dimensions:
    print(dimension)

#练习
foods = ("one","two","three","four","five")
#foods[0]="zero"
foods = ("one","two","three","six","seven")
for food in foods:
    print(food)
