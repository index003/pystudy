#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用unittest调用oop的get和post请求'

__author__ = 'Victor Wu'

import configparser
import unittest
import ddt
import sys

from method_index_demo.getpost_method import RunMain


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

    @ddt.file_data('./data/get_demo.yaml')
    def test_001_get(self, **kwargs):
        url = self.url + kwargs['path']
        # # 执行测试
        res = self.rm.run_main(url, 'GET', kwargs['data'])
        print(res.text)

        TestMethodDDT.value = self.rm.get_text(res.text, 'name')
        print(self.value)
        self.assertEqual(first=kwargs['text'], second=self.value, msg='获取信息失败')

    # @unittest.skip('test_002_post')   # 当前用例不执行
    @ddt.file_data('./data/post_demo.yaml')
    def test_002_post(self, **kwargs):
        url = self.url + kwargs['path']
        # # 执行测试
        res = self.rm.run_main(url, 'POST', kwargs['data'])
        print(res.text)

        TestMethodDDT.value = self.rm.get_text(res.text, 'name')
        print(self.value)
        self.assertEqual(first=kwargs['text'], second=self.value, msg='获取信息失败')


if __name__ == '__main__':
    # unittest.main()   # 全部执行，下面的方式可以自己组织
    # unittest.main(argv=sys.argv, testRunner=unittest.TextTestRunner(verbosity=2))  # 全部执行，并且打印调用的用例
    suite = unittest.TestSuite()
    suite.addTest(TestMethodDDT('test_001_get_00001_demo'))
    suite.addTest(TestMethodDDT('test_001_get_00002_demo2'))
    suite.addTest(TestMethodDDT('test_002_post_00001_demo'))
    suite.addTest(TestMethodDDT('test_002_post_00002_demo2'))
    unittest.TextTestRunner().run(suite)
