# -*- coding: utf-8 -*-
#list是一种有序的集合，可以随时添加和删除其中的元素
classmates = ['Victor','Alex','BeyondCode','Mark']
print(classmates)
#用len()函数可以获得list元素的个数
print(len(classmates))
#用索引来访问list中每一个位置的元素，记得索引是从0开始的
print(classmates[0])
#还可以用-1做索引，直接获取最后一个元素
print(classmates[-1])
print(classmates[-2])

#list是一个可变的有序表，所以，可以往list中追加元素到末尾
print(classmates)
classmates.append('Alvis')
print(classmates[-1])

#可以把元素插入到指定的位置，比如索引号为1的位置
print(classmates)
classmates.insert(1,'Jack')
print(classmates[1])
#要删除list末尾的元素，用pop()方法
print(classmates)
classmates.pop()
print(classmates[-1])
print(classmates)

#要删除指定位置的元素，用pop(i)方法，其中i是索引位置
classmates.pop(1)
print(classmates)

#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[2] = 'Code'
print(classmates)

#list里面的元素的数据类型也可以不同
L = ['Apple',123,True]
print(L)

#list元素也可以是另一个list
s = ['Python','Java',['PHP','C'],'go']
print(len(s))
print(s[2][1])

p = ['asp','jsp']
L.append(p)
print(L)
print(p[1])
print(L[3][1])