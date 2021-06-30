# -*- coding: utf-8 -*-
#Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
names = ['Victor','Jack','Mark']
for name in names:
    print(name)

lastnames = ("赵","钱","孙","李")
for lastname in lastnames:
    print(lastname)

#Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。
# 比如range(5)生成的序列是从0开始小于5的整数：

numbers = range(5)
print(numbers)
for number in numbers:
    print(number)
#Python的语法比较简单，采用缩进方式,print(sum)要缩进，不缩进的话会有问题
sum = 0
numbers = range(101)
for number in numbers:
    sum = sum + number
print(sum)

#第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。
# 比如我们要计算100以内所有奇数之和，可以用while循环实现
#在循环内部变量n不断自减，直到变为-1时，不再满足while条件，循环退出
sum = 0 
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

L = ['Java','Python','PHP']
for l in L:
    print('Hello,',l)


n = 1
while n<=100:
    print(n)
    n = n + 1
print('END')

#break语句可以提前退出循环
n = 1
while n<=100:
    if n>10:
        break
    print(n)
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n + 1
    print(n)

#continue语句，跳过当前的这次循环，直接开始下一次循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)

#break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。
#这两个语句通常都必须配合if语句使用。
#要特别注意，不要滥用break和continue语句。
# break和continue会造成代码执行逻辑分叉过多，容易出错。
# 大多数循环并不需要用到break和continue语句，
# 上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。