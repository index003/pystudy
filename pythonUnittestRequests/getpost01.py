#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'未封装的时候get和post调用'

__author__ = 'Victor Wu'

import requests
import json


def send_get(base_url,datalist):
    res = requests.get(url=base_url, data=datalist).json()
    return json.dumps(res,sort_keys=True,indent=2)

def send_post(base_url,datalist):
    res = requests.post(url=base_url, data=datalist).json()
    return json.dumps(res,indent=2,sort_keys=True)

def run_main(base_url,method,datalist=None):
    res = None
    if method == 'GET':
        res = send_get(base_url,datalist)
    else:   
        res = send_post(base_url,datalist)
    return res


baseurl = 'http://httpbin.org/get'
datalist = {
        'name':'zhangsan',
        'age':'25'
    }

print(run_main(baseurl,'GET',datalist))

print("==============================")

baseurl = 'http://httpbin.org/post'
datalist = {
        'name':'zhangsan',
        'age':'25'
    }
print(run_main(baseurl,'POST',datalist))
