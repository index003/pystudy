#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' about class and instance '

__author__ = 'Victor Wu'

# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），
# 只有内部可以访问，外部不能访问

class Student(object):
    def __init__(self,name,score,gender):
        self.__name = name
        self.__score = score
        self.__gender = gender

    def get_name(self):
        return self.__name    
    def get_score(self):
        return self.__score
    def get_gender(self):
        return self.__gender

    def set_name(self,name):
        self.__name = name
    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
    def set_gender(self,gender):
        self.__gender = gender
    

    def print_score(self):
        print('%s : %s' % (self.__name,self.__score))
# 改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问实例变量.__name和实例变量.__score了
'''
bart = Student('Bart Simpson', 59)
bart.__name
访问就会报错
'''
# 如果外部代码要获取name和score怎么办？
# 可以给Student类增加get_name和get_score这样的方法

# 如果又要允许外部代码修改score怎么办？
# 可以再给Student类增加set_score方法

# 用set的方法，可以加一些判断，而不是每次调用的时候做判断

'''
在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
但是，按照约定俗成的规定，当你看到这样的变量时，
意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。


'''
# 测试:
bart = Student('Bart', 100,'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')