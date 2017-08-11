#!/usr/bin/python
#coding=utf-8

a = 6
l = [1,2,3,4,5,a,7,8,9,'a',11,12,1]
l1 = [4,5,87,0]

print len (l)

print l[1:5]

print l[1:11:2]

print 5 in l      ,            ;print 544 in l

print l*2

print l + l1

print l.count(1)               #查看列表里的数字1有几个

y = l.append(8)                    #在列表里加入一个数
print y

l1.extend([1,2,3])              #在列表里加入一组数
print l1

l.index(3,1,10)                # 在l列表里从1到10范围内，查找3在哪个位置，应该显示2

l1.insert(3,100)               #在下标为3的位置 插入100
print l1

l1.pop()                       #弹出最后一个数
print l1
print l1.pop()                  #pop弹出去的返回值


l.remove(2)                     #删除2这个数字
print l

l.reverse()                    #从后往前排序
print l

l1.sort()                      #从小到大排序           max(l)  查看列表里的最大值 min最小值
print l1

def cmp(x,y):                  #从大到小排序  或者  l1.sort(reverse = True)直接转换
    return y - x
l1.sort(cmp = cmp)
print l1

del l[4:8]                   #删除4到8
print l
