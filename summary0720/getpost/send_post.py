#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用json'

__author__ = 'Victor Wu'

import requests
import json

url = 'http://httpbin.org/post'

data = {
    'name':'zhangsan',
    'age':'25'
}

# response = requests.post(url,json=data)
response = requests.post(url,data=data) # 两种方式都可以
response.encoding = 'utf-8'
print(response.text)    # 字符串形式
res = json.loads(response.text)
print(res)  # 字典形式