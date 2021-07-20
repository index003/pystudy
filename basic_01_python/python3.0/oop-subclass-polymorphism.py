#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 继承和多态'

__author__ = 'Victor Wu'

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

# 继承有什么好处？最大的好处是子类获得了父类的全部功能。
# 由于Animial实现了run()方法，因此，Dog和Cat作为它的子类，什么事也没干，就自动拥有了run()方法
dog = Dog()
dog.run()

cat = Cat()
cat.run()

# 也可以对子类增加一些方法，比如Tortoise类

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
tortoise = Tortoise()
tortoise.run()

# 新增一个Animal的子类，不必对run_twice()做任何修改，
# 实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，
# 原因就在于多态。
# 多态的意思通俗理解就是，狗有几种状态，首先它是Dog，同时它也是Animal，即一个角色有多个状态

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(cat)
run_twice(dog)
run_twice(tortoise)

'''
小结
继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，
子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写
'''