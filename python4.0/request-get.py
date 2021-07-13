#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用requests get'

__author__ = 'Victor Wu'

import requests

# Requests是用python语言基于urllib编写的，
# 采用的是Apache2 Licensed开源协议的HTTP库，
# Requests它会比urllib更加方便，可以节约我们大量的工作。

response = requests.get("https://www.baidu.com/")
print(type(response))
print(response.status_code)
print(type(response.text))
response.encoding = 'utf-8'
print(response.text)
print(response.cookies)

print(response.content)
print(response.content.decode("utf-8"))

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
# 基本GET

url = 'https://www.baidu.com'
response = requests.get(url)
print(response.text)

# 带参数的GET请求

url = 'http://httpbin.org/get'

data = {
    'name':'zhangsan',
    'age':'25'
}

response = requests.get(url,params=data)
print(response.url)
print(response.text)

# Json数据
import json
response = requests.get("http://httpbin.org/get")
print(type(response.text))
print(response.json())
print(json.loads(response.text))
print(type(response.json()))

#打印请求页面的状态（状态码）
print(type(response.status_code),response.status_code)
#打印请求网址的headers所有信息
print(type(response.headers),response.headers)
#打印请求网址的cookies信息
print(type(response.cookies),response.cookies)
#打印请求网址的地址
print(type(response.url),response.url)
#打印请求的历史记录（以列表的形式显示）
print(type(response.history),response.history)

# 添加Header头

url = 'https://www.zhihu.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}
response = requests.get(url,headers=headers)
print(response.text)

