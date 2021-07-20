# -*- coding: utf-8 -*-
#dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
#dict的key必须是不可变对象
#通过key计算位置的算法称为哈希算法（Hash）
#字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key
#初始化要用{}
d = {'Victor':90,'Amber':99,'Jasmine':100,'Thomas':60}
print(d['Amber'])

#把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
#由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
d['Victor'] = 91
print(d['Victor'])
d['Victor'] = 92
print(d['Victor'])
d['Victor'] = 93
print(d['Victor'])

bt = 'Thomas' in d
print(bt)
bt = d.get('Thomas')
print(bt)
bf = 'Jack' in d
print(bf)
bf = d.get('Jack')
print(bf)

#要删除一个key，用pop(key)方法，对应的value也会从dict中删除
bt = d.get('Thomas')
print(bt)
d.pop('Thomas')
bf = d.get('Thomas')
print(bf)

#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
#要创建一个set，需要提供一个list作为输入集合
s = set([1,2,3])
#传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。。
print(s)
#重复元素在set中自动被过滤：
s = set([1,1,2,2,2,3,3,3,3,3])
print(s)
#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(4)
print(s)
#通过remove(key)方法可以删除元素
s.remove(4)
print(s)
#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1,2,3])
s2 = set([2,3,4])
# &===and，交集
s = s1 & s2
print(s)
# |===or,并集
s = s1 | s2
print(s)

#set的原理和dict一样，所以，同样不可以放入可变对象

