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

    def test_02(self):
        baseurl = 'http://httpbin.org/post'
        datalist = {
        'name':'zhangsan',
        'age':'25'
        }
        res = self.run.run_main(baseurl,'POST',datalist)
        print(res)
        print(type(res))

if __name__ == '__main__':
    unittest.main()