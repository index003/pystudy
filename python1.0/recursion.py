# -*- coding: utf-8 -*-
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
m = fact(5)
print(m)

#汉诺塔

def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)  # 直接搬过去
    else:
        move(n-1, a, c, b)          # 先把a上面的n-1个盘子搬到b
        move(1, a, b, c)            # 然后把最后1个盘子搬到c
        move(n-1, b, a, c)          # 最后再把b上的n-1个盘子搬到c
move(4, 'A', 'B', 'C')
