#!/usr/bin/python
#coding=utf-8
s = {1,1,2,3,4,5,6}                     #集合不能有重复值

print s

print type(s)

s1 = {}

print type(s1)

s2 = set([])

print type(s2)

s3 = s - {1,2,3}

print s3

d = {5,6,7,8}

# s | d    s & d      s ^ d         s.add()      s.clear()    s.update()
#  并集     交集   并集之后去掉交集    添加一个     清除集合里的值    添加多个     

j = frozenset({1,2,3,4})      #创建不可变的集合
