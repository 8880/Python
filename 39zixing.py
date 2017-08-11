#!/user/bin/python
#coding=utf-8

#hasattr  getattr  setattr  delattr  isinstance  issubclass


class Parent(object):
    name = 'FangKun'

class Child(Parent):
    pass


p = Parent()
print issubclass(Child,Parent)
print isinstance(p,Parent)

print "---------------------------"

print hasattr(p,'name')

print getattr(p,'name')

setattr(p,'age',23)

# delatter(p,'age')
# delattr(p,'name')

print p.age
