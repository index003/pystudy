#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""数据分离使用unittest调用get和post请求"""

__author__ = 'Victor Wu'

import configparser
import unittest
import yaml
from common.get_post_requests import RunMain


class TestMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.value = None
        # 实例化需要的内容
        conf = configparser.ConfigParser()
        conf.read('./config/config.ini')
        cls.url = conf.get('DEFAULT', 'url')
        cls.rm = RunMain()

    def test_001_get(self):
        with open('./data/get.yaml', 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        url = self.url + data['path']
        # # 执行测试
        res = self.rm.run_main(url, 'GET', data['data'])
        print(res.text)

        TestMethod.value = self.rm.get_text(res.text, 'name')
        print(self.value)
        self.assertEqual(first=data['text'], second=self.value, msg='获取信息失败')

    # @unittest.skip('test_002_post')   # 当前用例不执行
    def test_002_post(self):
        with open('./data/post.yaml', 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        url = self.url + data['path']
        # 执行测试
        res = self.rm.run_main(url, 'POST', data['data'])
        print(res.text)
        self.assertEqual(res['form']['age'], '26', 'Failed')


if __name__ == '__main__':
    # unittest.main()   # 全部执行，下面的方式可以自己组织
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_001_get'))
    suite.addTest(TestMethod('test_002_post'))
    unittest.TextTestRunner().run(suite)
