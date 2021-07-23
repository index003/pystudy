#!/usr/bin/env python3.8

import requests
import unittest
import traceback
from urllib.parse import urljoin
from config import API_DOMAIN, API_ORDERS, TOKEN_ORDER
from config import API_TRADE, TOKEN_TARDE


class MyTest(unittest.TestCase):  # 封装测试环境的初始化和还原的类
    def setUp(self):  # 放对数据可操作的代码，如对mysql、momgodb的初始化等,这里不对数据库进行操作！
        print("start test")
        pass

    def tearDown(self):  # 与setUp()相对
        print("end test")
        pass


class testGetTrade(MyTest):  # 把这个接口封装一个类，下面的方法是具体的测试用例
    '''接口名称：用户交易'''  # 这个描述接口名称

    @staticmethod
    def get_order_list():
        order_no_list = []
        # 组合成接口
        api = urljoin(API_DOMAIN, API_ORDERS)
        headers = {
            "Content-Type": "application/json",
            "Authorization": TOKEN_ORDER
        }
        # 接口传送的参数
        data = {
            "pageNum": 1,
            "pageSize": 8
        }
        try:
            r = requests.post(url=api, json=data, headers=headers)
            r_dict = r.json()
        except Exception as e:
            print('调用orderNo接口发生异常，错误信息：{0}'.format(e))
            # 打印异常堆栈信息，有助于异常排查
            traceback.print_exc()
        else:
            # 请求成功会继续从此处执行
            if r_dict.get('rspCode') != '0000':
                # 接口反馈响应状态码非正常情况，此处添加异常处理逻辑
                print('orders接口响应状态码非0000，接口响应错误信息：{0}'.format(r_dict.get('message')))
                return order_no_list
            data = r_dict.get('data').get('list')
            for i in data:
                order_no_list.append(i.get('orderNo'))
        return order_no_list

    def test_trade_get(self):
        '''测试用例1：哈哈'''  # 这个描述接口用例名称
        api = urljoin(API_DOMAIN, API_TRADE)
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": TOKEN_TARDE
        }
        # 获取orderNo列表
        orders = self.get_order_list()
        if len(orders) == 0:
            print('未获取到orderNo数据')
            return
        for i in orders:
            print("---------- orderNo: {0} ------------".format(i))
            data = {
                'orderNo': i,
                'point': 1
            }
            try:
                r = requests.post(url=api, json=data, headers=self.headers)
                r_dict = r.json()
            except Exception as e:
                print('调用tradeSave接口发生异常，错误信息：{0}'.format(e))
                # 打印异常堆栈信息，有助于异常排查
                traceback.print_exc()
            else:
                # 请求成功会继续从此处执行
                if r_dict.get('rspCode') != '0000':
                    # 接口反馈响应状态码非正常情况，此处添加异常处理逻辑
                    print('tardeSave接口响应状态码非0000，接口响应错误信息：{0}'.format(r_dict.get('message')))
                    return
                # 接口响应正常，打印结果
                print('orderNo: {0}, trade save结果：{1}'.format(i, r.text))


if __name__ == "__main__":
    unittest.main()
