#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'在getpost01的基础上，使用类封装接口测试脚本'

__author__ = 'Victor Wu'

import requests
import json
class RunMain():
    def __init__(self,base_url,method,datalist=None):
        self.res = self.run_main(baseurl,'GET',datalist)
        #self.res = self.run_main(baseurl,'POST',datalist)

    def send_get(self,base_url,datalist):
        res = requests.get(url=base_url, params=datalist).json()
        return json.dumps(res,sort_keys=True,indent=2)

    def send_post(self,base_url,datalist):
        res = requests.post(url=base_url, data=datalist).json()
        return json.dumps(res,indent=2,sort_keys=True)

    def run_main(self,base_url,method,datalist=None):
        res = None
        if method == 'GET':
            res = self.send_get(base_url,datalist)
        else:   
            res = self.send_post(base_url,datalist)
        return res

if __name__ == '__main__':

    baseurl = 'http://httpbin.org/get'
    #baseurl = 'http://httpbin.org/post'
    datalist = {
        'name':'zhangsan',
        'age':'25'
    }
    run = RunMain(baseurl,'GET',datalist)
    #run = RunMain(baseurl,'POST',datalist)
    print('=================================')
    print(run.res)
    print('=================================')
    print(run.run_main(baseurl,'GET',datalist))
