# !/usr/bin/python2
# -*- coding: utf-8 -*-
# @Time    : 2019/9/12 12:15 上午
# @Author  : aogo
# @File    : test_while.py

num = 1
while num < 10:
    print num
    num += 1
print ('done')

# 使用while循环遍历元组
aogo_tuple = ['hello', 'world', 'aogo']
i = 0
while i < len(aogo_tuple):
    print aogo_tuple[i]
    i += 1
print ('done')
# hello
# world
# aogo
# done

# 使用while循环遍历列表，分别存放整除3余数为0、1、2
aogo_list = [12, 45, 34, 13, 100, 24, 56, 74, 109]
a_list = []
b_list = []
c_list = []
while len(aogo_list):
    ele = aogo_list.pop()
    if ele % 3 == 0:
        a_list.append(ele)
    elif ele % 3 == 1:
        b_list.append(ele)
    else:
        c_list.append(ele)

print ("divide 3", a_list)
print ("divide 3 by 1", b_list)
print ("divide 3 by two", c_list)

# ('divide 3', [24, 45, 12])
# ('divide 3 by 1', [109, 100, 13, 34])
# ('divide 3 by two', [74, 56])

