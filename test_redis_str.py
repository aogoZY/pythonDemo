# !/usr/bin/python2
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 12:12 上午
# @Author  : aogo
# @File    : test_redis_str.py

import redis


conn = redis.StrictRedis(host="127.0.0.1", port=6379)

# redis操作string类型
# 增
print(conn.set('name', 'aogo'))  # string类型的插入键值对,参数key，value；返回true或False
print (conn.get('name'))         #  aogo

print(conn.setex('name2', 10, 'amao'))  # 设置一个有保存时间的键值对,返回true或false
print (conn.get('name2'))

print(conn.mset({'age': 18, 'color': 'blue'}))  # 设置多个键值对，返回true或false
print(conn.mget('age', 'color'))            # ['18', 'blue']

# 删
print (conn.delete('age'))  # 删除多个键值对，获取删除成功的数量
print (conn.get('age'))     # None

# 改
conn.set('nums', 10)
print(conn.incr('nums'))      # 值自加操作，返回计算后的结果值 11
print(conn.incr('nums', '23'))  # 值加一个整数操作，返回计算后的结果值 34

print(conn.decr('nums'))  # 值自减操作，返回计算后的结果值  # 33

print(conn.append('boy', 'tom'))  # 字符串拼接，参数key value，返回当前字符串的长度
print (conn.get('boy'))     # tomtomtomtom
print(conn.setrange('name', '5', 'hh'))  # 字符串替换字符，参数为键、偏移量、值，返回当前字符串的长度

# 查
print(conn.get('color'))       # 获取键的值，返回二进制的数据 blue
print(conn.getrange('color', 0, 2))  # 获取子串，参数key、下标范围  blu
print(conn.strlen('color'))  # 获取值的长度   4
print(conn.exists('color'))  # 是否存在这个键，针对所有的类型 1