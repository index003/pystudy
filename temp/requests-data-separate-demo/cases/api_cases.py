#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""使用数据分离调用get和post"""

__author__ = 'Victor Wu'

import unittest
import sys
import yaml
import configparser
from os.path import dirname, abspath
from api_keyword.keyword_demo import KeyDemo

project_path = dirname(dirname(abspath(__file__)))
sys.path.append(project_path)

# 创建一个UnitTest测试用例管理框架


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

    def test_01_api_demo(self):
        # # 实例化需要的内容
        # conf = configparser.ConfigParser()
        # conf.read('./config/config.ini')
        # kd = KeyDemo()
        with open('../data/get.yaml', 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        # url = conf.get('DEFAULT', 'url') + data['path']
        url = self.url + data['path']
        # # 执行测试
        res = self.kd.get(url, data['data'])
        print(res.text)

        ApiCases.value = self.kd.get_text(res.text, 'Name')
        print(self.value)
        self.assertEqual(first=data['text'], second=self.value, msg='获取信息失败')

    def test_02_value(self):
        # # 实例化需要的内容
        # conf = configparser.ConfigParser()
        # conf.read('./config/config.ini')
        # kd = KeyDemo()
        with open('../data/post.yaml', 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        # url = conf.get('DEFAULT', 'url') + data['path']
        url = self.url + data['path']
        # # 执行测试
        res = self.kd.post(url, data['data'])
        print(res.text)

        ApiCases.value = self.kd.get_text(res.text, 'Name')
        print(self.value)
        self.assertEqual(first=data['text'], second=self.value, msg='获取信息失败')


if __name__ == '__main__':
    unittest.main()