#!/usr/bin/env python 
# -*- coding:utf-8 -*-
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])
names = ['zhangsan','lisi']
bicycles[0] = 'honck'
print(bicycles)
del bicycles[1]
print(bicycles)
poppes_bicycles =bicycles.pop()
print(bicycles)
print(poppes_bicycles)

print("------------------------------------------------------------------------")
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")
print(motorcycles)
print("------------------------------------------------------------------------")

#lianxi
invent = ['xiuxiu','miaomiao','nannan']
print(invent)
invent[0] = 'sansan'
print(invent)
invent.insert(0,'sisi')
invent.insert(2,'wuwu')
invent.append('liuliu')
print(invent)
in1=invent.pop()
in2=invent.pop()
in3=invent.pop()
in4=invent.pop()
print(invent)
print(in1+","+in2+","+in3+","+in4+" sorry ")
del invent[0]
del invent[0]
print(invent)




















