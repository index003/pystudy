#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""post方法的最原始的方法"""

__author__ = 'Victor Wu'

import requests
import json

url = 'http://httpbin.org/post'
data = {
    'name': 'zhangsan',
    'age': '25'
}

response = requests.post(url, data=data)
response.encoding = 'utf-8'
print(response.text)    # 字符串形式
res = json.loads(response.text)
print(res)  # 字典形式