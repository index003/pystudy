#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用unittest调用oop的get和post请求'

__author__ = 'Victor Wu'

from demo.send_get_post_oop import RunMain
import sys
import os

class TestMethod():

    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(base_path)

    def test_001_get(self):
        baseurl = 'http://httpbin.org/get'
        datalist = {
        'name':'zhangsan',
        'age':'25'
        }
        res = self.run.run_main(baseurl,'GET',datalist)
        print(res)
        self.assertEqual(res['args']['age'], '25','Passed')