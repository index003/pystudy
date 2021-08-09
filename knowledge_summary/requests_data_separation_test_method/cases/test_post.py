#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""供discover调用"""

__author__ = 'Victor Wu'

import configparser
import unittest
import ddt
from common.get_post_requests import RunMain


@ddt.ddt
class TestMethodDDT(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.value = None
        # 实例化需要的内容
        conf = configparser.ConfigParser()
        conf.read('./config/config.ini')
        cls.url = conf.get('DEFAULT', 'url')
        cls.rm = RunMain()

    def setUp(self):
        print('<=================>')

    @ddt.file_data('../data/post_ddt.yaml')
    def test_001_get(self, **kwargs):
        url = self.url + kwargs['path']
        # # 执行测试
        res = self.rm.run_main(url, 'POST', kwargs['data'])
        print(res.text)

        TestMethodDDT.value = self.rm.get_text(res.text, 'name')
        print(self.value)
        self.assertEqual(first=kwargs['text'], second=self.value, msg='获取信息失败')


if __name__ == '__main__':
    unittest.main()
