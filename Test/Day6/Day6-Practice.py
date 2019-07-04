#!/usr/bin/env python 
# -*- coding:utf-8 -*-

class Restaurant():
    def __init__(self,name,type):
        self.name = name
        self.type = type
    def describe_restaurant(self):
        print("name:"+self.name+","+"type:"+self.type)
    def open_restaurant(self):
        print("open")

class IceCreamStand(Restaurant):
    def __init__(self,name,type):
        super().__init__(name,type)
        self.flavos = ['sweet','oduar']
    def fav_ice(self):
        for ice in self.flavos:
            print("I like " + ice)

ice_ = IceCreamStand('CoCo','ice')
ice_.open_restaurant()
ice_.describe_restaurant()
ice_.fav_ice()
