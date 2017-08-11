#!/usr/bin/python
#coding=utf-8

class Calculator(object):
    name = 'luosifu'
    age = 88

class Talker(object):
    name = 'mengfei'
    sex = 'man'

class TalkCalculator(Talker,Calculator):           #先继承前面的
    pass

A = TalkCalculator()


print A.age
print A.sex
print A.name


print TalkCalculator.__mro__                  #查看继承顺序
