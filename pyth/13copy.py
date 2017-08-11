#!/usr/bin/python
#coding=utf-8
import copy
l = [1,[4,5,6],8]
l1 = l                       # l变l1就会改变
l2 = copy.copy(l)              #除了l列表里的列表改变，其余保持不变
l3 = copy.deepcopy(l)             #始终不变

print l,"   ",l1,"   ",l2,"   ",l3

l[0]=9                         #下面元组的值不能改变

print l,"   ",l1,"   ",l2,"   ",l3

l[1][0]=2

print l,"   ",l1,"   ",l2,"   ",l3


t = (1,[2,3],4)                        #显然与列表一样
t1 = t
t2 = copy.copy(t)
t3 = copy.deepcopy(t)

t[1][0] = 5

print t,"   ",t1,"   ",t2,"   ",t3
