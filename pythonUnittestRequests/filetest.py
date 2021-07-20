#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''

__author__ = 'Victor Wu'

import time,os,sys
import unittest


print(os.name)
print('=======',os.path.abspath('.'))
case_path = os.path.join(os.path.dirname(os.path.abspath('lottery-order.py')))
case_path2 = os.path.join(os.getcwd(), 'lottery-order.py')
print(case_path)
print(case_path2)
print(os.path.abspath('lottery-order.py'))
print(os.path.dirname(os.path.abspath('lottery-order.py')))
print(os.path.dirname((os.path.dirname(os.path.abspath('lottery-order.py')))))

sys.path.append('./Interface')    
test_dir = './Interface'     
print(test_dir)
public_path = os.path.dirname(os.path.abspath(sys.argv[0]))
print(public_path)
filename = public_path + "\\Report\\" + "report.html"  
print(filename)

with open('./test.txt','r') as f:
    for line in f.readlines():
        print(line)

