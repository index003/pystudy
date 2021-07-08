#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'使用@property'

__author__ = 'Victor Wu'

'''
为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数：

class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
'''
# 上面的调用方法又略显复杂
# Python内置的@property装饰器就是负责把一个方法变成属性调用的
'''
把一个getter方法变成属性，只需要加上@property就可以了，
此时，@property本身又创建了另一个装饰器@score.setter，
负责把一个setter方法变成属性赋值，
于是，我们就拥有一个可控的属性操作
'''

class Student(object):

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60    # OK，实际转化为s.set_score(60)
print(s.score)  # OK，实际转化为s.get_score()
# s.score = 9999
# print(s.score)

# 定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性

class Student2(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
# birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来

'''
练习
请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
'''
class Screen(object):
    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    @width.setter
    def width(self,value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value <= 0:
            raise ValueError('score must over 0!')
        self.__width = value
    
    @height.setter
    def height(self,value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value <= 0:
            raise ValueError('score must over 0!')
        self.__height = value
    @property
    def resolution(self):
        return self.__height * self.__width

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')