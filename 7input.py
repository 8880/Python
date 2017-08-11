#!/usr/bin/python
#coding=utf-8

a,c = input("请输入:")              #python2 输入中文 必须写第二行的代码
                                   #input 只能输入数字
print "a = %d"%a
print "c =",c

b = raw_input()                   # 可以输入数字或字符或字符串 但是显示类型都是字符类型

print "b =",b
print type(b)
