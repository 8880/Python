#!usr/bin/python

class Person(object):
    age = 10
    name = 'xiaoming'

    def color(self,c):
        print '%s is %s,he is %d'%(self.name,c,self.age)


boy = Person()

print boy.age

print boy.name

boy.color('superman')
