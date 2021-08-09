#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""使用discover调用oop的get和post请求"""

__author__ = 'Victor Wu'

import os
import sys
import time
import unittest
from HTMLTestRunner import HTMLTestRunner


# 测试用例存放路径
case_path = './cases'
discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
suite = unittest.TestSuite()

now = time.strftime("%Y-%m-%d %H-%M-%S")
# public_path = os.path.dirname(os.path.abspath(sys.argv[0]))  # 获取当前运行的.py文件所在的绝对路径
# filename = os.path.join(public_path, 'report', now + 'report.html')
# print('==========', filename)

filename = os.path.join('./', 'report', now + 'report.html')

with open(filename, 'wb') as wf:
    # 定义测试报告
    runner = HTMLTestRunner(
    stream=wf,
    title="get post HTMLTestRunner",
    description="description"
    )
    runner.run(discover)
