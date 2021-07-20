#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''

__author__ = 'Victor Wu'

import time,os,sys
import unittest


print(os.name)

public_path = os.path.dirname(os.path.abspath(sys.argv[0]))
print('public_path ===>', public_path)

filename = public_path + "\\Report\\" + "report.html"  
print('filename ===>', filename)

current_path = os.path.dirname(__file__)    # 当前执行文件的路径
print('current_path===>', current_path)

with open(current_path + './test.txt','r', encoding = 'utf-8') as f:
    for line in f.readlines():
        print(line)

