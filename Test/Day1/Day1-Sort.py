#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#sort
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print("-------------------------------------------")
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
cars.reverse()
print(cars)
print(len(cars))

print("--------------------------------------------------------------------")
#练习
travel = ["thailand","tokyo","paris","london","shanghai"]
print(travel)
print(sorted(travel))
print(travel)
print(sorted(travel,reverse=True))
print(travel)

travel.reverse()
print(travel)

travel.reverse()
print(travel)

travel.sort()
print(travel)

travel.sort(reverse=True)
print(travel)





