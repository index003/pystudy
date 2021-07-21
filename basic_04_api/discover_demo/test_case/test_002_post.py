#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用unittest调用oop的get和post请求'

__author__ = 'Victor Wu'

from demo.send_get_post_oop import RunMain

class TestMethod():
    
    def test_002_post(self):
        # print(self.userid)
        baseurl = 'http://httpbin.org/post'
        datalist = {
        'name':'zhangsan',
        'age':'25'
        }
        res = self.run.run_main(baseurl,'POST',datalist)
        print(res)
        self.assertEqual(res['form']['age'], '26','Failed')