#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'分类菜单查询'
'https://fat1-api.testbitgame.com/lottery/platform/menus?lang=zh-Hans&type=0&launchType=CENTRALIZED'
__author__ = 'Victor Wu'

import unittest     #导入unittest
import requests     #导入requests库
import json         #导入json

class TestMenus(unittest.TestCase):     #定义一个类，类的首字母要大写

    def setUp(self):                    #初始化
        self.base_url = 'https://fat1-api.testbitgame.com/lottery/platform/menus' 

    def test_get_success(self):         #定义一个方法，切记要以test开头
        datalist = {                    #定义传参数据
            'lang':'lang=zh-Hans',
            'type':'0',
            'launchType':'CENTRALIZED'
        }
        head = {                        #定义头部
            'Content-Type': 'application/Json',
            'charset':'UTF-8'
            }
             
        r = requests.get(self.base_url, params=datalist, headers=head)     #传入参数
        
        result = json.loads(r.text)            #使用json格式返回
        self.assertEqual(result['rspCode'], '0000')      #检验返回值
        print(result)
        res = json.dumps(r.json(),indent=2,sort_keys=True)
        print(res)

if __name__ == '__main__':
      unittest.main()