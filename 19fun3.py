#!usr/bin/python
#coding=utf-8

#定义位置参数的函数
def fun(a,b):
    print a,b

fun(1,2)

#设置参数默认值
def fun1(a,b = 100):               #把有默认参数的放在后面
    print a,b

fun1(1)

#定义收集参数的函数

def fun2(*a):
    print a

fun2(1,3,4,5)

#收集字典参数

def fun3(**a):
    print a

fun3(a = 1,b = 2,c = 3)

# *传参放在后面
def fun(a,*b):
    print a
    print b

fun(1,2,3,4,5)

print"---------------------------"
#都有的参数
def fun4(a,b = 100,*c,**d):                     #python3中 def fun(a,b=100,*c,d)
    print a                                     #*c后还可以加值
    print b
    print c
    print d

fun4(1,2,3,4,5,c = 6,d =7)
