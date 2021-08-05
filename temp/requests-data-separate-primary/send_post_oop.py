#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用类（即面向对象）的方式整合post_demo'

__author__ = 'Victor Wu'

import sys
import unittest
import configparser
import yaml
from os.path import dirname, abspath
from method_index_demo.getpost_method import RunMain


class OopPost(unittest.TestCase):
    project_path = dirname(dirname(abspath(__file__)))
    sys.path.append(project_path)

    # 实例化需要的内容
    conf = configparser.ConfigParser()
    rm = RunMain()

    with open('./data/post.yaml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    # 测试数据
    conf.read('./config/config.ini')
    url = conf.get('DEFAULT', 'url') + data['path']

    # 执行测试
    res = rm.run_main(url, 'POST', data['data'])
    print(res.text)


if __name__ == '__main__':  # 本方法内使用
    unittest.main()