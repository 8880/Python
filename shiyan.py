#!/usr/bin/python

class A(object):
    def __init__(self):
        self.weight = 180

    def about(self,name):
        print "{} is {}".format(name,self.weight)

class B(A):
    def __init__(self):
        self.height = 50
        super(B,self).__init__()
    def about(self,name):
        print "{} is {} and {}".format(name,self.weight,self.height)


a = B()
a.about('dawang')
