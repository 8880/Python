#!/usr/bin/python
#coding=utf-8

class Person(object):
    def __init__(self,nam,ag):                   #初始化函数
        self.name = nam
        self.age = ag

    age = 10
    name = 'moren'
    face = '帅'


    def color(self,c):
        print '%s is %s,he is %d'%(self.name,c,self.age)


boy = Person('xiaom',55)
boy.age = 22                           #后面的会把前面的覆盖掉
print boy.age


print boy.name

print boy.face

boy.color('pig')
