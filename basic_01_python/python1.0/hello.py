# -*- coding: utf-8 -*-
print("Hello world")
print("hello","world","game","work")
name = input("please input your name:")
print ("hello,",name)
print("1024 * 768 =",1024*768)

#以#开头的语句是注释
#语法比较简单，采用缩进方式
#按照约定俗成的惯例，应该始终坚持使用4个空格的缩进
#当语句以冒号:结尾时，缩进的语句视为代码块
#Python程序是大小写敏感的，如果写错了大小写，程序会报错
a = 100
if(a>=100):
    print(a)
else:
    print(1000)

#在Python中使用单引号或双引号是没有区别的，都可以用来表示一个字符串

#包含单引号的字符串，用双引号，如下
my_str = "I'm a student"
print(my_str)
#包含双引号的字符串,用单引号，如下
my_str = 'Jason said "I like you"'
print(my_str)

#如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识
my_str = 'I\'m \"OK\"!'
print(my_str)

age = 20
if age >= 18:
    print("adult")
else:
    print("teenager")

#变量名必须是大小写英文、数字和_的组合，且不能用数字开头
#等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
#用全部大写的变量名表示常量
#/除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数
my_int = 10 / 3
print(my_int)
#//称为地板除，两个整数的除法仍然是整数
my_int = 10 // 3
print(my_int)
#%余数运算，可以得到两个整数相除的余数
my_int = 10 % 3
print(my_int)

my_str = "中文"
print(my_str)
#最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言，
str = "包含中文的变量str"
print(str)

#ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord("A"))
print(chr(65))


