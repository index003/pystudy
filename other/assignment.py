#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""测试用例集合"""
__author__ = 'Victor Wu'


# 处理kwargs的参数，递归方式解析字典格式的内容
def assignment(kwargs):
    for key, value in kwargs.items():
        if type(value) is dict:
            assignment(value)
        else:
            if value:
                pass
            else:
                kwargs[key] = getattr(key)
    print(kwargs)
    return kwargs


# 处理kwargs的参数，递归方式解析字典格式的内容
datalist = {
    'data': 'victor',
    'data2': {
        'name': 'amber',
        'age': 18,
        'score': {
            'math': 99,
            'English': 99.5
        }
    },
    'data3': {
        'gender': 'male'
    }
}

assignment_result = assignment(datalist)
