# -*- coding: utf-8 -*-
import functools
import time
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
def now():
    print('1==2021-7-6')
f = now
f()
# 函数对象有一个__name__属性，可以拿到函数的名字
fn = f.__name__
print(fn)

# 现在，假设我们要增强now()函数的功能，
# 比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# 本质上，decorator就是一个返回函数的高阶函数。
# 所以，我们要定义一个能打印日志的decorator，可以定义如下

def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2==2021-7-6')
# 调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志
now()
# 在wrapper()函数内，首先打印日志，再紧接着调用原始函数。

# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本
def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():'%(text, func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('3==2021-7-7')
now()
# 首先执行log('execute')，返回的是decorator函数，
# 再调用返回的函数，参数是now函数，
# 返回值最终是wrapper函数

# 一个完整的decorator的写法如下


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('4==2021-7-6')
now()

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print('5==2021-7-7')
now()

'''
练习
请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
'''
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args):
        t1 = time.time()
        ex = fn(*args)
        t2 = time.time()
        print('%s exhauted in %s ms' %(fn.__name__,t2-t1))
        return ex # 返回ex
    return wrapper
# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功!')

'''
请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
'''
def log1(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('begin call %s():' % fn.__name__)
        res = fn(*args, **kw)
        print('begin call %s():' % fn.__name__)
        return res
    return wrapper
@log1
def now():
    print('8==2021-7-7')
now()

'''
写出一个@log的decorator，使它既支持：
@log
def f():
    pass
又支持：

@log('execute')
def f():
    pass
'''
def log2(str):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kw):
            if callable(str):
                print('call %s():' % fn.__name__)
                return fn(*args, **kw)
            else:
                print('%s %s():' % (str, fn.__name__))

        return wrapper

    if callable(str):
        return decorator(str)
    return decorator

@log2
def now():
    print('6==2021-7-7')
now()

@log2('execute')
def now():
    print('7==2021-7-7')
now()

