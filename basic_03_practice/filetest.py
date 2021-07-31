#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''

__author__ = 'Victor Wu'

import time,os,sys
import unittest


print(os.name)

# 路径操作1==current_path

current_path = os.path.dirname(__file__)    # 当前执行文件的路径
print('current_path===>', current_path)

filenameC = './test.txt'

# 第一种方式，直接用加号，当前目录的文件
filepathC01 = current_path + filenameC
# with open(current_path + filenameC,'r', encoding = 'utf-8') as f:
with open(filepathC01,'r', encoding = 'utf-8') as f:
    print('===filenameC01 start===')
    for line in f.readlines():
        print(line)
    print('===filenameC01 end===')

    
# 第二种方式，join方式，当前目录的文件
filepathC02 = os.path.join(current_path, filenameC) 

with open(filepathC02,'r', encoding = 'utf-8') as f:
    print('===filenameC02 start===')
    for line in f.readlines():
        print(line)
    print('===filenameC02 end===')


filenameD = '../testtemp/test.txt'

# 第三种方式，直接用加号,上层目录的文件

# 这种方式不可行

# filepathC03 = current_path + filenameD
# with open(filepathC03,'r', encoding = 'utf-8') as f:
#     print('===filenameC03 start===')
#     for line in f.readlines():
#         print(line)
#     print('===filenameC03 end===')

    
# 第四种方式，join方式，上层目录的文件
filepathC04 = os.path.join(current_path, filenameD) 

with open(filepathC04,'r', encoding = 'utf-8') as f:
    print('===filenameC04 start===')
    for line in f.readlines():
        print(line)
    print('===filenameC04 end===')


# 路径操作2==public_path

public_path = os.path.dirname(os.path.abspath(sys.argv[0])) # 获取当前运行的.py文件所在的绝对路径
print('current_path===>', public_path)

filenameE = './test.txt'

# 第一种方式，直接用加号，当前目录的文件
filepathC05 = public_path + filenameE
# with open(current_path + filenameC,'r', encoding = 'utf-8') as f:
with open(filepathC05,'r', encoding = 'utf-8') as f:
    print('===filenameC05 start===')
    for line in f.readlines():
        print(line)
    print('===filenameC05 end===')

    
# 第二种方式，join方式，当前目录的文件
filepathC06 = os.path.join(public_path, filenameE) 

with open(filepathC06,'r', encoding = 'utf-8') as f:
    print('===filenameC06 start===')
    for line in f.readlines():
        print(line)
    print('===filenameC06 end===')


filenameF = '../testtemp/test.txt'

# 第三种方式，直接用加号,上层目录的文件,这种方式不可行
# filepathC07 = public_path + filenameF
# with open(filepathC07,'r', encoding = 'utf-8') as f:
#     print('===filenameC07 start===')
#     for line in f.readlines():
#         print(line)
#     print('===filenameC07 end===')

    
# 第四种方式，join方式，上层目录的文件
filepathC08 = os.path.join(public_path, filenameF) 

with open(filepathC08,'r', encoding = 'utf-8') as f:
    print('===filenameC08 start===')
    for line in f.readlines():
        print(line)
    print('===filenameC08 end===')
