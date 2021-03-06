# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/5 0005 下午 4:47'

# 题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。


from sys import stdout

for j in range(2, 1001):
    k = []
    n = -1
    s = j
    for i in range(1, j):
        if j % i == 0:
            n += 1
            s -= i
            k.append(i)

    if s == 0:
        print(j)
        for i in range(n):
            print(str(k[i]),end="")
            print(" ",end="")
        print(k[n])

# 进阶版
print("我是进阶版")
for i in range(1, 1001):
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum += j
    if sum == i:
        print(i)