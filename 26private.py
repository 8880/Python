#!/usr/bin/python
#coding=utf-8

class Parent(object):
    def __init__(self):
        self.job = 'teacher'
        self.__name = 'cainiao'               # __ 表示私有 不能在外部使用，只能在内部使用
                                              #要想使用，定义方法
    def name(self,n):
        if n == 1:
            return self.__name
        else:
            return 'sorry'


class Child(Parent):
    pass

#c = child()

#print c.__name


p = Child()
print p.job

print p.name(1)
