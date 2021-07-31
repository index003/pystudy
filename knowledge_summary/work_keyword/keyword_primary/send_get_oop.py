#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用类（即面向对象）的方式整合get_demo'

__author__ = 'Victor Wu'

import sys
import unittest
from os.path import dirname, abspath
import configparser
import yaml
from work_keyword.keyword_demo.keyword_method import RunMain


class OopGet():

    project_path = dirname(dirname(abspath(__file__)))
    print(project_path)

    sys.path.append(project_path)

    # 实例化需要的内容
    conf = configparser.ConfigParser()
    rm = RunMain()
    with open('../data/get.yaml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    # 测试数据
    conf.read('../config/config.ini')
    # print(conf.get('DEFAULT', 'url'))
    url = conf.get('DEFAULT', 'url') + data['path']
    print(url)

    # 执行测试
    res = rm.run_main(url, 'GET', data['data'])
    print(res.text)


if __name__ == '__main__':  # 本方法内使用
    pass