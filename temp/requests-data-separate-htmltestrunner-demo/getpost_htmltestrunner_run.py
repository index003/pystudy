#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用unittest调用oop的get和post请求，并且生成报告'

__author__ = 'Victor Wu'

import configparser
import unittest
import yaml
import time
import os
import sys
from HTMLTestRunner import HTMLTestRunner
from method_index_demo.getpost_method import RunMain


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

    now = time.strftime("%Y-%m-%d %H-%M-%S")
    public_path = os.path.dirname(os.path.abspath(sys.argv[0]))  # 获取当前运行的.py文件所在的绝对路径
    # public_path = os.path.dirname(__file__)  # 当前执行文件的路径 推荐使用这种方式
    # filename = public_path + "/report/" + now + "report.html"
    filename = os.path.join(public_path, 'report', now + 'report.html')
    print('==========', filename)
    with open(filename, 'wb') as wf:
        # 定义测试报告
        runner = HTMLTestRunner(
            stream=wf,
            title="get post HTMLTestRunner",
            description="description"
        )
        runner.run(suite)
