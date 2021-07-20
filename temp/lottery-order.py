#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'提交赛事订单'

__author__ = 'Victor Wu'

import requests
import json
import unittest

class OrderSubmit(unittest.TestCase):

# 初始化数据
    def setUp(self):
        self.order_url = 'https://fat1-api.testbitgame.com/lottery/platform/v2/orders'

# 测试增加单号接口
    def test_submitOrder_success(self):
        datalist = {
            "centralized":True,
            "currency":"XRP",
            "marketOptions":[{"marketOptionLaunchId":'208675',"optionOdds":'1.02',"betAmount":"32"}],
            "singleOptionLaunchIds":['208675']
        }

        # 过长字符串换行\

        head = {
            'Content-Type':'application/json',
            'charset':'UTF-8',
            'authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.'\
                'eyJleHAiOjE2MjYzMDA1MTUsImlhdCI6MTYyNjI1NzMxNSwidXNlcl9uYW'\
                    '1lIjoiODU3NjkyNDQ1IiwianRpIjoiZjYwNTNjZGMtZDYxOC00MmUwLT'\
                        'k3N2YtOGU4N2EzN2Q5MjFlIiwiY2xpZW50X2lkIjoid3d3Iiwic2Nvc'\
                            'GUiOlsidWkiXX0.NodoNWdn5aYSwhrjSmEx5yXSBctVNyfSvYxtOJRxjNM',
        }

        r = requests.post(self.order_url,data=json.dumps(datalist),headers=head)
        print(r.url)
        result = json.loads(r.text)            #使用json格式返回
        print(result)
        self.assertEqual(result['rspCode'], 'S3001001')      #检验返回值
        print(result)

if __name__ == '__main__':
      unittest.main()
