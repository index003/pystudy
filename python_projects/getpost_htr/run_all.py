#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用discover'

__author__ = 'Victor Wu'

import unittest
from HTMLTestRunner import HTMLTestRunner
import os
import time
from run_htr import TestMethod

class RunAll(TestMethod):

    if __name__=="__main__":
        #定义测试用例的目录为当前目录
        test_dir = './'
        discover = unittest.defaultTestLoader.discover(test_dir,pattern = '*_htr.py')
        localpath = public_path = os.path.dirname(__file__)  # 当前执行文件的路径 推荐使用这种方式
        print('本文件目录位置：' + localpath)
        now = time.strftime("%Y-%m-%d %H-%M-%S")
        filename = os.path.join(localpath, 'report', now + '.html')
        print('报告存放路径  ：' + filename)

        with open(filename, 'wb') as wf:
            # 定义测试报告
            runner = HTMLTestRunner(
                stream=wf,
                title="discover get post HTMLTestRunner",
                description="description"
            )
            runner.run(discover)