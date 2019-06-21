#!/usr/bin/env python 
# -*- coding:utf-8 -*-
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

def print_models(unprinted_designs, completed_models):
    """ 模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
  """
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # 模拟根据设计制作3D打印模型的过程
    print("Printing model: " + current_design)
    completed_models.append(current_design)
def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


magic_name = ["one","two","three"]
name = []

def make_grate():
    for names in magic_name:
        name.append(names +" great")

def show_magicians(num1):
    for name1 in name:
        print(name1)

make_grate()
show_magicians(name)
