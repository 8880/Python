#!/usr/bin/python

class Person(object):
    def __init__(self):
        self.height = 165

    def about(self,name):
        print "{} is about {}".format(name,self.height)

class Girl(Person):
    def __init__(self):
        self.weight = 98
        super(Girl,self).__init__()

    def about(self,name):
        print "{} is a girl,she is about {} and her weight is {}".format(name,self.height,self.weight)
#        super(Girl,self).about(name)
class boy(Girl):
    def about(self,name):
        print "ssssss%s"%name
        super(boy,self).about(name)


Chan = Girl()
Chan.about("DiaoChan")
print '----------------------------'

super(Girl,Chan).about("Zhenfu")
#print Girl.__mro__
print '-------------------'

a = boy()
a.about("ddfff")
