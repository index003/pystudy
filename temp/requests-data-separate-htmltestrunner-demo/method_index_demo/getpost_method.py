#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""get、post及断言获取方法，供api调用调用"""

__author__ = 'Victor Wu'

import requests
import json
import jsonpath


class RunMain():

    def send_get(self, url, param=None, header=None):
        # response = requests.get(url=url, params=param, headers=header)
        # return json.loads(response.text)
        return requests.get(url=url, params=param, headers=header)

    def send_post(self, url, data, header=None):
        # response = requests.post(url=url, data=data, headers=header)
        # return json.loads(response.text)
        return requests.post(url=url, data=data, headers=header)

    def run_main(self, url, method, data=None, headers=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res

    def get_text(self, res, key):

        if res is not None:
            try:
                # 将res文本转换为JSON，通过jsonpath解析获取到指定的key的value值。
                text = json.loads(res)
                value = jsonpath.jsonpath(text, '$..{0}'.format(key))
                # jsonpath获取的结果是list类型的值,如果获取失败则是False
                if value:
                    # 将list转成String格式
                    if len(value) == 1:
                        return value[0]
                return value
            except Exception as e:
                return e
        else:
            return None
