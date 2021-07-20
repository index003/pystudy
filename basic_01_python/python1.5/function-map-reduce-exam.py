# -*- coding: utf-8 -*-
# 练习1：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']

def normalize(name):
    name = name[0].upper() + name[1:].lower()
    return name 
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 练习2：Python提供的sum()函数可以接受一个list并求和，
# 请编写一个prod()函数，可以接受一个list并利用reduce()求积

from functools import reduce
def prod(L):
    def mult(a,b):
        return a * b
    return reduce(mult,L)
# 测试代码
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

def mult(a,b):
    return a * b

def prod1(L):
    return reduce(mult,L)
# 测试代码
print('3 * 5 * 7 * 9 =', prod1([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

def prod2(L):
    return reduce(lambda x, y: x * y, L)
# 测试代码
print('3 * 5 * 7 * 9 =', prod2([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 练习3：利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2float(s):
    # fn：输入两个数，输出一个数字，例如输入2，3，输出23
    def fn(x,y):
        return 10*x + y
    #  char2num：将字符串转换成数字，例如输入‘12345’，输出list:[1，2，3，4，5]
    def char2num(s):
        return DIGITS[s]
    # 找到小数点位置
    index = s.find('.')
    # print(index)
    # 用MAP函数分别生成小数点前后的LIST
    # 例如：123.456,输出：[1，2，3]和[4，5，6]
    L1 = list(map(char2num,s[:index]))
    # print(L1)
    L2 = list(map(char2num,s[index+1:]))
    # print(L2)
    # print(len(L2))
    # print(reduce(fn,L1))
    # print(reduce(fn,L2))
    # 用REDUCE函数计算小数点前后对应的数字
    # 例如：[1，2，3]和[4，5，6],输出：123和456
    # 将2个数相加
    return reduce(fn,L1)+reduce(fn,L2)/10**len(L2)

#测试代码
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
