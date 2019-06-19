#!/usr/bin/env python 
# -*- coding:utf-8 -*-
for value in range(1,5):
    print(value)
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(1,10,2))
print(even_numbers)

squares =[]
for value in range(1,11):
    squares.append(value**2)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in range(1,11)]
print(squares)
print("------------------------------------------------------------------")
#lianxi
for value in range(1,21):
    print(value)

million = list(range(1,1000001))
print(min(million))
print(max(million))

qishu = list(range(1,20,2))
for value in qishu:
    print(value)

san = list(range(3,30,3))
for value in san:
    print(value)

triple = [value**3 for value in range(1,11)]
print(triple)

