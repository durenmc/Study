#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import json

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)