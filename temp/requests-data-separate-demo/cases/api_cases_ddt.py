#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""使用ddt数据分离调用get和post"""

__author__ = 'Victor Wu'

import unittest
import sys
from os.path import dirname, abspath
from api_keyword.keyword_demo import KeyDemo
import configparser
import ddt


project_path = dirname(dirname(abspath(__file__)))
sys.path.append(project_path)


# 创建一个UnitTest测试用例管理框架

@ddt.ddt
class ApiCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.value = None
        # 实例化需要的内容
        conf = configparser.ConfigParser()
        conf.read('../config/config.ini')
        cls.url = conf.get('DEFAULT', 'url')
        cls.kd = KeyDemo()

        # 测试用例

    @ddt.file_data('../data/get_demo.yaml')
    def test_01_api_demo(self, **kwargs):
        url = self.url + kwargs['path']
        print(url)
        # # 执行测试
        res = self.kd.get(url, kwargs['data'])
        print(res.text)

        ApiCases.value = self.kd.get_text(res.text, 'Name')
        print(self.value)
        self.assertEqual(first=kwargs['text'], second=self.value, msg='获取信息失败')


if __name__ == '__main__':
    unittest.main()
