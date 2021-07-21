#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" get post请求 """

__author__ = 'Victor Wu'

import requests

class KeyDemo:

    def send_get(self, url, headers=None, param=None):
        return requests.get(url=url, headerss=headers, params=param)
    
    def send_post(self, url, headers=None, param=None):
        return requests.post(url=url, headers=headers, data=param)