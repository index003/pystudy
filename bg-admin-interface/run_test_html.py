#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""使用discover调用oop的get和post请求"""
__author__ = 'Victor Wu'

import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner


# 测试用例存放路径
case_path = './'
discover = unittest.defaultTestLoader.discover(case_path, pattern="test_*.py")
suite = unittest.TestSuite()
now = time.strftime("%Y-%m-%d %H-%M-%S")
filename = os.path.join('./', 'report', now + 'report.html')
print('==========', filename)
with open(filename, 'wb') as wf:
    # 定义测试报告
    runner = HTMLTestRunner(
        stream=wf,
        title="Admin interface test",
        description="测试admin后台的接口"
    )
    runner.run(discover)