#!/usr/bin/python
# coding=utf-8
import copy

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1)

print t.count(1)

print t.index(3, 1, 10)                # 在l列表里从1到10范围内，查找3在哪个位置，应该显示2

print sum(t)                         #把元组里的数相加

# 元组只有这两个命令可以使用


r = (1, 2, 3, [5, 4], 6)

r1 = copy.copy(r)            #copy.deepcopy  不会改变元组里列表的值 除了这个 别的元组的值不能改变

print r, r1

r[3][0]=9

print r, r1
