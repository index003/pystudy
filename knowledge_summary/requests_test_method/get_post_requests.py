#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""get post方法，供unittest调用"""

__author__ = 'Victor Wu'

import json
import requests


def json_dumps(data):
    return json.dumps(data)


class RunMain():

    def send_get(self, url, param=None, header=None):
        response = requests.get(url=url, params=param, headers=header)
        return json.loads(response.text)

    def send_post(self, url, data, header=None):
        if data is not None:
            data = json_dumps(data)
        response = requests.post(url=url, data=data, headers=header)
        return json.loads(response.text)

    def run_main(self, url, method, data=None, headers=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res
