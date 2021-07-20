#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用json'

__author__ = 'Victor Wu'

import json
import requests
# Json数据

response = requests.get("http://httpbin.org/get")
res = response.json()
# print(type(response.text))
print('=========================================')
print(res)
print('=========================================')
print(json.dumps(res, sort_keys=True, indent=2))
print('=========================================')
print(json.loads(response.text))
print('=========================================')
# print(type(response.json()))
print('=========================================')
#打印请求页面的状态（状态码）
print(type(response.status_code),response.status_code)
print('=========================================')
#打印请求网址的headers所有信息
print(type(response.headers),response.headers)
print('=========================================')
#打印请求网址的cookies信息
print(type(response.cookies),response.cookies)
print('=========================================')
#打印请求网址的地址
print(type(response.url),response.url)
print('=========================================')
#打印请求的历史记录（以列表的形式显示）
# print(type(response.history),response.history)
print('=========================================')

# 添加Header头

url = 'https://www.zhihu.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}
response = requests.get(url,headers=headers)
response.encoding = 'utf-8'
print(response.text)