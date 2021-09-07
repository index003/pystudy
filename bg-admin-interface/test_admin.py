#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""测试用例集合"""
__author__ = 'Victor Wu'

import unittest
import ddt
from getpost_method import RunMain
from config import API_DOMAIN


@ddt.ddt
class TestMethodDDT(unittest.TestCase):
    # 处理kwargs的参数，递归方式解析字典格式的内容
    """
    {
        data: victor,
        data2: {
            name: amber
            age: 18
            score:{
                math: 99
                English: 99.5
            }
        }
        data3:{
            gender: male
        }
    }

    """

    def assignment(self, kwargs):
        for key, value in kwargs.items():
            if type(value) is dict:
                self.assignment(value)
            else:
                if value:
                    pass
                else:
                    kwargs[key] = getattr(self, key)
        print(kwargs)
        return kwargs

    @classmethod
    def setUpClass(cls) -> None:
        cls.value = None
        cls.token = None
        # 实例化需要的内容
        cls.url = API_DOMAIN
        cls.rm = RunMain()

    def setUp(self):
        print('<=================>')

    # 发送登录验证码
    @ddt.file_data('./data/sendOtp.yaml')
    def test_001_sendOtp(self, **kwargs):
        url = self.url + kwargs['path']
        # # 执行测试
        res = self.rm.run_main(url, 'GET', kwargs['data'])
        TestMethodDDT.value = self.rm.get_text(res.text, 'rspCode')
        self.assertEqual(first=kwargs['text'], second=self.value, msg='获取短信成功')

    # 登录admin
    @ddt.file_data('./data/login.yaml')
    def test_002_login(self, **kwargs):
        url = self.url + kwargs['path']
        # # 执行测试
        res = self.rm.run_main(url, 'POST', kwargs['data'], kwargs['headers'])
        TestMethodDDT.value = self.rm.get_text(res.text, 'rspCode')
        TestMethodDDT.token = self.rm.get_text(res.text, 'token')
        print(self.value)
        print(self.token)
        self.assertEqual(first=kwargs['text'], second=self.value, msg='获取信息失败')

    # 设置赔率异常阈值
    @ddt.file_data('./data/set_return_rate.yaml')
    def test_003_set_return_rate(self, **kwargs):
        headers = kwargs['headers']
        headers['authorization'] = self.token
        url = self.url + kwargs['path']
        # 执行测试
        res = self.rm.run_main(url, 'POST', kwargs['data'], kwargs['headers'])
        TestMethodDDT.value = self.rm.get_text(res.text, 'rspCode')
        self.assertEqual(first=kwargs['text'], second=self.value, msg='获取信息成功')

    # 获取赔率异常阈值
    @ddt.file_data('./data/return_rate.yaml')
    def test_004_return_rate(self, **kwargs):
        headers = kwargs['headers']
        headers['authorization'] = self.token
        url = self.url + kwargs['path']
        # 执行测试
        res = self.rm.run_main(url, 'GET', kwargs['data'], kwargs['headers'])
        TestMethodDDT.value = self.rm.get_text(res.text, 'configValue')
        self.assertEqual(first=kwargs['text'], second=self.value, msg='获取信息成功')

    @ddt.file_data('./data/set_League.yaml')
    def test_005_setLeague(self, **kwargs):
        headers = kwargs['headers']
        headers['authorization'] = self.token
        url = self.url + kwargs['path'] + kwargs['id']
        # 执行测试
        res = self.rm.run_main(url, 'PATCH', kwargs['data'], kwargs['headers'])
        print(res.text)

    @ddt.file_data('./data/set_limit.yaml')
    def test_006_setLeague(self, **kwargs):
        headers = kwargs['headers']
        headers['authorization'] = self.token
        url = self.url + kwargs['path']
        # 执行测试
        res = self.rm.run_main(url, 'PATCH', kwargs['data'], kwargs['headers'])
        print(res.text)


if __name__ == '__main__':
    # 测试用例存放路径
    case_path = './'
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test_*.py")
    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner()
    runner.run(discover)
