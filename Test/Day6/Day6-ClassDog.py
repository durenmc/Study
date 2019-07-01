#!/usr/bin/env python 
# -*- coding:utf-8 -*-
class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
    def sit(self):
        """"模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")

my_dog = Dog("whille",6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

#lianxi
class Restaurant():
    def __init__(self,name,type):
        self.name = name
        self.type = type
    def describe_restaurant(self):
        print("name:"+self.name+","+"type:"+self.type)
    def open_restaurant(self):
        print("open")

prac = Restaurant("haha","aaa")
prac.describe_restaurant()
prac.open_restaurant()