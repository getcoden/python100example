# -*- coding:utf-8 -*-
__author__ = 'gjw'
__time__ = '2018/1/3 0003 上午 10:23'
"""
    题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
    利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
    20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
    60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
"""

# 程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。
i = input('净利润(元）：')
i = float(i)/10000
r = 0
# 基础版

if i <= 10:
    r = 0.1 * i
if 10 < i <= 20:
    r = 10 * 0.1 + (i-10) * 0.075
if 20 < i <= 40:
    r = 10 * 0.1 + 10 * 0.075 + (i-20) * 0.05
if 40 < i <= 60:
    r = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + (i-40)*0.03
if 60 < i <= 100:
    r = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + (i-60)*0.015
if i > 100:
    r = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + 40 * 0.015 + (i-100)*0.01
print('奖金总数：'+str(r*10000))


# 前面的方法太过于原始，根据程序分析给出的方法，可以把它们分成界限
print("我是优化版")
arr = [100, 60, 40, 20, 10, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
r = 0
for idx in range(0, 6):
    if i > arr[idx]:
        r += (i-arr[idx])*rat[idx]
        print((i-arr[idx])*rat[idx]*10000)
        i = arr[idx]
print("最终结果:"+str(r*10000))