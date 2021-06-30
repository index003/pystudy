# -*- coding: utf-8 -*-
# 列表生成式
# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式
# 要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))
L = list(range(1,11))
print(L[:])
print(L)

# 如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环
L = []
for x in range(1,11):
    L.append(x * x)
print(L)

# 方法二是列表生成式，则可以用一行语句代替循环生成上面的list
# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
L = [x * x for x in range(1,11)]
print(L)

########## 在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else
# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
#### 跟在for后面的if是一个筛选条件，不能带else
L = [x * x for x in range(1,11) if x % 2 == 0]
print(L)

#### for前面的部分是一个表达式，它必须根据x计算出一个结果。因此必须加上else
L = [x if x % 2 == 0 else -x for x in range(1, 11)]
print(L)


# 可以使用两层循环，可以生成全排列
L = [x + y for x in 'ABC' for y in 'XYZ']
print(L)

# 三层和三层以上的循环就很少用到了。
# 运用列表生成式，可以写出非常简洁的代码。
# 例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：

import os
D = [d for d in os.listdir('.')]
print(D)

# for循环其实可以同时使用两个甚至多个变量，
# 比如dict的items()可以同时迭代key和value
d = {'x':'A','y':'B','z':'C'}
for k,v in d.items():
    print(k,'=',v)

# 列表生成式也可以使用两个变量来生成list
l = [k + '=' + v for k,v in d.items()]
print(l)

# 把一个list中所有的字符串变成小写
L = ['Victor','Jack','Mike','Amber']
l = [s.lower() for s in L]
print(L)
print(l)

K = ['Victor','Jack',18,'Mike','Amber']
l = [n for n in K if isinstance(n,str)]
L2 = [s.lower() for s in l]
# 测试:
print(L2)
if L2 == ['victor','jack','mike','amber']:
    print('测试通过!')
else:
    print('测试失败!')

L1 = ['Victor','Jack',18,'Mike','Amber']
# 只保留字符串
L3 = [x.lower() for x in L1 if isinstance(x,str)] 
# 测试:
print(L3)
if L3 == ['victor','jack','mike','amber']:
    print('测试通过!')
else:
    print('测试失败!')

# 全部保留，非字符串不改变
L4 = [x.lower() if isinstance(x,str) else x for x in L1] 
# 测试:
print(L4)
if L4 == ['victor','jack',18,'mike','amber']:
    print('测试通过!')
else:
    print('测试失败!')