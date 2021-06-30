# -*- coding: utf-8 -*-
#给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
L = ['Jack','Mike','Victor','Tiger']
for i in range(4):
    print(L[i])

D = {'a':2,'b':3}
for key in D:
    print(key)

for value in D.values():
    print(value)

for k, v in D.items():
    print(k,v)

#由于字符串也是可迭代对象，因此，也可以作用于for循环
for ch in 'Victor':
    print(ch)

#所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，
# 而我们不太关心该对象究竟是list还是其他数据类型
#如何判断一个对象是可迭代对象呢？方法是通过collections.abc模块的Iterable类型判断
from collections.abc import Iterable
# str是否可迭代
print(isinstance('abc', Iterable))
# list是否可迭代
print(isinstance([1,2,3], Iterable))
# tuple是否可迭代
print(isinstance({'a':2,'b':3}, Iterable))
# 整数是否可迭代
print(isinstance(123, Iterable))

# 如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对，
# 这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

#上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码
for x,y in [(1,1),(2,2)]:
    print(x,y)

#请使用迭代查找一个list中最小和最大值，并返回一个tuple

def findMinAndMax(l):
    if  len(l) == 0:
        return(None,None)
    elif len(l) == 1:
        return(l[0],l[0])
    else:
        min = l[0]
        max = l[0]
        for i in l:
            if i >= max:
                max = i
            if i <= min:
                min = i
    return(min,max)

l = [8,-3,3,1,-8,7,-1,9,0] 
print(findMinAndMax(l))

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')