# -*- coding: utf-8 -*-
#取一个list或tuple的部分元素是非常常见的操作
L = ['Jack','Mike','Victor','Tiger']
print(L)
#取前3个元素，应该怎么做
print([L[0],L[1],L[2]])
#取前N个元素，也就是索引为0-(N-1)的元素，可以用循环
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)
#对这种经常取指定索引范围的操作，用循环十分繁琐
#对应上面的问题，取前3个元素，用一行代码就可以完成切片
print(L[0:3])
#从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素
#如果第一个索引是0，还可以省略
print(L[:3])
#也可以从索引1开始，取出2个元素出来
print(L[1:3])
#Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
print(L[-2:-1])
print(L[-2:])

#可以通过切片轻松取出某一段数列
M = list(range(100))
#前10
print(M[:10])
#后10
print(M[-10:])
#前11-20个数
print(M[10:20])
#前10个数，每两个取一个
print(M[:10:2])
#所有数，每5个取一个
print(M[::5])
#什么都不写，只写[:]就可以原样复制一个list
print(M[:])

#tuple也是一种list，唯一区别是tuple不可变。
#因此，tuple也可以用切片操作，只是操作的结果仍是tuple
T = tuple(range(100))
print(T[:10:2])

#字符串'xxx'也可以看成是一种list，每个元素就是一个字符。
#因此，字符串也可以用切片操作，只是操作结果仍是字符串
#Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单。
s = 'victorwu'
print(s[1:3])

#练习：利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s
print(trim('abcde fg'))
print(trim(' abcde fg '))

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
