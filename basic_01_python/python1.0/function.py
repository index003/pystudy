# -*- coding: utf-8 -*-
h = hex
n1 = 255
n2 = 1000
for i in(n1,n2):
    print(h(i)) 

def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

print(my_abs(100))
print(my_abs(-99))

#如果想定义一个什么事也不做的空函数，可以用pass语句
#pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
def nop():
    pass

#pass还可以用在其他语句里，比如：
age = 18
if age > 18:
    pass
#缺少了pass，代码运行就会有语法错误。

#参数检查

def my_n_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
       return x
    else:
        return -x

print(my_n_abs(98))
print(my_n_abs('A'))
