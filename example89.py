# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/11 0011 上午 11:41'

"""
题目：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，
加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
"""
if __name__ == "__main__":
    n = input("请输入一个四位数")
    l = []
    for i in range(4):
        l.append((int(n[i])+5) % 10)
        l[i] = str(l[i])

l = l[3]+l[2]+l[1]+l[0]
print(l)
