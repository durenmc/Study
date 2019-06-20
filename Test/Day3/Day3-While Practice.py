#!/usr/bin/env python 
# -*- coding:utf-8 -*-
sandwich_orders = ["one","two","three"]
finished_sandwiches = []
while sandwich_orders:
    finished_sandwiche = sandwich_orders.pop()
    print("I made " + finished_sandwiche.title())
    finished_sandwiches.append(finished_sandwiche)
print(finished_sandwiches)


sandwich_orders = ["one","two","three","two","two","two"]
print("two nothing")
while "two" in sandwich_orders:
    sandwich_orders.remove("two")
print(sandwich_orders)

ans = []

while True:
    local = input("If you could visit one place in the world, where would you go?")
    ans.append(local)
    stop = input("yes/no?")
    if stop == "yes":
        break
print(ans)

