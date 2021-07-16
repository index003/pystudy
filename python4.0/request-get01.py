#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用requests get'

__author__ = 'Victor Wu'

import requests

# Requests是用python语言基于urllib编写的，
# 采用的是Apache2 Licensed开源协议的HTTP库，
# Requests它会比urllib更加方便，可以节约我们大量的工作。
# 基本GET
response = requests.get("http://httpbin.org/get")
# print(type(response))
# print(response.status_code)
# print(type(response.text))
response.encoding = 'utf-8'
print(response.text)
# print(response.cookies)
print('=========================================')
# print(response.content)
print(response.content.decode("utf-8"))
print('=========================================')

'''
response.text返回的是Unicode格式，通常需要转换为utf-8格式，否则就是乱码。
response.content是二进制模式，可以下载视频之类的，如果想看的话需要decode成utf-8格式。
不管是通过response.content.decode("utf-8)的方式
还是通过response.encoding="utf-8"的方式都可以避免乱码的问题发生
'''
'''
# 一大推请求方式
requests.post("http://httpbin.org/post")
requests.put("http://httpbin.org/put")
requests.delete("http://httpbin.org/delete")
requests.head("http://httpbin.org/get")
requests.options("http://httpbin.org/get")
'''

# 带参数的GET请求

url = 'http://httpbin.org/get'

data = {
    'name':'zhangsan',
    'age':'25'
}

response = requests.get(url,params=data)

response.encoding = 'utf-8'
print(response.text)
# print(response.cookies)
print('=========================================')
# print(response.content)
print(response.content.decode("utf-8"))
print('=========================================')
