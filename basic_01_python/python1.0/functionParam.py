# -*- coding: utf-8 -*-
#参数中n = 2是默认参数
def power(x,n=2):
    if not isinstance(x,(int,float)):
        raise TypeError('wrong param')
    if not isinstance(n,(int,float)):
        raise TypeError('wrong param')
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
#参数中n = 2是默认参数，所以调用的时候可以单参数调用
#必选参数在前，默认参数在后
m = power(15)
print(m)
k = power(2,10)
print(k)

#默认参数有什么好处？最大的好处是能降低调用函数的难度。
#举个例子，我们写个一年级小学生注册的函数，需要传入name和gender两个参数
def enroll(name,gender):
    print('name:',name)
    print('gender:',gender)

#这样，调用enroll()函数只需要传入两个参数：
enroll('Jasmine','F')
#如果要继续传入年龄、城市等信息怎么办？这样会使得调用函数的复杂度大大增加。
#我们可以把年龄和城市设为默认参数：
def enroll2(name,gender,age=6,city='beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)

enroll2('Jasmine2','F')
#只有与默认参数不符的学生才需要提供额外的信息：
enroll2('Jasmine3','F',9,'tianjing')

enroll2('Bob', 'M', 7)
enroll2('Adam', 'M', city='Tianjin')

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

sum0 = calc([1,2,3])
print('sum0 = ',sum0)

#函数的参数改为可变参数
def calc1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

sum1 = calc1(1,2,3)
print('sum1 = ',sum1)

nums = [1,2,3]
sum2 = calc1(nums[0],nums[1],nums[2])
print('sum2 = ',sum2)
#sum2写法太繁琐，可以用下面的方法替代
#这种写法相当有用，而且很常见
sum3 = calc1(*nums)
print('sum3 = ',sum3)

