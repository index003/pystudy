#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""使用数据分离调用post"""


__author__ = 'Victor Wu'


import sys
from os.path import dirname, abspath
from work_keyword.api_keyword.keyword_demo import KeyDemo
import configparser
import yaml

project_path = dirname(dirname(abspath(__file__)))
sys.path.append(project_path)

# 实例化需要的内容
conf = configparser.ConfigParser()
kd = KeyDemo()

with open('../data/post.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

# 测试数据
conf.read('../config/config.ini')
url = conf.get('DEFAULT', 'url') + data['path']

# 执行测试
res = kd.post(url, data['data'])
print(res.text)
