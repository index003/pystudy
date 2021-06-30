# -*- coding: utf-8 -*-
weight = 80.5
height = 1.75
pBMI = weight / (height * height) 
print(pBMI)
'''
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
'''
if pBMI > 32:
    print('严重肥胖')
elif pBMI > 28:
     print('肥胖')
elif pBMI > 25:
     print('超重')
elif pBMI >18.5:
    print('正常')
else:
    print('过轻')

