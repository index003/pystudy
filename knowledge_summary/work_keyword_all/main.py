#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""使用discover调用oop的get和post请求"""

__author__ = 'Victor Wu'

import unittest


class RunAllCase(unittest.TestCase):

    if __name__ == '__main__':
        # 测试用例存放路径
        case_path = '../keyword_cases'
        discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
        suite = unittest.TestSuite()
        runner = unittest.TextTestRunner()
        runner.run(discover)
