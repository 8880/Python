#!/usr/bin/python
#coding=utf-8

class ParentClass(object):
    name = '上帝'

    def func(self):
        print '阿门'

class ChildClass(ParentClass):
    name = '恶魔'

    def fun(self):
        print 'asa'

class GrentChildClass(ChildClass):
    pass


child = ChildClass()

print child.name

child.func()

grent_child = GrentChildClass()

print grent_child.name
