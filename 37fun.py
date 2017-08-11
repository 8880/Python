#!/user/bin/python
#coding=utf-8
import datetime

def deco(arg):                       #装饰器传参需要在加一个函数
    def begin(func):
        def wrapper(*args,**kwargs):
            print arg
            print "现在时间:"
            func(*args,**kwargs)
        return wrapper
    return begin

@deco('sssss')
def getTime(a,b,c,d):
    print a,b,c,d
    print datetime.datetime.now()


getTime(1,2,3,4)
