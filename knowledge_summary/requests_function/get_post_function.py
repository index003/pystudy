#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""get和post最原始的方法"""

__author__ = 'Victor Wu'

import requests
import json

# 请求需要的url和参数
get_url = 'http://httpbin.org/get'
data = {
    'name': 'zhangsan',
    'age': '25'
}

# 发送请求的结果
response_get = requests.get(get_url, params=data)
# 将结果转码，大部分情况不需要
response_get.encoding = 'utf-8'
# 字符串方式
print(response_get.text)
# 转为json，字典方式
res_get = json.loads(response_get.text)
print(res_get)
print("=========这是分割线===========")
post_url = 'http://httpbin.org/post'
# 发送请求的结果
response_post = requests.post(post_url, data=data)
# 将结果转码，大部分情况不需要
response_post.encoding = 'utf-8'
# 字符串方式
print(response_post.text)
# 转为json，字典方式
res_post = json.loads(response_post.text)
print(res_post)
