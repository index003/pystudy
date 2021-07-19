#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'在getpost02的基础上，使用unittest'

__author__ = 'Victor Wu'

import unittest
from getpost02 import RunMain

class TestMethod(unittest.TestCase):
    
    def setUp(self):
        self.run = RunMain()

    def test_01(self):
        baseurl = 'http://httpbin.org/get'
        datalist = {
        'name':'zhangsan',
        'age':'25'
        }
        res = self.run.run_main(baseurl,'GET',datalist)
        print(res)

        self.assertEqual(res['args']['age'], '25','Passed')

        # globals()['userid'] = '1000023'

    # @unittest.skip('test_02')   # 当前用例不执行
    def test_02(self):
        # print(self.userid)
        baseurl = 'http://httpbin.org/post'
        datalist = {
        'name':'zhangsan',
        'age':'25'
        }
        res = self.run.run_main(baseurl,'POST',datalist)
        print(res)
        print(type(res))
        self.assertEqual(res['form']['age'], '26','Failed')

if __name__ == '__main__':
    # unittest.main() # 下面的方式一样
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_01'))
    suite.addTest(TestMethod('test_02'))
    unittest.TextTestRunner().run(suite)