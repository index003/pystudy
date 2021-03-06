# -*- coding: utf-8 -*-
import functools
# 介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。
# 而偏函数（Partial function）也可以做到这一点
# int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换
n = int('12345')
print(n)

# 但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换
n = int('12345',base=8)
print(n)
n = int('12345',base=16)
print(n)

# 假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，
# 于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去
def int2(x,base=2):
    return int(x,base)
n = int2('10000000')
print(n)
n = int2('110')
print(n)

# functools.partial就是帮助我们创建一个偏函数的，
# 不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2
int2 = functools.partial(int,base=2)
n = int2('10000000')
print(n)
n = int2('110')
print(n)

# 上面的新的int2函数，仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值
n = int2('110',base=10)
print(n)

'''
# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，当传入：

int2 = functools.partial(int, base=2)
# 实际上固定了int()函数的关键字参数base，也就是：

int2('10010')
# 相当于：

kw = { 'base': 2 }
int('10010', **kw)
# 当传入：

max2 = functools.partial(max, 10)
# 实际上会把10作为*args的一部分自动加到左边，也就是：

max2(5, 6, 7)
# 相当于：

args = (10, 5, 6, 7)
max(*args)
# 结果为10。

'''
# 可以参考函数参数那一节
