#!/usr/bin/env python 
# -*- coding:utf-8 -*-
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-2:])
for player in players[:3]:
    print(player)

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
print("\n-----------------------------------")

#lianxi
lianxi = ['charles', 'martina', 'michael', 'florence', 'eli']
print("The first three items in the list are:")
print(lianxi[:3])
print("Three items from the middle of the list are:")
print(lianxi[1:4])
print("The last three items in the list are:")
print(lianxi[-3:])

lianxi_copy = lianxi[:]
print(lianxi_copy)
lianxi.append("five")
lianxi_copy.append("six")
print("My favorite pizzasare:")
for value in lianxi:
    print(value)
print("My friend's favorite pizzasare:")
for value in lianxi_copy:
    print(value)

