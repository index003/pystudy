#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'使用类封装接口测试脚本'

__author__ = 'Victor Wu'

import unittest

class TestMethod(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('before--->class')
    
    @classmethod
    def tearDownClass(cls):
        print('after--->class')

    def tearUp(self):
        print('test--->terUp()')

    def tearDown(self):
        print('test--->tearDown()')

    def test_01(self):
        print('first test_01')

    def test_02(self):
        print('second test_02')

if __name__ == '__main__':
    unittest.main()