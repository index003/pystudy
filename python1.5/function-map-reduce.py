# -*- coding: utf-8 -*-
# Python内建了map()和reduce()函数
# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

def f(x):
    return x * x

r = map(f,[1,2,3,4,5,6,7,8,9])
# print(r)
lr = list(r)
print(lr)

# 不需要map()函数，写一个循环，也可以计算出结果
L = []
for n in [1,2,3,4,5,6,7,8,9]:
    L.append(f(n))
print(L)

# 的确可以，但是，从上面的循环代码，我们不能一眼看明白“把f(x)作用在list的每一个元素并把结果生成一个新的list”
# map()作为高阶函数，事实上它把运算规则抽象了，
# 因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串
l = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(l)



# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce

def add(x,y):
    return x + y
sum0 = reduce(add,[1,2,3,4,5,6])
print(sum)

# 当然求和运算可以直接用Python内建函数sum()，没必要动用reduce。

# 但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场

def fn(x,y):
    return 10 * x + y
mul = reduce(fn,[1,3,5,7,9])
print(mul)

# 这个例子本身没多大用处，但是，如果考虑到字符串str也是一个序列，
# 对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数

def char2num(s):
    digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digits[s]
char2 = reduce(fn,map(char2num,'13579'))
print(char2)

# 整理成一个str2int的函数就是

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
char3 = str2int('13579')
print(char3)

# 还可以用lambda函数进一步简化成
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
char4 = str2int('13579')
print(char4)

# 也就是说，假设Python没有提供int()函数，你完全可以自己写一个把字符串转化为整数的函数，而且只需要几行代码！