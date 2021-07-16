#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'使用类封装接口测试脚本'

__author__ = 'Victor Wu'

import requests
import json

def send_get(base_url,datalist):
    res = requests.get(url=base_url, data=datalist).json()
    return json.dumps(res,sort_keys=True,indent=2)

def send_post(base_url,datalist):
    res = requests.post(url=base_url, data=datalist).json()
    return json.dumps(res,indent=2,sort_keys=True)

def run_main(base_url,datalist,method):
    if method == 'GET':
        send_get(base_url,datalist)
    else:
        send_post(base_url,datalist)

baseurl = 'http://httpbin.org/get'

datalist = {
    'name':'zhangsan',
    'age':'25'
}

run_main(baseurl,datalist,'GET')