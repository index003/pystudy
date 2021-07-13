#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用requests post'

__author__ = 'Victor Wu'

# 基本post请求：
# 通过post把数据提交到url地址，等同于一字典的形式提交form表单里面的数据

import requests

url = 'http://httpbin.org/post'

data = {
    'name':'zhangsan',
    'age':'25'
}

response = requests.post(url,data=data)
print(response.url)
print(response.text)

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

# 使用request内置的字母判断状态码
 
#如果response返回的状态码是非正常的就返回404错误
if response.status_code != requests.codes.ok:
    print('404')
 
#如果页面返回的状态码是200，就打印下面的状态
response = requests.get('http://www.jianshu.com')
if response.status_code == 200:
    print('200')