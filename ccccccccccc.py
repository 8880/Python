#!/usr/bin/python
#coding=utf-8

class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print 'Parent'

    def bar(self,message):
        print message,'from Parent'

class FooChild(FooParent):
    def __init__(self):
        super(FooChild,self).__init__()  #调用父类初始化方法
        print 'Child'

    def bar(self,message):
        super(FooChild, self).bar(message)  #调用父类bar方法
        print 'Child bar fuction'
        print self.parent

if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')
