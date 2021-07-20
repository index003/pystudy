#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用__slots__'

__author__ = 'Victor Wu'

'''
Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
'''
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

class GraduateStudent(Student):
    pass

s = Student() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误
# ERROR: AttributeError: 'Student' object has no attribute 'score'
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
g = GraduateStudent()
g.score = 99
print('g.score =', g.score)

# 在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__