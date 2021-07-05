# -*- coding: utf-8 -*-
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回

from typing import FrozenSet


def calc_sum(*args):
    ax = 0
    for x in args:
        ax = ax + x
    return ax

f = calc_sum(1,2,3,4,5,6)
print(f)

# 如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？
# 可以不返回求和的结果，而是返回求和的函数

def lazy_sum(*args):
    def sum():
        ax = 0
        for x in args:
            ax = ax + x
        return ax
    return sum

# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数
f = lazy_sum(1,2,3,4,5,6)
print(f)
# 调用函数f时，才真正计算求和的结果
f = f()
print(f)

# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，
# 并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
# 这种称为“闭包（Closure）”的程序结构拥有极大的威力。

# 请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)
if f1 == f2:
    print("相同")
else:
    print("不相同")

# f1()和f2()的调用结果互不影响
# 闭包
# 注意到返回的函数在其定义内部引用了局部变量args，
# 所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，
# 所以，闭包用起来简单，实现起来可不容易。

# 另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())

# 在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了
# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。
# 等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9

# 如果一定要引用循环变量怎么办？
# 方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))# f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())
        
# 练习
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：

def createCounter():
    f = [0]
    print('闭包外--')
    def counter():
        print('闭包内--')
        f[0] = f[0] + 1
        return f[0]
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

'''
输出： 闭包外-- 闭包内-- 闭包内-- 闭包内-- 闭包内-- 闭包内-- 1 2 3 4 5

建议新手这样跑一下，即可知道2个结论： 
1）同一个返回函数对象，重复执行的时候，仅跑函数内的内容。返回函数外的内容是跑1次 
2）假如是这么写：

def counter():
    print('闭包中--')
    f[0] = f[0] + 1
    return f
print是等内容全部执行完，再输出的。
很简单就可以测试：print(2, 3, 1/0)，并不会输出2和3。（没找底层代码，就这么反推出结论不会被打脸吧。。） 
那么当都运算完毕，f变量已经存了最后一个值。
反过来假设是f[0]，这个不是可变量。
'''