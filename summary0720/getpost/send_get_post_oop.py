#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用类的方式整合'

__author__ = 'Victor Wu'

import json
import requests


class RunMain():

    def __init__(self, url, data=None, headers=None):
        # self.res = self.run_main(url, 'GET', param, header)
        self.res = self.run_main(url, 'POST', data, headers)
    
    def send_get(self, url, param=None, header=None):
        response = requests.get(url=url, params=param, headers=header)
        return json.loads(response.text)
    
    def send_post(self,url,data,header=None):
        response = requests.post(url=url, data=data, headers=header)
        return json.loads(response.text)

    def run_main(self, url, method, data=None, headers=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res

if __name__ == '__main__':  #本方法内使用

    # baseurl = 'http://httpbin.org/get'
    baseurl = 'http://httpbin.org/post'
    datalist = {
        'name':'zhangsan',
        'age':'25'
    }
    # run = RunMain(baseurl,'GET',datalist)
    # print(run.res)
    # print(run.run_main(baseurl,'GET',datalist))
 
    run = RunMain(baseurl,'POST',datalist)
    print(run.res)
    print(run.run_main(baseurl,'POST',datalist))
