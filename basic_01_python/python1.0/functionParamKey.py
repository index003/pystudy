# -*- coding: utf-8 -*-
#关键字参数允许你传入0个或任意个含参数名的参数，
#这些关键字参数在函数内部自动组装为一个dict
def person(name,age,**key):
    print('name:',name,'age:',age,'other:',key)
#在调用该函数时，可以只传入必选参数
person('Mike',30)
#也可以传入任意个数的关键字参数
person('Mike',30,gender = 'M',job = 'Player')
#用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，
#利用关键字参数来定义这个函数就能满足注册的需求

#和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
extra = {'city':'Beijing','job':'engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
#可以用简化的写成下面形式
person('Jack',24,**extra)
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
#kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。


#我们希望检查是否有city和job参数
def person(name,age,**kw):
    if 'city' in kw:
        #有city参数
        pass
    if 'job' in kw:
        #有job参数
        pass
    print('name:',name,'age:',age,'other:',kw)
#但是调用者仍可以传入不受限制的关键字参数
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

#命名关键字参数
#如果要限制关键字参数的名字，就可以用命名关键字参数，
#例如，只接收city和job作为关键字参数。这种方式定义的函数如下
def person(name,age,*,city,job):
    print(name,age,city,job)
#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
person('Jack', 24, city='Beijing', job='Engineer')

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name,age,*args,city,job):
    print(name,age,args,city,job)
#命名关键字参数必须传入参数名
#person('Jack', 24, 'Beijing', 'Engineer')
person('Jack', 24, city='Beijing', job='Engineer')
person('Jack', 24, 'A',city='Beijing', job='Engineer')

#命名关键字参数city具有默认值，调用时，可不传入city参数
def person(name,age,*,city='shanghai',job):
    print(name,age,city,job)

person('Jack',24,job='Engineer')

def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass

#参数组合
#Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def f1(a,b,c=0,*args,**kw):
    print(a,b,c,args,kw)

def f2(a,b,c=0,*,d,**kw):
    print(a,b,c,d,kw)

f1(1,2)
f1(1,2,c=3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',kk='AB')
f1(1,2,3,'a','b',x=99)
f2(1,2,d=99,ext=None)

#通过一个tuple和dict，你也可以调用上述函数
args = (1,2,3,4)
kw = {'d':99,'x':'#'}
f1(*args,**kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args,**kw)
#对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
##虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。