#!/usr/bin/python
#coding=utf-8

a = 5
b = 4
def fun():
    global a,b
    a += 1
    b += 1
    print a,b

    c,d = 1,2
    return locals()                    #局部变量生成字典

print fun()
print a

print globals()
