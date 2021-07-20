#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'文件操作小结'

__author__ = 'Victor Wu'

import time,os,sys
import unittest

# 路径操作1==current_path（推荐）

current_path = os.path.dirname(__file__)    # 当前执行文件的路径
print('current_path===>', current_path)

filenameC = './test.txt'

# 第二种方式，join方式，当前目录的文件
filepathC02 = os.path.join(current_path, filenameC) 

with open(filepathC02,'r', encoding = 'utf-8') as f:
    print('===filenameC02 start===')
    for line in f.readlines():
        print(line)
    print('===filenameC02 end===')

filenameD = '../testtemp/test.txt'

# 第四种方式，join方式，上层目录的文件
filepathC04 = os.path.join(current_path, filenameD) 

with open(filepathC04,'r', encoding = 'utf-8') as f:
    print('===filenameC04 start===')
    for line in f.readlines():
        print(line)
    print('===filenameC04 end===')

# 路径操作2==public_path（可以用）

public_path = os.path.dirname(os.path.abspath(sys.argv[0])) # 获取当前运行的.py文件所在的绝对路径
print('current_path===>', public_path)

filenameE = './test.txt'

# 第二种方式，join方式，当前目录的文件
filepathC06 = os.path.join(public_path, filenameE) 

with open(filepathC06,'r', encoding = 'utf-8') as f:
    print('===filenameC06 start===')
    for line in f.readlines():
        print(line)
    print('===filenameC06 end===')

filenameF = '../testtemp/test.txt'

# 第四种方式，join方式，上层目录的文件
filepathC08 = os.path.join(public_path, filenameF) 

with open(filepathC08,'r', encoding = 'utf-8') as f:
    print('===filenameC08 start===')
    for line in f.readlines():
        print(line)
    print('===filenameC08 end===')

