#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""使用数据分离调用get"""

__author__ = 'Victor Wu'


import sys
from os.path import dirname, abspath
from api_keyword.keyword_demo import KeyDemo
import configparser
import yaml

project_path = dirname(dirname(abspath(__file__)))
print(project_path)
sys.path.append(project_path)

# 实例化需要的内容
conf = configparser.ConfigParser()
kd = KeyDemo()

# 创建data
with open('../data/get.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
print(data)
print(type(data))
print(data['path'])
print(type(data['path']))
print(data['data'])
print(type(data['data']))
# 测试数据
conf.read('../config/config.ini')
# print(conf.get('DEFAULT', 'url'))
url = conf.get('DEFAULT', 'url') + data['path']

# 执行测试
res = kd.get(url, data['data'])
print(res.text)
