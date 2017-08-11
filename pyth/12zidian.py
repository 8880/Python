#!/usr/bin/python
#coding=utf-8

d = {}

print type(d)

d = {'a':1,'b':2,32:100,'one':1}

print "%(a)d"%d                         #与下面显示一样
print d['b']
print d.get('a')

d1 = d.copy()                            #复制字典
print d1

q = d.values()                         #查看所有字典里的值
print q

w = d.items()                         #把字典里的值变成列表
print w

e = d.has_key('a')                   #查看是否在字典里
print e

d.update({'k':888})                  #加入一个内容
print d

l = d.pop('k')                      #弹出‘k’值
print l
print d
