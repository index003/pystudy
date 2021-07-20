# -*- coding: utf-8 -*-
# 生成器
# 创建一个generator，有很多种方法。
# 第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
L = [x * x for x in range(1,11)]
print(L)

g = (x * x for x in range(1,11))
# 使用for循环读取generator
for n in g:
    print(n)

# 如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现
# 比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a + b
        n = n + 1
    return 'done'

'''
注意，赋值语句：
a, b = b, a + b
相当于：
t = (b, a + b) # t是一个tuple
a = t[0]
b = t[1]
'''
f = fib(6)
print(f)

# 第二种方法
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator

def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

for n in fib2(6):
    print(n)

# fib2拿不到return的值

# 按照下面的方式可以取到done
g = fib2(7)
while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

'''
generator是非常强大的工具，在Python中，可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator。
要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。
对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。
请注意区分普通函数和generator函数，普通函数调用直接返回结果,generator函数的“调用”实际返回一个generator对象

在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行

'''

'''
杨辉三角定义如下：

          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1

把每一行看做一个list，试写一个generator，不断输出下一行的list
'''
def triangles():
    N=[1]   # 初始化为[1],杨辉三角的每一行为一个list
    while True:
        yield N # yield 实现记录功能，没有下一个next将跳出循环，
        S=N[:]  # 将list N赋给S，通过S计算每一行
        S.append(0) # 将list添加0，作为最后一个元素，长度增加1
        N=[S[i-1]+S[i] for i in range(len(S))]  # 通过S来计算得出N

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

