#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""将function_yaml改成面向对象方式"""

__author__ = 'Victor Wu'

import configparser
import yaml
from common.get_post_requests import RunMain


class OopRequests():

    # 实例化需要的内容
    conf = configparser.ConfigParser()
    rm = RunMain()

    with open('./data/get.yaml', 'r', encoding='utf-8') as f:
        get_data = yaml.safe_load(f)

    # get测试数据
    conf.read('./config/config.ini')
    get_url = conf.get('DEFAULT', 'url') + get_data['path']

    # 执行get测试
    res = rm.run_main(get_url, 'GET', get_data['data'])
    print(res.text)

    print('===========这是分割线===========')

    with open('./data/post.yaml', 'r', encoding='utf-8') as f:
        post_data = yaml.safe_load(f)

    # post测试数据
    conf.read('./config/config.ini')
    post_url = conf.get('DEFAULT', 'url') + post_data['path']

    # 执行post测试
    res = rm.run_main(post_url, 'POST', post_data['data'])
    print(res.text)


if __name__ == '__main__':  # 本方法内使用
    pass
