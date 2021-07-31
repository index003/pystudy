#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""使用HTMLTestRunner调用oop的get和post请求，并且生成报告"""

__author__ = 'Victor Wu'

import unittest
from getpost_htmltestrunner_demo import RunMain
from HTMLTestRunner import HTMLTestRunner
import time
import os
import sys


class TestMethod(unittest.TestCase):

    def setUp(self):
        self.run = RunMain()

    def test_001_get(self):
        baseurl = 'http://httpbin.org/get'
        datalist = {
            'name': 'zhangsan',
            'age': '25'
        }
        res = self.run.run_main(baseurl, 'GET', datalist)
        print(res)
        self.assertEqual(res['args']['age'], '25', 'Passed')
        # globals()['userid'] = '1000023'

    # @unittest.skip('test_002_post')   # 当前用例不执行
    def test_002_post(self):
        # print(self.userid)
        baseurl = 'http://httpbin.org/post'
        datalist = {
            'name': 'zhangsan',
            'age': '25'
        }
        res = self.run.run_main(baseurl, 'POST', datalist)
        print(res)
        self.assertEqual(res['form']['age'], '25', 'Failed')


if __name__ == '__main__':
    # unittest.main()   # 全部执行，下面的方式可以自己组织
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_001_get'))
    suite.addTest(TestMethod('test_002_post'))

    now = time.strftime("%Y-%m-%d %H-%M-%S")

    # public_path = os.getcwd()
    # print('本文件目录位置：' + public_path)
    # filename = os.path.join(public_path, 'report', now + '.html')
    # print('报告存放路径  ：' + public_path)

    # public_path = public_path = os.path.dirname(__file__)  # 当前执行文件的路径 推荐使用这种方式
    # print('本文件目录位置：' + public_path)
    # filename = os.path.join(public_path, 'report', now + '.html')
    # print('报告存放路径  ：' + filename)

    public_path = os.path.dirname(os.path.abspath(sys.argv[0]))  # 获取当前运行的.py文件所在的绝对路径
    # print('本文件目录位置：' + public_path)
    filename = os.path.join(public_path, 'report', now + 'report.html')
    # print('报告存放路径  ：' + filename)

    with open(filename, 'wb') as wf:
        # 定义测试报告
        runner = HTMLTestRunner(
            stream=wf,
            title="get post HTMLTestRunner",
            description="description"
        )
        runner.run(suite)
