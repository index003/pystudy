#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""使用unittest调用oop的get和post请求"""

__author__ = 'Victor Wu'

import unittest
from get_post_requests import RunMain


class TestMethod(unittest.TestCase):

    def setUp(self):
        self.run = RunMain()

    def test_001_get(self):
        get_url = 'http://httpbin.org/get'
        datalist = {
            'name': 'zhangsan',
            'age': '25'
        }
        res = self.run.run_main(get_url, 'GET', datalist)
        print(res)
        self.assertEqual(res['args']['age'], '25', 'Passed')

    # @unittest.skip('test_002_post')   # 当前用例不执行
    def test_002_post(self):
        post_url = 'http://httpbin.org/post'
        datalist = {
            'name': 'zhangsan',
            'age': '25'
        }
        res = self.run.run_main(post_url, 'POST', datalist)
        print(res)
        self.assertEqual(res['json']['age'], '26', 'Failed')


if __name__ == '__main__':
    # unittest.main()   # 全部执行，下面的方式可以自己组织
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_001_get'))
    suite.addTest(TestMethod('test_002_post'))
    unittest.TextTestRunner().run(suite)
