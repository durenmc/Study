#!/usr/bin/env python 
# -*- coding:utf-8 -*-
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print('\n')

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# 向右移动外星人
# 据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
# 这个外星人的速度一定很快
    x_increment = 3
# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))
print('\n')

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

print('\n')
#lianxi
person = {'first_name':'zhang','last_name':'san','age':20,'city':'shanghai'}
print(person)

for key,value in person.items():
    print("\nKey:"+key)
    print("Value:"+str(value))

print('\n')

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for name,language in favorite_languages.items():
    print(name.title()+ "'s favorite language is " +
    language.title() + ".")

for name in favorite_languages.keys():
    print(name)
print("\n")

friends = ['phil', 'sarah']
for name in favorite_languages:
    print(name.title())
    if name in friends:
        print(name.title()+" is "+favorite_languages[name])
print("\n")

for name in sorted(favorite_languages):
    print(name.title())
print("\n")
