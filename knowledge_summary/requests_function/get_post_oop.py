#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""使用类（即面向对象）的方式实现函数式的requests的get和post请求"""

__author__ = 'Victor Wu'

import json
import requests


def json_dumps(data):
    return json.dumps(data)


class RunMain():

    # def __init__(self, url, data=None, headers=None):
    #     self.res = self.run_main(url, 'GET', data, headers)

    def send_get(self, url, param=None, header=None):
        response = requests.get(url=url, params=param, headers=header)
        return json.loads(response.text)

    def send_post(self, url, data, header=None):
        if data is not None:
            data = json_dumps(data)
        response = requests.post(url=url, data=data, headers=header)
        return json.loads(response.text)

    def run_main(self, url, method, data=None, headers=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res


if __name__ == '__main__':  # 本方法内使用

    get_url = 'http://httpbin.org/get'
    post_url = 'http://httpbin.org/post'
    datalist = {
        'name': 'zhangsan',
        'age': '25'
    }
    # 实例化
    # 如果__init__启用，就需要下面方式实例化
    # run = RunMain(baseurl, 'GET', datalist)
    run = RunMain()
    # 调用类run_main()方法
    response_main_get = run.run_main(get_url, 'GET', datalist)
    print(response_main_get)

    response_main_post = run.run_main(post_url, 'POST', datalist)
    print(response_main_get)

    # 调用类get()方法
    response_get = run.send_get(get_url, param=datalist)
    print(response_get)

    # 调用类post()方法
    response_post = run.send_post(post_url, datalist)
    print(response_post)
