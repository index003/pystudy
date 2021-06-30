# -*- coding: utf-8 -*-

def maxNum(x,y):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if not isinstance(y,(int,float)):
        raise TypeError('bad operand type')
    if(x>y):
        return x
    else:
        return y
#max = maxNum(3,'x')
max = maxNum(3,9)
print(max)