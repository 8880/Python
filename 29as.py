#!/usr/bin/python
#coding=utf-8

def div(a,b):
    try:
        c = a / b
    except ZeroDivisionError as e:              # as 打印错误的提示语句
        return e
    except TypeError as e:                      #也可以用Exception
        return e
    else:                                      #无错误的情况下执行
        print "else........."
    finally:                                   #无论对错都会执行
        print "finally......."

    return c

#def div(a,b):
#    try:
#        return a / b
#    except(ZeroDivisionError,TypeError) as e:
#        return e

result = div(3,'k')
print result
