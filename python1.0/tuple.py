# -*- coding: utf-8 -*-
#tuple和list非常类似，但是tuple一旦初始化就不能修改
#现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。
# 其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
#初始化时list是[],tuple是（）
classmates = ('Victor','Jack','Mark')
#读取的时候是[]
print(classmates[0])
#不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。

#只有1个元素的tuple定义时必须加一个逗号,否则就成了括号，不是tuple
#括号
t1 = (1)
print(t1)
#tuple
t2 = (1,)
print(t2)
print(t2[0])

#表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。
# tuple一开始指向的list并没有改成别的list，
# 所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
# 即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，
# 但指向的这个list本身是可变的！
t3 = ('a','b',['A','B'])
print(t3)
t3[2][0] = 'X'
t3[2][1] = 'Y'
print(t3)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[-1][-1])

