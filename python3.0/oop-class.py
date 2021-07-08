#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 类和实例'

__author__ = 'Victor Wu'

# class后面紧接着是类名，即Student，类名通常是大写开头的单词，
# 紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，
# 通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。

class Student(object):
# 在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。### 所以__init__也可以不写 ###
# 通过定义一个特殊的__init__方法
    def __init__(self,name,score):
        self.name = name
        self.score = score
# 注意：特殊方法“__init__”前后分别有两个下划线
# __init__方法的第一个参数永远是self，表示创建的实例本身，
# 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，
# 但self不需要传，Python解释器自己会把实例变量传进去

# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，
# 并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，
# 所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。

# 要定义一个方法，除了第一个参数是self外，其他和普通函数一样。
# 要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            print('A')
        elif self.score >=60:
            print('B')
        else:
            print('C')

lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())
