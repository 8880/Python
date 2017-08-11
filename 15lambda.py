#!/usr/bin/python
#coding=utf-8

def fun(x):
    return x % 2


temp = range(10)
show = filter(fun,temp)            #filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
print show

print '------------------------------'

print filter(lambda x : x % 2, range(10))

#lambda 创建一个匿名函数。冒号前面是传入参数，后面是一个处理传入参数的单行表达式。
