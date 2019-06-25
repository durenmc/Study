#!/usr/bin/env python 
# -*- coding:utf-8 -*-
def make_pizza(*toppings):
    print('\nMaking a pizza need')
    for topping in toppings:
        print("- "+topping)
make_pizza('qqqqq')
make_pizza('aaa','bbb','ccc')

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    print(profile)
    for key ,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                                location='princeton',
                                field='physics')
print(user_profile)


#lianxi
def practice(*make):
    print("\nthese are:"+str(make))

practice('111')
practice('222','333')


print(build_profile('m','cc',age='80',weight='200',height='500'))

def make_car(baron,style,**any):
    car = {}
    car['baron'] = baron
    car['style'] = style
    for key,value in any.items():
        car[key] = value
        return car

print(make_car('subaru', 'outback', color='blue', towpackage=True))