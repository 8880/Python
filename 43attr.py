#!/user/bin/python
# coding=utf-8
class A(object):
    def __getattr__(self,name):
        print "You use getattr no attr %s"%name
        return "NO"

    def __setattr__(self,name,value):
        print "You use setattr"
        self.__dict__[name] = value

a = A()

print a.k
a.x = "set x"

# setattr(self,name,value):如果要给name赋值，就会自动调用这个方法
# getattr(self，name):如果name被访问，但同时它不存在，则自动调用这个方法。
