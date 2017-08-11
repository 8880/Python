#!/usr/bin/python
#coding=utf-8

#def div(a,b):
#    try:
#        return a / b
#    except ZeroDivisionError:                    # 写入相应类型的错误 会执行 不加错误类型也会执行
#        return "zero can not be division"

def div(a,b):                                   #只要有两种错误其中的一种，就会显示下面的内容
    try:
        return a / b
    except(ZeroDivisionError,TypeError):
        return "division error or type error"

result = div(3,'c')
print result
