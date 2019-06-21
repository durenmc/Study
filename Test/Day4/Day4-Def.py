#!/usr/bin/env python 
# -*- coding:utf-8 -*-

def dispaly_meaasge(username):
    """this is def"""
    print("hoho"+ username.title())

dispaly_meaasge("asd")

def make_shirt(size,style="I love python"):
    print("The shirt's size is "+ size)
    print("The shirt's style is "+ style)

make_shirt("XL")
make_shirt("xxl")
make_shirt("s")

def city_country(city,country):
    message = city.title()+" "+country.title()
    return message

print(city_country("shanghai","china"))


def muscian(name,work,count=""):
    if count:
        muscle = {"name" : name,"work":work,"count":count}
    else:
        muscle = {"name": name, "work": work}
    return muscle



while True:
   print("input 'q' break")
   names =  input("name:")
   works = input("work:")
   if names == "q" or works == "q":
       break
   print(muscian(names,works))