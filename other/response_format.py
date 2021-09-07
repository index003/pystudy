#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""处理json字符串"""
__author__ = 'Victor Wu'

from json.decoder import JSONDecoder
from json.encoder import JSONEncoder
import requests
import json

# 主站顶部导航栏
url = 'https://api.bitgame.com/sp/maintain/config/list'
# 发送请求的结果
response_get = requests.get(url)
# 将结果转码，大部分情况不需要
response_get.encoding = 'utf-8'
# 字符串方式
print(response_get.text)
print("=========这是分割线===========")
# 转为json，字典方式
res_get = json.loads(response_get.text)
print(res_get)
print("=========这是分割线===========")

data_list = res_get.get('data')
print(data_list)
print("=========这是分割线===========")
data_list_0 = data_list[0]
print(data_list_0)
print("=========这是分割线===========")
data_list_0_key = data_list_0.get('type')
print(data_list_0_key)



data = [{
    "name": "Tom",
    "gender": "male"
}, {
    "name": "杰克",
    "gender": "男"   
}]
 
#将json格式转为字符串
print(type(data))
str = json.dumps(data, indent=2) #indent=2按照缩进格式
print(type(str))
print(str)
str2 = JSONEncoder.__str__(data)
print(type(str2))
print(str2)

data_str = {"name": "miluo", "age": 18, "salary": "10k"}
s = """{"name": "miluo", "age": 18, "salary": "10k"}"""
s = json.dumps(s)
print(s)

