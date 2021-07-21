#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用unittest调用oop的get和post请求'

__author__ = 'Victor Wu'

import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import os
import sys


class TestMethod(unittest.TestCase):

    if __name__=='__main__':

        sys.path.append('./test_case')    
        test_dir = './test_case'       #指定当前文件夹下的Interface目录
        file = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')    #匹配开头为test的py文件
        now = time.strftime("%Y-%m-%d %H-%M-%S")
        public_path = os.path.dirname(__file__)  # 当前执行文件的路径 推荐使用这种方式
        reportpath = '../report' + now + 'report.html'
        filename = os.path.join(public_path,reportpath)
        print(filename)

        with open(filename, 'wb') as wf:
            # 定义测试报告
            runner = HTMLTestRunner(
                stream=wf,
                title="get post HTMLTestRunner",
                description="description"
            )
            runner.run(file)
