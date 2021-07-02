# -*- coding: utf-8 -*-
# Python内置的sorted()函数就可以对list进行排序
l = sorted([36,5,-12,9,-21])
print(l)

# 此外，sorted()函数也是一个高阶函数，
# 它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
l = sorted([36,5,-12,9,-21],key=abs)
print(l)

# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面
s = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(s)

# 忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较。
# 这样，我们给sorted传入key函数，即可实现忽略大小写的排序
s = sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower)
print(s)

s = sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.upper)
print(s)

# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
s = sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.upper,reverse = True)
print(s)

# 从上述例子可以看出，高阶函数的抽象能力是非常强大的，而且，核心代码可以保持得非常简洁。

# 小结
# sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。

'''
练习
假设我们用一组tuple表示学生名字和成绩：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
请用sorted()对上述列表分别按名字排序
'''
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    name = t[0].lower()
    return name

L2 = sorted(L, key=by_name)
print(L2)

def by_score(t):
    return t[1]
    # score = t[1]
    # return score 

# 默认按照从小到大的排序
L2 = sorted(L, key=by_score,reverse=True)
print(L2)