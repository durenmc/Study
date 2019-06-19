#!/usr/bin/env python 
# -*- coding:utf-8 -*-
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

#lianxi
car = "One"
print(car=="one")
print(car=="One")
print(car=="two")
print(car.lower()=="one")
print("\n____________________-------")
names=["admin","one","two","three","four"]
for name in names:
    if name == "":
        print("null")
    elif name == "admin":
        print("this is special")
    else:
        print("Hello " + name +" haha")
print("\n")
current_users = ["one","two","three","fouR","five"]
new_users =  ["Four","Five","six","seven","eight"]
for new_user in new_users:
    if new_user.lower() in [current_user.lower() for current_user in current_users]:
        print(new_user+" exsit,input other")
    else:
        print(new_user+" ok")

print("\n")
numbers = range(1,10)
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number)+"th")





