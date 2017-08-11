#!/usr/bin/python
#coding=utf-8

s = 'hello{1},nihao{0}'.format('yi','er')                #在字符串中插入

print s

l = 'hello world'

a = l.split(' ')              #将字符串从空格两面拆开
print a

b = '1'.join(l)                 #在字符直接插入1
print b

t = l.replace("l","2")          #把l替换成2
print t

m = l.split("l")                 #方法与上面一样i
o =','.join(m)
print o

t = '    hello   '

c = t.lstrip()          # l 清除左面空格  r清除右面空格     strip清除前后空格
print c

l1 = '{},{}'.format('cat',5)          #映射

print l1
