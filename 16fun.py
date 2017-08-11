#!/usr/bin/python
#coding=utf-8
def func():                   #定义一个函数
    print "hello kitty"


func()                         #调用函数



def fun1():                            #函数的嵌套
    print 'fun1()正在被调用...'
    def fun2():
        print 'fun2()正在被调用...'
    fun2()


fun1()
