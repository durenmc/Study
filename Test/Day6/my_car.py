#!/usr/bin/env python 
# -*- coding:utf-8 -*-

'''
from Day6.Car import Car                 导入类
from Day6.Car import Car,ElectricCar     导入两个类

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
'''

#导入一整个模块
import Day6.Car
from Day6.electric_car import ElectricCar

my_beetle = Day6.Car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#导入所有类
from Day6.Car import *